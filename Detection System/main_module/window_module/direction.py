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
        self.slot_init()

    def slot_init(self):
        self.verify_btn.clicked.connect(self.verify)
        self.item_list.currentIndexChanged.connect(self.choose)

    def choose(self):
        print(self.item_list.currentIndex() + 1)

    def verify(self):
        set_driection = self.item_list.currentText()
        self.my_Signal1.emit(set_driection)
        self.close()

if __name__ == '__main__':
    app = QApplication(sys.argv)
    demo = Direction()
    demo.show()
    sys.exit(app.exec_())