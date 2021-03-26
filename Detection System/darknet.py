import copy
import cv2
import darknet
from ctypes import *
import pyqtgraph as pg
import IntelligentTrafficSystem
# from PIL import ImageFont
from PyQt5.QtGui import *
from main_module.sql import insertIllegal
from main_module.detection import *
from main_module.init_and_save_xml import *
from main_module.tools import illegal_action_list

# weights_path = "./weights/yolov4-car.weights"
# weights_path = '/root/PycharmProjects/temp_file/yolov4.weights'
weights_path = '/home/tinynoconv/yolov3-tiny_last.weights'
# config_path = "./cfg/yolov4-voc_car.cfg"
# config_path = '/root/PycharmProjects/yolo/cfg/yolov4.cfg'
config_path = '/root/PycharmProjects/yolo/cfg/yolov3-tiny.cfg'
meta_path = "./cfg/voc.data"                                                     # 5 classes
# meta_path = '/root/PycharmProjects/yolo/cfg/coco.data'                         # 80 classes

ID = 0
sum = 0
use_index = 0
not_stop = True
widthMul = 2.1
heightMul = 1.2
license2id = dict()
object_show_list = []
peopleCntBook = []
carCntBook = []
recordDB = dict()
# font = ImageFont.truetype("/root/SourceHanSerifSC-SemiBold.otf", 20, encoding="utf-8")  # 参数1：字体文件路径，参数2：字体大小
pg.setConfigOption('background', '#1F2429')


class BOX(Structure):
    _fields_ = [("x", c_float),
                ("y", c_float),
                ("w", c_float),
                ("h", c_float)]


class DETECTION(Structure):
    _fields_ = [("bbox", BOX),
                ("classes", c_int),
                ("prob", POINTER(c_float)),
                ("mask", POINTER(c_float)),
                ("objectness", c_float),
                ("sort_class", c_int),
                ("uc", POINTER(c_float)),
                ("points", c_int)]


class DETNUMPAIR(Structure):
    _fields_ = [("num", c_int),
                ("dets", POINTER(DETECTION))]


class IMAGE(Structure):
    _fields_ = [("w", c_int),
                ("h", c_int),
                ("c", c_int),
                ("data", POINTER(c_float))]


class METADATA(Structure):
    _fields_ = [("classes", c_int),
                ("names", POINTER(c_char_p))]


hasGPU = True
if os.name == "nt":
    cwd = os.path.dirname(__file__)
    os.environ['PATH'] = cwd + ';' + os.environ['PATH']
    winGPUdll = os.path.join(cwd, "yolo_cpp_dll.dll")
    winNoGPUdll = os.path.join(cwd, "yolo_cpp_dll_nogpu.dll")
    envKeys = list()
    for k, v in os.environ.items():
        envKeys.append(k)
    try:
        try:
            tmp = os.environ["FORCE_CPU"].lower()
            if tmp in ["1", "true", "yes", "on"]:
                raise ValueError("ForceCPU")
            else:
                print("Flag value '" + tmp + "' not forcing CPU mode")
        except KeyError:
            # We never set the flag
            if 'CUDA_VISIBLE_DEVICES' in envKeys:
                if int(os.environ['CUDA_VISIBLE_DEVICES']) < 0:
                    raise ValueError("ForceCPU")
            try:
                global DARKNET_FORCE_CPU
                if DARKNET_FORCE_CPU:
                    raise ValueError("ForceCPU")
            except NameError:
                pass
            # print(os.environ.keys())
            # print("FORCE_CPU flag undefined, proceeding with GPU")
        if not os.path.exists(winGPUdll):
            raise ValueError("NoDLL")
        lib = CDLL(winGPUdll, RTLD_GLOBAL)
    except (KeyError, ValueError):
        hasGPU = False
        if os.path.exists(winNoGPUdll):
            lib = CDLL(winNoGPUdll, RTLD_GLOBAL)
            print("Notice: CPU-only mode")
        else:
            # Try the other way, in case no_gpu was
            # compile but not renamed
            lib = CDLL(winGPUdll, RTLD_GLOBAL)
            print(
                "Environment variables indicated a CPU run, but we didn't find `" + winNoGPUdll + "`. Trying a GPU run anyway.")
