import sys
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from main_module.window_module.waiting import Ui_Form


class Wait(QWidget, Ui_Form):
    my_Signal = pyqtSignal(str)
    def __init__(self, parent=None):
        super(Wait, self).__init__(parent)
        self.setupUi(self)
        qr = self.frameGeometry()                   # set center
        cp = QDesktopWidget().availableGeometry().center()
        qr.moveCenter(cp)
        self.move(qr.topLeft())
        self.slot_init()

    def slot_init(self):
        self.verify_btn.clicked.connect(self.verify)

    def verify(self):
        self.set_time = self.wait_time.text()
        self.my_Signal.emit(self.set_time)
        self.close()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    demo = Wait()
    demo.show()
    sys.exit(app.exec_())