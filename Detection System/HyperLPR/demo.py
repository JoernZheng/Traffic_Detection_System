import time
import tensorflow
from . import HyperLPRLite as pr
import cv2
import numpy as np

tf_config = tensorflow.compat.v1.ConfigProto()
tf_config.gpu_options.allow_growth = True   # 自适应
session = tensorflow.compat.v1.Session(config=tf_config)

def SpeedTest(image_path):
    grr = cv2.imread(image_path)
    model = pr.LPR("/root/PycharmProjects/yolo/HyperLPR/model/cascade.xml", "/root/PycharmProjects/yolo/HyperLPR/model/model12.h5", "/root/PycharmProjects/yolo/HyperLPR/model/ocr_plate_all_gru.h5")
    model.SimpleRecognizePlateByE2E(grr)
    t0 = time.time()
    for x in range(20):
        model.SimpleRecognizePlateByE2E(grr)
    t = (time.time() - t0)/20.0
    print ("Image size :" + str(grr.shape[1])+"x"+str(grr.shape[0]) +  " need " + str(round(t*1000,2))+"ms")

    

from PIL import ImageFont
from PIL import Image
from PIL import ImageDraw
fontC = ImageFont.truetype("/root/PycharmProjects/yolo/HyperLPR/Font/platech.ttf", 14, 0)

def drawRectBox(image,rect,addText):
    cv2.rectangle(image, (int(rect[0]), int(rect[1])), (int(rect[0] + rect[2]), int(rect[1] + rect[3])), (0,0, 255), 2,cv2.LINE_AA)
    cv2.rectangle(image, (int(rect[0]-1), int(rect[1])-16), (int(rect[0] + 115), int(rect[1])), (0, 0, 255), -1,
                  cv2.LINE_AA)
    img = Image.fromarray(image)
    draw = ImageDraw.Draw(img)
    draw.text((int(rect[0]+1), int(rect[1]-16)), addText.encode("utf-8").decode("utf-8"), (255, 255, 255), font=fontC)
    imagex = np.array(img)
    return imagex

def predict(img_path):
    grr = cv2.imread("/root/darknet/demo1.png")
    print('------------------------------', grr)
    model = pr.LPR("model/cascade.xml", "model/model12.h5", "model/ocr_plate_all_gru.h5")
    for pstr, confidence, rect in model.SimpleRecognizePlateByE2E(grr):
        if confidence > 0.7:
            image = drawRectBox(grr, rect, pstr + " " + str(round(confidence, 3)))
            print("plate_str:")
            b_str = (pstr.encode('utf-8'))
            print(b_str)
            print("plate_confidence")
            print(confidence)

    cv2.imshow("image", image)
    cv2.waitKey(0)


if __name__ == '__main__':
    # grr = cv2.imread("/root/darknet/demo1.png")
    # print('------------------------------', grr)
    # #model = pr.LPR("model/cascade.xml", "model/model12.h5", "model/ocr_plate_all_gru.h5")
    # model = pr.LPR()
    # for pstr, confidence, rect in model.SimpleRecognizePlateByE2E(grr):
    #     if confidence>0.7:
    #         image = drawRectBox(grr, rect, pstr+" "+str(round(confidence, 3)))
    #         print("plate_str:")
    #         b_str = (pstr.encode('utf-8'))
    #         print(b_str)
    #         print("plate_confidence")
    #         print(confidence)
    #
    # cv2.imshow("image", image)
    # cv2.waitKey(0)



    SpeedTest("/root/HyperLPR/images_rec/2.jpg")