else:
    lib = CDLL("./libdarknet.so", RTLD_GLOBAL)
lib.network_width.argtypes = [c_void_p]
lib.network_width.restype = c_int
lib.network_height.argtypes = [c_void_p]
lib.network_height.restype = c_int

copy_image_from_bytes = lib.copy_image_from_bytes
copy_image_from_bytes.argtypes = [IMAGE, c_char_p]


def network_width(net):
    return lib.network_width(net)


def network_height(net):
    return lib.network_height(net)


predict = lib.network_predict_ptr
predict.argtypes = [c_void_p, POINTER(c_float)]
predict.restype = POINTER(c_float)

if hasGPU:
    set_gpu = lib.cuda_set_device
    set_gpu.argtypes = [c_int]

init_cpu = lib.init_cpu

make_image = lib.make_image
make_image.argtypes = [c_int, c_int, c_int]
make_image.restype = IMAGE

get_network_boxes = lib.get_network_boxes
get_network_boxes.argtypes = [c_void_p, c_int, c_int, c_float, c_float, POINTER(c_int), c_int, POINTER(c_int), c_int]
get_network_boxes.restype = POINTER(DETECTION)

make_network_boxes = lib.make_network_boxes
make_network_boxes.argtypes = [c_void_p]
make_network_boxes.restype = POINTER(DETECTION)

free_detections = lib.free_detections
free_detections.argtypes = [POINTER(DETECTION), c_int]

free_batch_detections = lib.free_batch_detections
free_batch_detections.argtypes = [POINTER(DETNUMPAIR), c_int]

free_ptrs = lib.free_ptrs
free_ptrs.argtypes = [POINTER(c_void_p), c_int]

network_predict = lib.network_predict_ptr
network_predict.argtypes = [c_void_p, POINTER(c_float)]

reset_rnn = lib.reset_rnn
reset_rnn.argtypes = [c_void_p]

load_net = lib.load_network
load_net.argtypes = [c_char_p, c_char_p, c_int]
load_net.restype = c_void_p

load_net_custom = lib.load_network_custom
load_net_custom.argtypes = [c_char_p, c_char_p, c_int, c_int]
load_net_custom.restype = c_void_p

do_nms_obj = lib.do_nms_obj
do_nms_obj.argtypes = [POINTER(DETECTION), c_int, c_int, c_float]

do_nms_sort = lib.do_nms_sort
do_nms_sort.argtypes = [POINTER(DETECTION), c_int, c_int, c_float]

free_image = lib.free_image
free_image.argtypes = [IMAGE]

letterbox_image = lib.letterbox_image
letterbox_image.argtypes = [IMAGE, c_int, c_int]
letterbox_image.restype = IMAGE

load_meta = lib.get_metadata
lib.get_metadata.argtypes = [c_char_p]
lib.get_metadata.restype = METADATA

load_image = lib.load_image_color
load_image.argtypes = [c_char_p, c_int, c_int]
load_image.restype = IMAGE

rgbgr_image = lib.rgbgr_image
rgbgr_image.argtypes = [IMAGE]

predict_image = lib.network_predict_image
predict_image.argtypes = [c_void_p, IMAGE]
predict_image.restype = POINTER(c_float)

predict_image_letterbox = lib.network_predict_image_letterbox
predict_image_letterbox.argtypes = [c_void_p, IMAGE]
predict_image_letterbox.restype = POINTER(c_float)

network_predict_batch = lib.network_predict_batch
network_predict_batch.argtypes = [c_void_p, IMAGE, c_int, c_int, c_int,
                                  c_float, c_float, POINTER(c_int), c_int, c_int]
network_predict_batch.restype = POINTER(DETNUMPAIR)


def array_to_image(arr):
    import numpy as np
    # need to return old values to avoid python freeing memory
    arr = arr.transpose(2, 0, 1)
    c = arr.shape[0]
    h = arr.shape[1]
    w = arr.shape[2]
    arr = np.ascontiguousarray(arr.flat, dtype=np.float32) / 255.0
    data = arr.ctypes.data_as(POINTER(c_float))
    im = IMAGE(w, h, c, data)
    return im, arr


