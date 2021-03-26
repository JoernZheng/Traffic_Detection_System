import sys
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from main_module.window_module.setLocationWin import Ui_widget


class setLocation(QWidget, Ui_widget):
    my_Signal = pyqtSignal(bool)
    def __init__(self, parent=None):
        super(setLocation, self).__init__(parent)
        self.setupUi(self)
        qr = self.frameGeometry()                   # set center
        cp = QDesktopWidget().availableGeometry().center()
        qr.moveCenter(cp)
        self.location = ''
        self.move(qr.topLeft())
        self.slot_init()

    def slot_init(self):
        self.pushButton.clicked.connect(self.verify)

    def verify(self):
        self.location = self.textEdit.toPlainText()
        self.my_Signal.emit(True)
        self.close()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    demo = setLocation()
    demo.show()
    sys.exit(app.exec_())