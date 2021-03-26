import sys
from HyperLPR.demo import *
from darknet import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from Zoning import Drawing
from mainUI.mainUI3 import Ui_MainWindow
from main_module.window_module.setLocation import setLocation
from main_module.window_module.progress import Demo

model = pr.LPR("./HyperLPR/model/cascade.xml",
               "./HyperLPR/model/model12.h5",
               "./HyperLPR/model/ocr_plate_all_gru.h5")


class CameraPageWindow(QMainWindow, Ui_MainWindow):
    def __init__(self, parent=None):
        super(CameraPageWindow, self).__init__(parent)
        threading.Thread(target=self.init_yolo).start()
        self.setWindowFlags(Qt.CustomizeWindowHint)  # 窗口导航条去除
        self.ans_img = {'ans': None}
        self.has_ans = False
        self.video_location = '测试地点'
        self.palette = QPalette()
        self.setupUi(self)
        self.setLabelOpacity()
        self.slot_init()

    def keyPressEvent(self, event):  # 重写keyPressEvent()事件处理器。
        if event.key() == Qt.Key_Escape:  # 当我们按住键盘是esc按键时
            self.closeEvent(QCloseEvent)  # 关闭程序

    def setLabelOpacity(self):
        op = QGraphicsOpacityEffect()
        op.setOpacity(0.3)
        self.illegalInfo1.setGraphicsEffect(op)
        self.illegalInfo1.setAutoFillBackground(True)
        op = QGraphicsOpacityEffect()
        op.setOpacity(0.3)
        self.illegalInfo2.setGraphicsEffect(op)
        self.illegalInfo2.setAutoFillBackground(True)
        op = QGraphicsOpacityEffect()
        op.setOpacity(0.3)
        self.illegalInfo3.setGraphicsEffect(op)
        self.illegalInfo3.setAutoFillBackground(True)

    def init_yolo(self):
        performDetect()
        self._download_path = "/root"  # Linux默认下载路径是root
        self.down_video_path = "/root"
        self.upload_filename = ""
        self.ans_path = ""

    def slot_init(self):
        # 信号和槽连接
        self.ans_label.clicked.connect(self.capture_ans_img)
        self.start_comboBox.setCurrentIndex(3)
        self.start_comboBox.currentIndexChanged.connect(self.choose)
        self.child = Drawing()
        self.setLocation = setLocation()

    def choose(self):
        index = self.start_comboBox.currentIndex()
        if index == 0:
            self.show_drag_paint()
        elif index == 1:
            self.set_download_path()
        elif index == 2:
            self.set_video_down_path()
        self.start_comboBox.setCurrentIndex(3)

    def start_detect_video(self):
        if self.child.detect_video:
            self.has_ans = True
            show_list = [self.illegalImg1, self.illegalImg2, self.illegalImg3]  # 右侧的3个展示框
            info_list = [self.carCountLabel, self.carCountImg, self.peopleCountLabel, self.peopleCountImg]
            illegalInfo_list = [self.illegalInfo1, self.illegalInfo2, self.illegalInfo3]
            YOLO(self.child.Areas, self.ans_label, show_list, self.down_video_path, self.ans_img, info_list, illegalInfo_list, self.video_location, self.fname)
            # threading.Thread(target=YOLO, args=(self.child.Areas, self.ans_label, show_list, self.down_video_path, self.ans_img, info_list, illegalInfo_list, self.fname)).start()
            # Process(target=YOLO, args=(self.child.Areas, self.ans_label, show_list, self.down_video_path, self.ans_img, info_list, illegalInfo_list, self.fname)).start()
            print('----------------YOLO OVER-----------------------')
            self.child.detect_video = False

    def show_progress(self):
        self.progress = Demo()
        self.progress.set_time(30)
        self.progress.show()

    def show_drag_paint(self):
        self.fname, _ = QFileDialog.getOpenFileName(self, '选择视频', '/root', 'Video files(*.mp4 *.MP4 *.avi *.webm)')
        cap = cv2.VideoCapture(self.fname)
        if not cap.isOpened():  # open failed
            QMessageBox.about(self, '提示', '打开视频失败')
            return
        video_name = str(self.fname).split('/')[-1].split('.')[0]
        self.child.Areas = init_areas(1280, 720, video_name)
        self.Draw_Win(cap)

    def Draw_Win(self, cap):
        ret, frame = cap.read()
        frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        frame = cv2.resize(frame, (1280, 720))
        cap.release()
        self.child.clear()
        self.palette.setBrush(QPalette.Background, QBrush(Image.fromarray(np.uint8(frame)).toqpixmap()))
        self.child.setPalette(self.palette)
        self.child.img_h = frame.shape[0]
        self.child.img_w = frame.shape[1]
        self.child.my_Signal.connect(self.start_detect_video)  # 与drag_paint中的exit()中的信号量进行绑定
        self.child.show()

    def capture_ans_img(self):  # 下载检测图片到本地
        if self.has_ans:
            ans_img = self.ans_img['ans']
            ans_img = cv2.cvtColor(ans_img, cv2.COLOR_BGR2RGB)
            cv2.imwrite(self._download_path + '/' + 'ans.jpg', ans_img)
            QMessageBox.about(self, '提示', '画面抓取成功')
        else:
            QMessageBox.about(self, '提示', '画面抓取失败')

    def set_download_path(self):
        dirname = QFileDialog.getExistingDirectory(self, '选择文件夹', '/root')
        self.download_path = dirname
        print(self._download_path)

    def setVideoLocation(self):
        self.video_location = self.setLocation.location

    def set_video_down_path(self):
        self.setLocation.my_Signal.connect(self.setVideoLocation)
        self.setLocation.show()


    def start_predict_one(self, input_img_path):
        t1 = time.time()
        from tqdm import tqdm
        for pic in tqdm(os.listdir('pictures')):
            performDetect('/root/PycharmProjects/yolo/pictures/' + pic)
        print(1077 / (time.time() - t1))

    def closeEvent(self, QCloseEvent):  # 自定义PyQt5窗口的右上角退出点击事件
        app = QApplication.instance()
        reply = QMessageBox.question(self, '退出', '确定退出？', QMessageBox.Yes | QMessageBox.Cancel, QMessageBox.Cancel)
        if reply == QMessageBox.Yes:
            sys.exit(app.exec())  # 应用退出

    def set_center(self):  # Window set Center
        qr = self.frameGeometry()
        cp = QDesktopWidget().availableGeometry().center()
        qr.moveCenter(cp)
        self.move(qr.topLeft())

def predict(img):
    for pstr, confidence, rect in model.SimpleRecognizePlateByE2E(img):
        b_str = (pstr.encode('utf-8'))
        return (b_str, confidence)

if __name__ == '__main__':
    app = QApplication(sys.argv)
    camer = CameraPageWindow()
    camer.set_center()
    camer.show()
    app.processEvents()
    sys.exit(app.exec())  # 应用退出

'''
from PyQt5.QtWidgets import *

class ClickLabel(QLabel):
    clicked = QtCore.pyqtSignal()

    def mousePressEvent(self, event):
        self.clicked.emit()
        QLabel.mousePressEvent(self, event)

设置了这个类之后,还需要将之前的QLable改成ClickLabel 

'''
