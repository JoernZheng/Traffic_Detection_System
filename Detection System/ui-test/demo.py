import sys
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from main_module.window_module.road_direction import Ui_Form


class Direction(QWidget, Ui_Form):
    my_Signal1 = pyqtSignal(str)
    def __init__(self, parent=None):
        super(Direction, self).__init__(parent)
        self.setupUi(self)
        qr = self.frameGeometry()                   # set center
        cp = QDesktopWidget().availableGeometry().center()
        qr.moveCenter(cp)
        self.move(qr.topLeft())
        self.item_list.setStyleSheet("{}")
        self.slot_init()

if __name__ == '__main__':
    app = QApplication(sys.argv)
    demo = Direction()
    demo.show()
    sys.exit(app.exec_())