def classify(net, meta, im):
    out = predict_image(net, im)
    res = []
    for i in range(meta.classes):
        if altNames is None:
            nameTag = meta.names[i]
        else:
            nameTag = altNames[i]
        res.append((nameTag, out[i]))
    res = sorted(res, key=lambda x: -x[1])
    return res


def detect(net, meta, image, thresh=.5, hier_thresh=.5, nms=.45, debug=False):
    """
    Performs the meat of the detection
    """
    # pylint: disable= C0321
    im = load_image(image, 0, 0)
    if debug: print("Loaded image")
    ret = detect_image(net, meta, im, thresh, hier_thresh, nms, debug)
    # ret = network_predict_batch(net, im, 4, 608,608, thresh, hier_thresh, None, 0, 0)
    free_image(im)
    if debug: print("freed image")
    return ret


def detect_image(net, meta, im, thresh=.5, hier_thresh=.5, nms=.45, debug=False):
    num = c_int(0)
    if debug: print("Assigned num")
    pnum = pointer(num)
    if debug: print("Assigned pnum")
    predict_image(net, im)
    letter_box = 0
    # predict_image_letterbox(net, im)
    # letter_box = 1
    if debug: print("did prediction")
    # dets = get_network_boxes(net, custom_image_bgr.shape[1], custom_image_bgr.shape[0], thresh, hier_thresh, None, 0, pnum, letter_box) # OpenCV
    dets = get_network_boxes(net, im.w, im.h, thresh, hier_thresh, None, 0, pnum, letter_box)
    if debug: print("Got dets")
    num = pnum[0]
    if debug: print("got zeroth index of pnum")
    if nms:
        do_nms_sort(dets, num, meta.classes, nms)
    if debug: print("did sort")
    res = []
    if debug: print("about to range")
    for j in range(num):
        if debug: print("Ranging on " + str(j) + " of " + str(num))
        if debug: print("Classes: " + str(meta), meta.classes, meta.names)
        for i in range(meta.classes):
            if debug: print("Class-ranging on " + str(i) + " of " + str(meta.classes) + "= " + str(dets[j].prob[i]))
            if dets[j].prob[i] > 0:
                b = dets[j].bbox
                if altNames is None:
                    nameTag = meta.names[i]
                else:
                    nameTag = altNames[i]
                if debug:
                    print("Got bbox", b)
                    print(nameTag)
                    print(dets[j].prob[i])
                    print((b.x, b.y, b.w, b.h))
                res.append((nameTag, dets[j].prob[i], (b.x, b.y, b.w, b.h)))
    res = sorted(res, key=lambda x: -x[1])
    free_detections(dets, num)
    return res


netMain = None
metaMain = None
altNames = None


