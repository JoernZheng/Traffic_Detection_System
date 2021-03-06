from ctypes import *
import math
import random
import os
import cv2
import numpy as np
import time
import darknet


def convertBack(x, y, w, h):
    xmin = int(round(x - (w / 2)))
    xmax = int(round(x + (w / 2)))
    ymin = int(round(y - (h / 2)))
    ymax = int(round(y + (h / 2)))
    return xmin, ymin, xmax, ymax


def cvDrawBoxes(detections, img):
    for detection in detections:
        # print(detection)
        x, y, w, h = detection[2][0], \
                     detection[2][1], \
                     detection[2][2], \
                     detection[2][3]
        xmin, ymin, xmax, ymax = convertBack(
            float(x), float(y), float(w), float(h))
        pt1 = (xmin, ymin)
        pt2 = (xmax, ymax)
        cv2.rectangle(img, pt1, pt2, (0, 255, 0), 1)
        cv2.putText(img,
                    detection[0] +
                    " [" + str(round(detection[1] * 100, 2)) + "]",
                    (pt1[0], pt1[1] - 5), cv2.FONT_HERSHEY_SIMPLEX, 0.5,
                    [0, 255, 0], 2)
    return img


netMain = None
metaMain = None
altNames = None


# configPath = "./cfg/yolov4-voc_car.cfg", weightPath = "/home/train_weight/yolov4-voc_car_6000.weights", metaPath= "./cfg/voc.data",

def YOLO(video_path="/root/test200.avi"):
    global metaMain, netMain, altNames
    configPath = "./cfg/yolov4-voc_car.cfg"
    weightPath = "/home/train_weight/yolov4-voc_car_6000.weights"
    metaPath = "./cfg/voc.data"
    if not os.path.exists(configPath):
        raise ValueError("Invalid config path `" +
                         os.path.abspath(configPath) + "`")
    if not os.path.exists(weightPath):
        raise ValueError("Invalid weight path `" +
                         os.path.abspath(weightPath) + "`")
    if not os.path.exists(metaPath):
        raise ValueError("Invalid data file path `" +
                         os.path.abspath(metaPath) + "`")
    if netMain is None:
        netMain = darknet.load_net_custom(configPath.encode(
            "ascii"), weightPath.encode("ascii"), 0, 1)  # batch size = 1
    if metaMain is None:
        metaMain = darknet.load_meta(metaPath.encode("ascii"))
    if altNames is None:
        try:
            with open(metaPath) as metaFH:
                metaContents = metaFH.read()
                import re
                match = re.search("names *= *(.*)$", metaContents,
                                  re.IGNORECASE | re.MULTILINE)
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
    # cap = cv2.VideoCapture(0)    # open camera
    cap = cv2.VideoCapture(video_path)
    # cap.set(3, 1280)
    # cap.set(4, 720)
    # out = cv2.VideoWriter(
    #     "output.avi", cv2.VideoWriter_fourcc(*"mp4v"),int(cap.get(cv2.CAP_PROP_FPS)),
    #     (darknet.network_width(netMain),darknet.network_height(netMain)))
    # print("Starting the YOLO loop...")

    # Create an image we reuse for each detect
    darknet_image = darknet.make_image(darknet.network_width(netMain),
                                       # the darknet_image is a struct, it contains w,h,c,data; c is the number of image channels
                                       darknet.network_height(netMain), 3)
    f = open('./detection_200.txt', 'w+')
    ret, frame_read = cap.read()
    while ret:
        frame_rgb = cv2.cvtColor(frame_read, cv2.COLOR_BGR2RGB)
        frame_resized = cv2.resize(frame_rgb,  # (darknet.network_width(netMain),darknet.network_height(netMain))
                                   (darknet.network_width(netMain),
                                    darknet.network_height(netMain)),
                                   interpolation=cv2.INTER_LINEAR)
        darknet.copy_image_from_bytes(darknet_image, frame_resized.tobytes())
        detections = darknet.detect_image(netMain, metaMain, darknet_image, thresh=0.6)  # kaung de wei zhi zuo biao
        # print(frame_resized.shape)
        # for detection in detections:
        f.writelines(str(detections) + '\n')

        # frame_resized = cv2.cvtColor(frame_resized, cv2.COLOR_BGR2RGB)
        # #cv2.imshow('demo',frame_resized)    #xian shi qian jing tu
        # #print(frame_resized)
        # image = cvDrawBoxes(detections, frame_resized)
        # cv2.imshow('Demo', image)
        # cv2.imshow('demo', frame_rgb)
        # # out.write(image)
        # cv2.waitKey(1)
        ret, frame_read = cap.read()
    cap.release()
    f.close()
    # out.release()


if __name__ == "__main__":
    YOLO()
