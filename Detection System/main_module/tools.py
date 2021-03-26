import math
import os
import time
import numpy as np
from PIL import Image
from main_module.Object import Object

illegal_action_list = ['None', '压线', '违停', '不合法方向', '逆向行驶', '超速']


def getXYWH(object):
    return int(object.coordinate[0]), int(object.coordinate[1]), int(object.coordinate[2]), int(object.coordinate[3])


def get_boundary_of_this_area(area):
    """
    :param area:area
    :return: xmin, xmax, ymin, ymax
    """
    if area.type == 3 and len(area.points) != 0:
        xs = []
        ys = []
        for point in area.points:
            if point == (-1, -1):
                break
            xs.append(point[0])
            ys.append(point[1])
        xs.sort()
        ys.sort()
        area.turn_boundary = [xs[0], xs[-1], ys[0], ys[-1]]


def getNewObjects(detections):
    objects = []
    for detection in detections:
        object = Object()
        object.type = str(detection[0])
        object.coordinate = detection[2]
        objects.append(object)
    return objects


def euclideanDistance(x1, x2, y1, y2):  # 欧氏距离
    return math.sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)


def sizeRatio(new_object, old_object):
    """
    新旧检测面积比值
    """
    nx, ny, nw, nh = getXYWH(new_object)
    ox, oy, ow, oh = getXYWH(old_object)
    sn = nw * nh
    so = ow * oh
    return sn / so


def getWidthAndHeightRatio(car):
    """
    :return:宽高比
    """
    x, y, w, h = getXYWH(car)
    return w / h


def isTurn(car):
    if getWidthAndHeightRatio(car) / car.turn_init_ratio > 1.5:
        return True
    else:
        return False


def lineRegion(point1, point2, area):
    """
    point = (x,y)
    """
    x1 = int(float(point1[0]))
    y1 = int(float(point1[1]))
    x2 = int(float(point2[0]))
    y2 = int(float(point2[1]))

    if x1 == x2:  # 避免斜率为0和无穷大
        x2 += 1
    if y1 == y2:
        y2 += 1
    try:
        if abs(x1 - x2) > abs(y1 - y2):
            if x1 > x2:
                x1, y1, x2, y2 = x2, y2, x1, y1
            x = x1
            k = (y2 - y1) / (x2 - x1)
            while x <= x2:
                y = int(y1 + k * (x - x1))
                area.region[y][x] = True
                x += 1
        else:
            if y1 > y2:
                x1, y1, x2, y2 = x2, y2, x1, y1
            y = y1
            m = (x2 - x1) / (y2 - y1)
            while y <= y2:
                x = int(x1 + m * (y - y1))
                area.region[y][x] = True
                y += 1
    except Exception as e:
        print('x:', x)
        print('y:', y)
    # return area


def getLinedRegion(areas):
    for area in areas:
        point_count = len(area.points)
        if area.type == 1:
            for i in range(point_count):
                if i % 3 == 0:
                    point1 = area.points[i]
                    point2 = area.points[i + 1]
                    lineRegion(point1, point2, area)
        else:
            first_flag = 0
            for i in range(point_count):
                if area.points[i] == (-1, -1):
                    continue
                elif area.points[i + 1] == (-1, -1):
                    point1 = area.points[i]
                    point2 = area.points[first_flag]
                    lineRegion(point1, point2, area)
                    first_flag = i + 2
                else:
                    point1 = area.points[i]
                    point2 = area.points[i + 1]
                    lineRegion(point1, point2, area)
    # return areas


def getRegion(areas):  # 凸多边形
    start_time = time.time()
    getLinedRegion(areas)
    for area in areas:
        get_boundary_of_this_area(area)
        if area.type == 1:  # 对于压线区域，有线条即可
            continue
        x = len(area.region)  # x=1080才能实现横向扫描，这个和常规的坐标系有所不同
        y = len(area.region[0])
        for i in range(x):  # x的长度
            start = 0
            end = 0
            for j in range(y):  # y的长度
                if area.region[i][j] and start == 0:
                    start = j
                elif area.region[i][j - 1] and area.region[i][j]:
                    continue
                elif not area.region[i][j - 1] and area.region[i][j] and start != 0:
                    end = j
            while start < end:
                start += 1
                area.region[i][start] = True
    print('whole time:', time.time() - start_time)
    # return areas


def inArea(object, area, type):
    """
    存在一个感兴趣区域像素数组，region = w×h×(感兴趣类别)
    area.region[w][h] = [0,0,0,0,...0]
    存在问题：没有将同一类型的区域区分开
    """
    if area.type != type:  # 不是想要检测的类型，直接跳过
        return False
    x = int(object.coordinate[1])  # 形状是[1080,1920]
    y = int(object.coordinate[0])
    try:
        return area.region[x][y]
    except Exception as e:
        print(e)
        return False


def fuseNewAndOld(old, new):
    """
    将新旧目标的信息融合
    """
    new.id = old.id
    new.license = old.license
    new.lost_count = 0
    new.break_rule = old.break_rule
    new.parking_start_time = old.parking_start_time
    new.speed_detection_start_time = old.speed_detection_start_time
    new.retrograde_detection = old.retrograde_detection
    new.speeding_detection_coordinates = old.speeding_detection_coordinates
    new.in_retrograde_detection_area = old.in_retrograde_detection_area
    new.in_illegal_parking_area = old.in_illegal_parking_area
    new.in_speeding_detection_area = old.in_speeding_detection_area


def printRegion(areas):
    for area in areas:
        pic = np.zeros((720, 1280), dtype=np.int8)
        for i in range(720):
            for j in range(1280):
                if area.region[i][j]:
                    pic[i][j] = 255
        if not os.path.exists('visualize_regions'):
            os.mkdir('visualize_regions')
        Image.fromarray(pic, mode='L').save('visualize_regions/type_{}.jpg'.format(str(area.type)))