def performDetect(imagePath="/root/data/VOCdevkit/VOC2007/JPEGImages/0070.jpg",
                  thresh=0.6,
                  configPath=config_path,
                  weightPath=weights_path,
                  metaPath=meta_path,
                  showImage=True,
                  makeImageOnly=False,
                  initOnly=False):
    """
    Convenience function to handle the detection and returns of objects.

    Displaying bounding boxes requires libraries scikit-image and numpy

    Parameters
    ----------------
    imagePath: str
        Path to the image to evaluate. Raises ValueError if not found

    thresh: float (default= 0.25)
        The detection threshold

    configPath: str
        Path to the configuration file. Raises ValueError if not found

    weightPath: str
        Path to the weights file. Raises ValueError if not found

    metaPath: str
        Path to the data file. Raises ValueError if not found

    showImage: bool (default= True)
        Compute (and show) bounding boxes. Changes return.

    makeImageOnly: bool (default= False)
        If showImage is True, this won't actually *show* the image, but will create the array and return it.

    initOnly: bool (default= False)
        Only initialize globals. Don't actually run a prediction.

    Returns
    ----------------------


    When showImage is False, list of tuples like
        ('obj_label', confidence, (bounding_box_x_px, bounding_box_y_px, bounding_box_width_px, bounding_box_height_px))
        The X and Y coordinates are from the center of the bounding box. Subtract half the width or height to get the lower corner.

    Otherwise, a dict with
        {
            "detections": as above
            "image": a numpy array representing an image, compatible with scikit-image
            "caption": an image caption
        }
    """
    # Import the global variables. This lets us instance Darknet once, then just call performDetect() again without
    # instancing again
    global metaMain, netMain, altNames  # pylint: disable=W0603
    assert 0 < thresh < 1, "Threshold should be a float between zero and one (non-inclusive)"
    if not os.path.exists(configPath):
        raise ValueError("Invalid config path `" + os.path.abspath(configPath) + "`")
    if not os.path.exists(weightPath):
        raise ValueError("Invalid weight path `" + os.path.abspath(weightPath) + "`")
    if not os.path.exists(metaPath):
        raise ValueError("Invalid data file path `" + os.path.abspath(metaPath) + "`")
    if netMain is None:
        netMain = load_net_custom(configPath.encode("ascii"), weightPath.encode("ascii"), 0, 1)  # batch size = 1
    if metaMain is None:
        metaMain = load_meta(metaPath.encode("ascii"))
    if altNames is None:
        # In Python 3, the metafile default access craps out on Windows (but not Linux)
        # Read the names file and create a list to feed to detect
        try:
            with open(metaPath) as metaFH:
                metaContents = metaFH.read()
                import re
                match = re.search("names *= *(.*)$", metaContents, re.IGNORECASE | re.MULTILINE)
                if match:
                    result = match.group(1)
                else:
                    result = None
                try:
                    if os.path.exists(result):
                        with open(result) as namesFH:
                            namesList = namesFH.read().strip().split("\n")
                            altNames = [x.strip() for x in namesList]
                except TypeError:
                    pass
        except Exception:
            pass
    if initOnly:
        print("Initialized detector")
        return None
    if not os.path.exists(imagePath):
        raise ValueError("Invalid image path `" + os.path.abspath(imagePath) + "`")
    # Do the detection
    # detections = detect(netMain, metaMain, imagePath, thresh)	# if is used cv2.imread(image)
    detections = detect(netMain, metaMain, imagePath.encode("ascii"), thresh)
    if showImage:
        try:
            image = cv2.imread(imagePath)  # you can transport image(np.array) to here
            image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
            print("*** " + str(len(detections)) + " Results, color coded by confidence ***")
            imcaption = []
            for detection in detections:
                label = detection[0]
                confidence = detection[1]
                pstring = label + ": " + str(np.rint(100 * confidence)) + "%"
                imcaption.append(pstring)
                bounds = detection[2]
                shape = image.shape
                yExtent = int(bounds[3])
                xEntent = int(bounds[2])
                # Coordinates are around the center
                xCoord = int(bounds[0] - bounds[2] / 2)
                yCoord = int(bounds[1] - bounds[3] / 2)
                boundingBox = [
                    [xCoord, yCoord],
                    [xCoord, yCoord + yExtent],
                    [xCoord + xEntent, yCoord + yExtent],
                    [xCoord + xEntent, yCoord]
                ]
                pt1 = (xCoord, yCoord)
                pt2 = (xCoord + xEntent, yCoord + yExtent)
                cv2.rectangle(image, pt1, pt2, (0, 255, 0), 3)
                cv2.putText(image, detection[0].encode('utf-8').decode('utf-8'), (pt1[0] + 5, pt1[1]),
                            cv2.FONT_HERSHEY_SIMPLEX, 1.2, [0, 255, 0], 3)
            detections = {
                "detections": detections,
                "image": image,
                "caption": "\n<br/>".join(imcaption)
            }
        except Exception as e:
            print("Unable to show image: " + str(e))
    return detections


