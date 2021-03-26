import sys
import time

from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from mainUI.mainUI2 import Ui_MainWindow

class CameraPageWindow(QMainWindow, Ui_MainWindow):
    def __init__(self, parent=None):
        super(CameraPageWindow, self).__init__(parent)
        self.setupUi(self)
        op = QGraphicsOpacityEffect()
        op.setOpacity(0.3)
        self.illegalInfo1.setGraphicsEffect(op)
        self.illegalInfo1.setAutoFillBackground(True)
        # self.illegalInfo1.setOpacity(0.5)

if __name__ == '__main__':
    app = QApplication(sys.argv)
    camer = CameraPageWindow()
    camer.show()
    time.sleep(4)
    app.processEvents()
    sys.exit(app.exec())  # 应用退出