import sys
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from main_module.window_module.max_speed import Ui_Form


class Speed(QWidget, Ui_Form):
    my_Signal1 = pyqtSignal(str)
    my_Signal2 = pyqtSignal(str)
    def __init__(self, parent=None):
        super(Speed, self).__init__(parent)
        self.setupUi(self)
        qr = self.frameGeometry()                   # set center
        cp = QDesktopWidget().availableGeometry().center()
        qr.moveCenter(cp)
        self.move(qr.topLeft())
        self.slot_init()

    def slot_init(self):
        self.verify_btn.clicked.connect(self.verify)

    def verify(self):
        set_max = self.speed_text.text()
        set_len = self.area_len.text()
        self.my_Signal1.emit(set_max)
        self.my_Signal2.emit(set_len)
        self.close()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    demo = Speed()
    demo.show()
    sys.exit(app.exec_())