def performBatchDetect(thresh=0.6, configPath=config_path, weightPath=weights_path, metaPath=meta_path, hier_thresh=.5,
                       nms=.45, batch_size=1):
    img_samples = ['data/person.jpg', 'data/person.jpg', 'data/person.jpg']
    image_list = [cv2.imread(k) for k in img_samples]
    net = load_net_custom(configPath.encode('utf-8'), weightPath.encode('utf-8'), 0, batch_size)
    meta = load_meta(metaPath.encode('utf-8'))
    pred_height, pred_width, c = image_list[0].shape
    net_width, net_height = (network_width(net), network_height(net))
    img_list = []
    for custom_image_bgr in image_list:
        custom_image = cv2.cvtColor(custom_image_bgr, cv2.COLOR_BGR2RGB)
        custom_image = cv2.resize(
            custom_image, (net_width, net_height), interpolation=cv2.INTER_NEAREST)
        custom_image = custom_image.transpose(2, 0, 1)
        img_list.append(custom_image)
    arr = np.concatenate(img_list, axis=0)
    arr = np.ascontiguousarray(arr.flat, dtype=np.float32) / 255.0
    data = arr.ctypes.data_as(POINTER(c_float))
    im = IMAGE(net_width, net_height, c, data)
    batch_dets = network_predict_batch(net, im, batch_size, pred_width, pred_height, thresh, hier_thresh, None, 0, 0)
    batch_boxes = []
    batch_scores = []
    batch_classes = []
    for b in range(batch_size):
        num = batch_dets[b].num
        dets = batch_dets[b].dets
        if nms:
            do_nms_obj(dets, num, meta.classes, nms)
        boxes = []
        scores = []
        classes = []
        for i in range(num):
            det = dets[i]
            score = -1
            label = None
            for c in range(det.classes):
                p = det.prob[c]
                if p > score:
                    score = p
                    label = c
            if score > thresh:
                box = det.bbox
                left, top, right, bottom = map(int, (box.x - box.w / 2, box.y - box.h / 2,
                                                     box.x + box.w / 2, box.y + box.h / 2))
                boxes.append((top, left, bottom, right))
                scores.append(score)
                classes.append(label)
                boxColor = (int(255 * (1 - (score ** 2))), int(255 * (score ** 2)), 0)
                cv2.rectangle(image_list[b], (left, top),
                              (right, bottom), boxColor, 2)
        cv2.imwrite(os.path.basename(img_samples[b]), image_list[b])
        batch_boxes.append(boxes)
        batch_scores.append(scores)
        batch_classes.append(classes)
    free_batch_detections(batch_dets, batch_size)
    return batch_boxes, batch_scores, batch_classes


def convertBack(x, y, w, h):
    xmin = int(round(x - (w / 2)))
    xmax = int(round(x + (w / 2)))
    ymin = int(round(y - (h / 2)))
    ymax = int(round(y + (h / 2)))
    return xmin, ymin, xmax, ymax


def compare(str1, str2):
    cnt = 0
    for i in range(len(str1)):
        cnt = cnt + 1 if str1[i] != str2[i] else 0
    return cnt


def cvDrawBoxes(imgView, illegalInfo_list, detections, img, originImg):
    global use_index
    global license2id
    for object in detections:
        kind, confidence = object.type, object.confidence
        confidence = str(confidence)[0:4]
        x, y, w, h = object.coordinate
        xmin, ymin, xmax, ymax = convertBack(float(x), float(y), float(w), float(h))
        pt1 = (xmin, ymin)
        pt2 = (xmax, ymax)
        if kind == 'car':
            if object.license:
                object_license = max(object.license, key=object.license.get)
            else:
                object_license = ''
            if len(object.break_rule) > 0:
                cv2.rectangle(img, pt1, pt2, (0, 69, 255), 2)
                cv2.putText(img, object.type + '  ' + confidence + '  ' + str(object.id), (pt1[0], pt1[1] - 5),
                            cv2.FONT_HERSHEY_SIMPLEX, 0.5, [0, 0, 255], 2)
                if xmin < 0 or ymin < 0 or xmax < 0 or ymax < 0 or object.id == -1:
                    continue
                elif object.break_rule != object.drawed_break_rule and object.id in license2id:
                    index = license2id[object.id]
                    object.drawed_break_rule = object.break_rule
                    info = object_license + ': ' if object_license != '' else ''
                    if object_license not in recordDB:
                        recordDB[object_license] = set()
                    for id in object.break_rule:
                        info = info + illegal_action_list[id] + '、'
                        recordDB[object_license].add(illegal_action_list[id])
                    illegalInfo_list[index].setText(info[:-1])
                elif object.id not in license2id:
                    license2id[object.id] = use_index
                    object.drawed_break_rule = object.break_rule
                    while len(object_show_list) >= 3:
                        object_show_list.pop(0)
                    height, width = originImg.shape[0], originImg.shape[1]
                    show_img = originImg[int(ymin * height / 720):int(ymax * height / 720),
                               int(xmin * width / 1280):int(xmax * width / 1280)]
                    show_img = cv2.cvtColor(show_img, cv2.COLOR_BGR2RGB)
                    show_img = Image.fromarray(np.uint8(show_img)).toqpixmap()
                    imgView.setPixmap(show_img.scaled(350, 150))
                    info = object_license + ': ' if object_license != '' else ''
                    if object_license not in recordDB:
                        recordDB[object_license] = set()
                    for id in object.break_rule:
                        info = info + illegal_action_list[id] + '、'
                        recordDB[object_license].add(illegal_action_list[id])
                    illegalInfo_list[use_index].setText(info[:-1])
                    use_index = (use_index + 1) % 3

            elif object.id != -1:
                cv2.rectangle(img, pt1, pt2, (0, 255, 0), 2)
                cv2.putText(img, object.type + '  ' + confidence + '  ' + str(object.id), (pt1[0], pt1[1] - 5),
                            cv2.FONT_HERSHEY_SIMPLEX, 0.5, [0, 255, 0], 2)
            else:
                cv2.rectangle(img, pt1, pt2, (0, 255, 0), 2)
                cv2.putText(img, object.type + '  ' + confidence, (pt1[0], pt1[1] - 5), cv2.FONT_HERSHEY_SIMPLEX, 0.5,
                            [0, 255, 0], 2)
        else:
            cv2.rectangle(img, pt1, pt2, (255, 191, 0), 2)
            cv2.putText(img, object.type + '  ' + confidence, (pt1[0], pt1[1] - 5), cv2.FONT_HERSHEY_SIMPLEX, 0.5,
                        [255, 191, 0], 2)
    return img


