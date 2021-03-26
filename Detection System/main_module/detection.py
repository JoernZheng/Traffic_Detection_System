import threading
from main_module.tools import *


def trafficStatisticAndTracking(old_objects, new_objects, areas, ID):
    # 先进行初次整理，将所有的行人都筛选掉
    sorted_objects = []
    for i in range(len(new_objects) - 1, -1, -1):
        if new_objects[i].type != 'car' and new_objects[i].type != 'bus' and new_objects[i].type != 'truck':
            sorted_objects.append(new_objects[i])
            new_objects.remove(new_objects[i])
    for i in range(len(old_objects) - 1, -1, -1):  # 旧的非车是不需要的对象
        if old_objects[i].type != 'car' and old_objects[i].type != 'bus' and old_objects[i].type != 'truck':
            old_objects.remove(old_objects[i])

    # 开始跟踪
    for old in old_objects:
        if old.id == -1:  # 不需要统计和跟踪的对象
            continue
        find = False
        threshold = old.coordinate[3] if old.coordinate[2] > old.coordinate[3] else old.coordinate[2]
        for new in new_objects:
            if euclideanDistance(old.coordinate[0], new.coordinate[0],
                                 old.coordinate[1], new.coordinate[1]) < threshold and 0.8 < sizeRatio(new, old) < 1.2:
                find = True
                fuseNewAndOld(old, new)  # 将新车和旧车的参数融合，例如违章记录、车牌信息等
                sorted_objects.append(new)
                new_objects.remove(new)
                break
        if not find:
            if old.lost_count < 5:  # 最多5次机会没被匹配到, 后期可以调整到1s对应的数字
                old.lost_count += 1
                sorted_objects.append(old)
            else:
                illegal_list = [illegal_action_list[i] for i in old.break_rule]
                # print("{}:{},{}".format(str(old.id), str(illegal_list), str(old.license)))

    # 开始计数
    new_car_count = 0
    if len(new_objects) > 0:
        for new in new_objects:
            for area in areas:
                if inArea(new, area, 0):
                    ID += 1
                    new.id = ID
                    sorted_objects.append(new)
                    new_car_count += 1
                else:
                    sorted_objects.append(new)

    return sorted_objects, new_car_count, ID


def pressLine(objects, areas):
    """
    压线检测
    压线的规则一般指的是两侧的车道线，一般不将停车线纳入考虑范围内
    轻微压线没有问题，但是较大压线存在问题
    压线只需要标记实线的边缘即可
    """
    for object in objects:
        if object.id == -1:  # 不是需要跟踪的对象
            continue
        if 1 not in object.break_rule:
            x, y, w, h = getXYWH(object)
            min_distance = -1
            for region_x in range(len(areas[1].region[y])):
                if areas[1].region[y][region_x]:
                    if min_distance == -1:
                        min_distance = abs(region_x - x)
                    else:
                        min_distance = abs(region_x - x) if abs(region_x - x) < min_distance else min_distance
            if min_distance != -1:
                if min_distance < 3 / 8 * w:
                    object.break_rule.append(1)


def illegalParking(objects, areas):
    """
    违规停车检测
    违停检测需要改进的地方：检测区单独判断及相似性检测
    具体步骤：
    1.在违停区中的车辆
    2.相似性检测配合计时功能
    3.得出违章结论
    """
    for object in objects:
        if object.id == -1:  # 不是需要跟踪的对象
            continue
        if 2 not in object.break_rule:
            flag = False  # 排除多个区域的干扰，只要存在于任何一个区域中，就变为True
            for area in areas:
                if inArea(object, area, 2):
                    if not object.in_illegal_parking_area:  # 第一次进入这片检测区域
                        object.parking_start_time = time.time()
                        object.in_illegal_parking_area = True
                    else:
                        if time.time() - object.parking_start_time > area.parking_threshold_time:
                            object.break_rule.append(2)
                            break
                    flag = True
                    print(time.time() - object.parking_start_time)
            if not flag:
                object.in_illegal_parking_area = False
    # return objects


def illegalTurn(objects, areas):
    """
    不合法方向行驶检测
    """
    for object in objects:
        if object.id == -1:  # 不是需要跟踪的对象
            continue
        if 3 not in object.break_rule:
            x, y, w, h = getXYWH(object)
            for area in areas:
                if inArea(object, area, 3):
                    if object.turn_init_ratio == -1:
                        object.turn_init_ratio = getWidthAndHeightRatio(object)
                    if y > area.turn_boundary[0] and not isTurn(object) and 'straight' not in area.turn:
                        print('straight')
                        object.break_rule.append(3)
                        break
                    elif x < area.turn_boundary[2] and isTurn(object) and 'left' not in area.turn:
                        print('left')
                        object.break_rule.append(3)
                        break
                    elif x > area.turn_boundary[3] and isTurn(object) and 'right' not in area.turn:
                        print('right')
                        object.break_rule.append(3)
                        break


def retrograde(objects, areas):
    """
    逆行检测，定时1S检测一次即可
    """
    for object in objects:  # 每一辆车
        if object.id == -1:  # 不是需要跟踪的对象
            continue
        if 4 not in object.break_rule:  # 如果车已经被判定为逆行，则直接结束
            y = object.coordinate[1]
            h = object.coordinate[3]
            flag = False
            for area in areas:
                if inArea(object, area, 4):
                    if not object.in_retrograde_detection_area:
                        object.retrograde_detection = []
                        object.in_retrograde_detection_area = True
                    object.retrograde_detection.append(y)
                    if len(object.retrograde_detection) < 2:
                        distance = y - object.retrograde_detection[0]
                    else:
                        distance = y - object.retrograde_detection[-2]
                    if distance > 1 and area.direction == 'B2T' or distance < -1 and area.direction == 'T2B':
                        object.break_rule.append(4)
                        break
                    flag = True  # 说明该车存在于至少一个逆行检测区中
            if not flag:
                object.in_retrograde_detection_area = False
    # return objects


def speeding(objects, areas):
    """
    max_speed:最高车速，单位KM/h
    road_length:检测区道路实际长度，单位M
    应当在间隔0.5S左右计算平均速度
    暂时只有最简单的方法：区域加时间，且只有一个超速测定区
    avg_speed = road_length / (time.time() - start_time) * 3.6
    """
    for object in objects:
        if object.id == -1:  # 不是需要跟踪的对象
            continue
        if 5 not in object.break_rule:
            x = object.coordinate[0]
            y = object.coordinate[1]
            for area in areas:
                if inArea(object, area, 5):
                    if not object.in_speeding_detection_area:  # 首次进入检测区域
                        object.speeding_detection_coordinates = []
                        object.in_speeding_detection_area = True
                        object.speed_detection_start_time = time.time()
                elif object.in_speeding_detection_area:  # 刚驶出检测区域
                    avg_speed = area.roadLength / (time.time() - object.speed_detection_start_time) * 3.6
                    if avg_speed > area.maxSpeed:
                        object.break_rule.append(5)
                        break
    #                 object.in_speeding_detection_area = False
    #             else:
    #                 object.in_speeding_detection_area = False
    # return objects


def all_illegal_detections(objects, areas, frame):
    if frame % 4 == 0:
        pressLine(objects, areas)
        illegalParking(objects, areas)
    elif frame % 4 == 2:
        illegalTurn(objects, areas)
        retrograde(objects, areas)
        speeding(objects, areas)
