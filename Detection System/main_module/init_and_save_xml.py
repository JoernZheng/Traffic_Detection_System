import os
import time
import xml.etree.ElementTree as ET

from main_module.Area import Area
from main_module.tools import printRegion, illegal_action_list


def existInitFile(file_path):
    if not os.path.exists('cache/areas/'):
        os.makedirs(file_path)
    if not os.path.exists(file_path):
        return False
    else:
        return True


def init_areas(w, h, video_name):
    """
    w: width of the video
    h: height of the video
    file_path: path of areas.xml, for example, file_path = cache/
    """
    init_start_time = time.time()
    file_path = 'cache/areas/' + video_name + '.xml'
    print('file_path:', file_path)
    areas = []
    if existInitFile(file_path):
        # print('提示：存在初始化文件，进行自动初始化。')
        print('Exist xml file, you can use it for auto initiation.')
        root = ET.parse(file_path).getroot()
        all_areas = root.findall('area')
        w = int(float(all_areas[0].find('width').text))
        h = int(float(all_areas[0].find('height').text))
        for xml_area in all_areas:
            area = Area(w, h)
            area.type = int(float(xml_area.find('type').text))
            points = xml_area.find('points').text[2:-2].split('), (')
            for point in points:
                if point == '':
                    continue
                number1, number2 = point.split(', ')
                number1 = int(float(number1))
                number2 = int(float(number2))
                area.points.append((number1, number2))
            regions = xml_area.find('regions')
            all_region = regions.findall('region')
            for i in range(len(all_region)):
                this_region = all_region[i].text.split(', ')
                for j in range(len(this_region)):
                    if this_region[j] == 'True':
                        area.region[i][j] = True
            area.turn = xml_area.find('turn').text[2:-2].split('\', \'')
            area.direction = xml_area.find('direction').text
            if area.type == 3 and len(area.points) != 0:
                boundary_text = xml_area.find('turn_boundary').text[1:-1].split(', ')
                area.turn_boundary = [float(i) for i in boundary_text]
            else:
                area.turn_boundary = []
            area.parking_threshold_time = float(xml_area.find('parking_threshold_time').text)
            area.maxSpeed = float(xml_area.find('maxSpeed').text)
            area.roadLength = float(xml_area.find('roadLength').text)
            areas.append(area)
    else:
        # print('提示：没有初始化文件，需要手动进行检测区域绘制。')
        print('This video has no xml file, so you need to draw areas by yourself.')
        for i in range(len(illegal_action_list)):
            area = Area(w, h)
            area.type = i
            areas.append(area)

    printRegion(areas)
    print('init time:', time.time() - init_start_time)
    return areas


def subElement(root, tag, text):
    ele = ET.SubElement(root, tag)
    if text != '':
        ele.text = text
        ele.tail = '\n'
    return ele


def modifyBackArea(areas):
    for area in areas:
        for i in range(len(area.points)):
            if area.points[i] != (-1, -1):
                area.points[i] = (int(area.points[i][0] * 1.5), int(area.points[i][1] * 1.5))


def saveFile(areas: object, video_name):

    root = ET.Element('areas')
    for area in areas:
        this_area = subElement(root, 'area', '')
        w = len(area.region[1])
        h = len(area.region)
        subElement(this_area, 'type', str(area.type))
        subElement(this_area, 'points', str(area.points))
        regions = subElement(this_area, 'regions', '')
        for i in range(h):
            subElement(regions, 'region', str(area.region[i]))
        subElement(this_area, 'turn', str(area.turn))
        subElement(this_area, 'direction', str(area.direction))
        subElement(this_area, 'turn_boundary', str(area.turn_boundary))
        subElement(this_area, 'parking_threshold_time', str(area.parking_threshold_time))
        subElement(this_area, 'width', str(w))
        subElement(this_area, 'height', str(h))
        subElement(this_area, 'maxSpeed', str(area.maxSpeed))
        subElement(this_area, 'roadLength', str(area.roadLength))
    tree = ET.ElementTree(root)
    tree.write('cache/areas/{}.xml'.format(video_name))