def license_detection(object_detections, img):
    for object in object_detections:
        kind, confidence = object.type, object.confidence
        if kind != 'car' or object.id == -1:
            continue
        x, y, w, h = object.coordinate
        height, width = img.shape[0], img.shape[1]
        x = x * width / 1280
        y = y * height / 720
        w = w * width / 1280
        h = h * height / 720
        xmin, ymin, xmax, ymax = convertBack(float(x), float(y), float(w), float(h))
        if w * h > 15000 and confidence > 0.8:
            pre_img = img[int(ymin):int(ymax), int(xmin):int(xmax)]  # 截取车辆
            if not pre_img.shape[0] or not pre_img.shape[1]:
                continue
            pre_ans = IntelligentTrafficSystem.predict(pre_img)  # 预测车牌
            if pre_ans:
                pstr, confidence = pre_ans
                if confidence < 0.8:
                    continue
                b_str = (pstr.decode('utf-8'))
                if len(b_str) < 7:
                    continue
                if b_str in object.license:
                    object.license[b_str] = object.license.get(b_str) + 1
                else:
                    object.license[b_str] = 1
    return object_detections


def modifyArea(Area_list):
    global widthMul, heightMul
    for area in Area_list:
        for i in range(len(area.points)):
            if area.points[i] != (-1, -1):
                area.points[i] = (int(area.points[i][0] / 1.5), int(area.points[i][1] / 1.5))


def insertImg(ans_label, q):
    while 1:
        image = q.get()
        if image[0]:
            # print('---------------线程退出-----------------')
            break
        # frame1 = QPixmap.loadFromData(image[1])
        frame1 = Image.fromarray(image[1]).toqpixmap()
        ans_label.setPixmap(frame1)


from queue import Queue

q = Queue()


