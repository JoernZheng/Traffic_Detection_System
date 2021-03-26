import sys
import time
from PyQt5.QtCore import Qt, QTimer
from PyQt5.QtWidgets import QApplication, QWidget, QProgressBar, QVBoxLayout, QLabel

t1 = 0


class Demo(QWidget):
    def __init__(self):
        global t1
        super(Demo, self).__init__()
        self.progressbar = QProgressBar(self)  # 1
        self.progressbar.setMinimum(0)  # 2
        self.progressbar.setMaximum(100)
        self.info_label = QLabel("视频加载中...")
        self.info_label.setAlignment(Qt.AlignHCenter)
        self.step = 0  #
        self.timer = QTimer(self)  # 4
        self.timer.timeout.connect(self.update_func)
        self.v_layout = QVBoxLayout()
        self.v_layout.addWidget(self.info_label)
        self.v_layout.addWidget(self.progressbar)
        self.setLayout(self.v_layout)
        t1 = time.time()
        self.timer.start(30)
        self.setWindowFlags(Qt.CustomizeWindowHint)

    def set_time(self, time):
        self.timer.start(time)

    def update_func(self):
        global t1
        self.step += 1
        self.progressbar.setValue(self.step)
        if self.step >= 100:
            self.timer.stop()
            self.close()
            print(time.time() - t1)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    demo = Demo()
    demo.show()
    sys.exit(app.exec_())