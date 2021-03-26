import sys
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from copy import deepcopy
from main_module.window_module.Zoning_win import Ui_Form
from main_module.window_module.wait_time_win import Wait
from main_module.window_module.speed import Speed
from main_module.window_module.direction import Direction
from main_module.window_module.ReDirection import ReDirection
from main_module.Area import Area


class Drawing(QWidget, Ui_Form):
    my_Signal = pyqtSignal(bool)
    def __init__(self, parent=None):
        super(Drawing, self).__init__(parent)
        self.resize(600, 400)
        self.setWindowTitle('区域划定')
        self.setupUi(self)
        self.img_h = 0
        self.img_w = 0
        self.Areas = []
        self.sum_area = []                  # 车数统计       type = 0
        self.press_line = []                # 压线          type = 1
        self.break_rule_area = []           # 违规停车       type = 2
        self.car_road = []                  # 违规车道转向   type = 3
        self.reDirection_area = []          # 逆向行驶       type = 4
        self.speed_area = []                # 车速计算       type = 5
        self.detect_video = False
        self.point_list = []
        self.qp = QPainter()
        self.pen = QPen(Qt.green, 3, Qt.SolidLine)
        self.setCursor(Qt.CrossCursor)
        self.setMouseTracking(True)
        qr = self.frameGeometry()                   # set center
        cp = QDesktopWidget().availableGeometry().center()
        qr.moveCenter(cp)
        self.move(qr.topLeft())
        self.setWindowFlag(Qt.FramelessWindowHint)  # 取消边框
        QShortcut("m", self, self.maxsize)          # 切换窗口大小
        QShortcut("1", self, self.tab1)             # 切换划定车数统计      green
        QShortcut("2", self, self.tab2)             # 切换划定违规区域      red
        QShortcut("3", self, self.tab3)             # 切换划定车速计算      yellow
        QShortcut("4", self, self.tab4)             # 切换划定压道线        black
        QShortcut("5", self, self.tab5)             # 切换划定车道方向区域   gray
        QShortcut("6", self, self.tab6)             # 切换划定逆向区域       blue
        QShortcut("z", self, self.undo)             # 撤销
        QShortcut("c", self, self.clear)            # 清空
        QShortcut("e", self, self.exit)             # 退出
        # 重写绘制函数
    def paintEvent(self, event):
        # 开始在窗口绘制
        self.qp.begin(self)
        self.qp.setRenderHint(QPainter.Antialiasing)
        # 自定义画点方法
        if self:
            self.drawPoint()
        # 结束在窗口的绘制
        self.qp.end()

    def mousePressEvent(self, event):

        print(event.x(), event.y())
        self.point_list.append((event.x(), event.y()))
        self.update()

        if self.pen.color() == Qt.black and len(self.point_list) == 2:
            reply = QMessageBox.question(self, '提示', '确认选择区域？', QMessageBox.Yes, QMessageBox.Cancel)
            if reply == QMessageBox.Yes:
                for point in self.point_list:
                    self.press_line.append(deepcopy(point))
                self.press_line.append((-1, -1))
                self.point_list.clear()
                self.update()

        elif len(self.point_list) > 1 and abs(self.point_list[0][0] - event.x()) < 5 and abs(self.point_list[0][1] - event.y()) < 5:
            reply = QMessageBox.question(self, '提示', '确认选择区域？', QMessageBox.Yes, QMessageBox.Cancel)
            if reply == QMessageBox.Yes:

                if self.pen.color() == Qt.red:     # 弹窗要求输入违停时间
                    # 弹窗
                    self.wait_time = Wait()
                    self.wait_time.show()
                    for position in self.point_list:
                        self.break_rule_area.append(deepcopy(position))
                    self.break_rule_area.append((-1, -1))

                elif self.pen.color() == Qt.yellow:  # 弹窗要求输入车速计算区域
                    # 弹窗
                    self.speed = Speed()
                    self.speed.show()
                    for position in self.point_list:
                        self.speed_area.append(deepcopy(position))
                    self.speed_area.append((-1, -1))

                elif self.pen.color() == Qt.gray:    # 弹窗要求输入车道方向区域
                    # 弹窗
                    self.direction = Direction()
                    self.direction.show()
                    for position in self.point_list:
                        self.car_road.append(deepcopy(position))
                    self.car_road.append((-1, -1))

                elif self.pen.color() == Qt.green:   # 确定统计区域
                    for position in self.point_list:
                        self.sum_area.append(deepcopy(position))
                    self.sum_area.append((-1, -1))

                elif self.pen.color() == Qt.black:   # 确定压线区域
                    for position in self.point_list:
                        self.press_line.append(deepcopy(position))
                    self.sum_area.append((-1, -1))

                elif self.pen.color() == Qt.blue:   # 确定逆向区域
                    self.reDirection = ReDirection()
                    self.reDirection.show()
                    for position in self.point_list:
                        self.reDirection_area.append(deepcopy(position))
                    self.reDirection_area.append((-1, -1))

                self.point_list.clear()
                self.update()

    def drawLine(self, area):
        index = 0
        base = 0
        for point in area:
            if point != (-1, -1):
                self.qp.drawPoint(*point)
                if index >= 1:
                    self.qp.drawLine(area[base + index - 1][0], area[base + index - 1][1], area[base + index][0], area[base + index][1])
                index += 1
            else:
                base = base + index + 1
                index = 0

    def drawPoint(self):
        if self.sum_area:
            pen = QPen(Qt.green, 3, Qt.SolidLine)
            self.qp.setPen(pen)
            self.drawLine(self.sum_area)

        if self.break_rule_area:
            pen = QPen(Qt.red, 3, Qt.SolidLine)
            self.qp.setPen(pen)
            self.drawLine(self.break_rule_area)

        if self.speed_area:
            pen = QPen(Qt.yellow, 3, Qt.SolidLine)
            self.qp.setPen(pen)
            self.drawLine(self.speed_area)

        if self.press_line:
            pen = QPen(Qt.black, 3, Qt.SolidLine)
            self.qp.setPen(pen)
            self.drawLine(self.press_line)

        if self.car_road:
            pen = QPen(Qt.gray, 3, Qt.SolidLine)
            self.qp.setPen(pen)
            self.drawLine(self.car_road)

        if self.reDirection_area:
            pen = QPen(Qt.blue, 3, Qt.SolidLine)
            self.qp.setPen(pen)
            self.drawLine(self.reDirection_area)

        self.qp.setPen(self.pen)
        if self.point_list:
            for index, point in enumerate(self.point_list):
                self.qp.drawPoint(*point)
                if index >= 1:
                    self.qp.drawLine(self.point_list[index - 1][0], self.point_list[index - 1][1], self.point_list[index][0], self.point_list[index][1])

    def undo(self):
        if len(self.point_list):
            self.point_list.pop()
            self.update()

    def clear(self):
        self.point_list = []
        self.break_rule_area = []
        self.sum_area = []
        self.speed_area = []
        self.car_road = []
        self.press_line = []
        self.reDirection_area = []
        self.update()

    def maxsize(self):
        if self.windowState() == Qt.WindowNoState:
            self.showMaximized()
        else:
            self.showNormal()

    def tab1(self):
        self.pen = QPen(Qt.green, 3, Qt.SolidLine)
        self.qp.setPen(self.pen)

    def tab2(self):
        self.pen = QPen(Qt.red, 3, Qt.SolidLine)
        self.qp.setPen(self.pen)

    def tab3(self):
        self.pen = QPen(Qt.yellow, 3, Qt.SolidLine)
        self.qp.setPen(self.pen)

    def tab4(self):
        self.pen = QPen(Qt.black, 3, Qt.SolidLine)
        self.qp.setPen(self.pen)

    def tab5(self):
        self.pen = QPen(Qt.gray, 3, Qt.SolidLine)
        self.qp.setPen(self.pen)

    def tab6(self):
        self.pen = QPen(Qt.blue, 3, Qt.SolidLine)
        self.qp.setPen(self.pen)

    @pyqtSlot()
    def exit(self):
        area = Area(self.img_w, self.img_h)

        if self.sum_area:
            area = Area(self.img_w, self.img_h)
            area.points = self.sum_area
            area.type = 0
            self.Areas[0] = deepcopy(area)

        if self.press_line:
            area = Area(self.img_w, self.img_h)
            area.points = self.press_line
            area.type = 1
            self.Areas[1] = deepcopy(area)

        if self.break_rule_area:
            area = Area(self.img_w, self.img_h)
            area.points = self.break_rule_area
            area.type = 2
            area.parking_threshold_time = eval(self.wait_time.set_time)
            self.Areas[2] = deepcopy(area)

        if self.car_road:
            area = Area(self.img_w, self.img_h)
            area.points = self.car_road
            area.type = 3
            if self.direction.item_list.currentText() == '左转车道':
                area.turn.append('left')
            elif self.direction.item_list.currentText() == '右转车道':
                area.turn.append('right')
            elif self.direction.item_list.currentText() == '直行车道':
                area.turn.append('straight')
            elif self.direction.item_list.currentText() == '左转或直行车道':
                area.turn.append('straight')
                area.turn.append('left')
            elif self.direction.item_list.currentText() == '右转或直行车道':
                area.turn.append('straight')
                area.turn.append('right')
            self.Areas[3] = deepcopy(area)

        if self.reDirection_area:
            area = Area(self.img_w, self.img_h)
            area.points = self.reDirection_area
            area.type = 4
            if self.reDirection.radioButton.isChecked():
                area.direction = 'T2B'
            else:
                area.direction = 'B2T'
            self.Areas[4] = deepcopy(area)

        if self.speed_area:
            area = Area(self.img_w, self.img_h)
            area.points = self.speed_area
            area.maxSpeed = eval(self.speed.speed_text.text())
            area.roadLength = eval(self.speed.area_len.text())
            area.type = 5
            self.Areas[5] = deepcopy(area)
        self.close()
        self.detect_video = True
        self.my_Signal.emit(self.detect_video)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    demo = Drawing()
    palette = QPalette()
    palette.setBrush(QPalette.Background, QBrush(QPixmap(r"C:\Users\镇长\Pictures\Saved Pictures\02.jpg")))
    demo.setPalette(palette)
    demo.show()
    sys.exit(app.exec_())