def YOLO(Area_list, ans_label, show_list, video_down_path, ans_img, info_list, illegalInfo_list,
         video_location, video_path="/root/test.mp4"):
    def drawChart():
        info_list[1].clear()
        info_list[3].clear()
        info_list[1].addPlot(title="车流量图", y=carCntBook, pen=pg.mkPen(color='#00eaff', width=2))
        info_list[3].addPlot(title="人流量图", y=peopleCntBook, pen=pg.mkPen(color='#00eaff', width=2))

    print(Area_list)
    for area in Area_list:
        print(area.type, area.points)

    global metaMain, netMain, altNames, ID, use_index, widthMul, heightMul, config_path, weights_path, meta_path
    old_detection = []
    cap = cv2.VideoCapture(video_path)  # open camera or video
    ret, frame_read = cap.read()
    out = cv2.VideoWriter(video_down_path + "/output.mp4", cv2.VideoWriter_fourcc(*"mp4v"),
                          int(cap.get(cv2.CAP_PROP_FPS)), (1280, 720))
    print("Starting the YOLO loop...")
    darknet_image = darknet.make_image(608, 608, 3)  # frame_read.shape[1], frame_read.shape[0]
    need_detection = 0
    # modifyArea(Area_list)
    getRegion(Area_list)
    before_time = time.time()
    start_time = time.time()
    num = 0
    max_fps = 0
    min_fps = 0
    insertProcess = threading.Thread(target=insertImg, args=(ans_label, q))
    insertProcess.setDaemon(True)
    insertProcess.start()

    while ret:
        start_time_in = time.time()
        carCnt = 0
        peopleCnt = 0
        frame_rgb = copy.deepcopy(frame_read)
        frame_read = cv2.resize(frame_read, (1280, 720))
        frame_resized = cv2.resize(frame_rgb, ((608, 608)), interpolation=cv2.INTER_LINEAR)
        # if need_detection % 1 == 0:  # 每k帧预测一次
        darknet.copy_image_from_bytes(darknet_image, frame_resized.tobytes())
        detections = darknet.detect_image(netMain, metaMain, darknet_image, thresh=0.6)
        new_detection = []
        for detection in detections:
            object = Object()
            object.type = detection[0]
            object.confidence = detection[1]
            x, y, w, h = int(detection[2][0] * widthMul), int(detection[2][1] * heightMul), int(
                detection[2][2] * widthMul), int(detection[2][3] * heightMul)
            object.coordinate = (x, y, w, h)
            carCnt = carCnt + 1 if object.type == 'car' else 0
            peopleCnt = peopleCnt + 1 if object.type == 'person' else 0
            new_detection.append(object)
        if need_detection % 25 == 0:
            peopleCntBook.append(peopleCnt)
            carCntBook.append(carCnt)
        old_detection, cnt, ID = trafficStatisticAndTracking(old_detection, new_detection, Area_list, ID)
        if need_detection % 2 == 0:
            all_illegal_detections(old_detection, Area_list, num)
            old_detection = license_detection(old_detection, frame_rgb)
        image = cvDrawBoxes(show_list[use_index], illegalInfo_list, old_detection, frame_read, frame_rgb)
        image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
        q.put((False, image))
        ans_img['ans'] = image
        # frame1 = Image.fromarray(image).toqpixmap()
        # ans_label.setPixmap(frame1)
        # else:
        #     # all_illegal_detections(old_detection, Area_list, num)
        #     # old_detection = license_detection(old_detection, frame_rgb)
        #     image = cvDrawBoxes(show_list[use_index], illegalInfo_list, old_detection, frame_read, frame_rgb)
        #     image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
        #     # out.write(image)
        #     # frame1 = Image.fromarray(image).toqpixmap()
        #     # ans_label.setPixmap(frame1)
        #     q.put((False, image))
        info_list[0].setText(str(carCnt))
        info_list[2].setText(str(peopleCnt))
        if time.time() - before_time > 1:
            drawChart()
            before_time = time.time()
        ret, frame_read = cap.read()
        need_detection += 1
        num = num + 1
        IntelligentTrafficSystem.QApplication.processEvents()
        fps = 1 / (time.time() - start_time_in)
        if fps > max_fps:
            max_fps = fps
        elif (fps < min_fps or min_fps == 0) and num > 50:
            min_fps = fps
    q.put((True, 0))
    print('fps:', num / (time.time() - start_time))
    print('max_fps:', max_fps)
    print('min_fps:', min_fps)
    printRegion(Area_list)                         # 输出各种绘制区域
    insertIllegal(recordDB, video_location, '/')
    recordDB.clear()
    saveFile(Area_list, video_path.split('/')[-1].split('.')[0])
    cap.release()
    out.release()


class MyThread(threading.Thread):
    def __init__(self, func, args):
        super(MyThread, self).__init__()
        self.func = func
        self.args = ""
        if args:
            self.args = args

    def run(self):
        if self.args:
            self.result = self.func(*self.args)
        else:
            self.result = self.func()

    def get_result(self):
        try:
            return self.result
        except Exception:
            return None
