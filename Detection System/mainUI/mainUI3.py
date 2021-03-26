# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'mainUI.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import *

class ClickLabel(QLabel):
    clicked = QtCore.pyqtSignal()

    def mousePressEvent(self, event):
        self.clicked.emit()
        QLabel.mousePressEvent(self, event)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1920, 1080)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(MainWindow.sizePolicy().hasHeightForWidth())
        MainWindow.setSizePolicy(sizePolicy)
        MainWindow.setMinimumSize(QtCore.QSize(1920, 1080))
        MainWindow.setMaximumSize(QtCore.QSize(1920, 1080))
        MainWindow.setStyleSheet("")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")

        self.background = QtWidgets.QLabel(self.centralwidget)
        self.background.setGeometry(QtCore.QRect(0, 0, 1920, 1080))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.background.sizePolicy().hasHeightForWidth())
        self.background.setSizePolicy(sizePolicy)
        self.background.setMinimumSize(QtCore.QSize(1920, 1080))
        self.background.setMaximumSize(QtCore.QSize(1920, 720))
        self.background.setStyleSheet("background:#1F2429")
        self.background.setText("")
        self.background.setObjectName("background")

        self.title_1 = QtWidgets.QLabel(self.centralwidget)
        self.title_1.setGeometry(QtCore.QRect(670, 10, 161, 61))
        self.title_1.setStyleSheet("color:#1885FE;font: 30pt \"幼圆\";")
        self.title_1.setObjectName("title_1")
        self.ans_label = ClickLabel(self.centralwidget)
        self.ans_label.setGeometry(QtCore.QRect(110, 70, 1200, 700))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.ans_label.sizePolicy().hasHeightForWidth())
        self.ans_label.setSizePolicy(sizePolicy)
        self.ans_label.setMinimumSize(QtCore.QSize(1280, 720))
        self.ans_label.setMaximumSize(QtCore.QSize(1280, 720))
        self.ans_label.setStyleSheet("background:black")
        self.ans_label.setText("")
        self.ans_label.setObjectName("ans_label")
        self.title_2 = QtWidgets.QLabel(self.centralwidget)
        self.title_2.setGeometry(QtCore.QRect(1530, 10, 171, 51))
        self.title_2.setStyleSheet("color:#1885FE;\n"
"font: 30pt \"幼圆\";")
        self.title_2.setObjectName("title_2")
        self.illegalImg1 = QtWidgets.QLabel(self.centralwidget)
        self.illegalImg1.setGeometry(QtCore.QRect(1440, 90, 350, 150))
        self.illegalImg1.setMinimumSize(QtCore.QSize(350, 150))
        self.illegalImg1.setMaximumSize(QtCore.QSize(350, 150))
        self.illegalImg1.setStyleSheet("")
        self.illegalImg1.setText("")
        self.illegalImg1.setObjectName("illegalImg1")
        self.statistic1 = QtWidgets.QLabel(self.centralwidget)
        self.statistic1.setGeometry(QtCore.QRect(110, 800, 171, 41))
        self.statistic1.setStyleSheet("color:rgb(23, 118, 147);\n"
"font: 9pt \"微软雅黑\";")
        self.statistic1.setObjectName("statistic1")
        self.statistic2 = QtWidgets.QLabel(self.centralwidget)
        self.statistic2.setGeometry(QtCore.QRect(840, 800, 191, 41))
        self.statistic2.setStyleSheet("color:rgb(23, 118, 147);\n"
"font: 20pt \"微软雅黑\";")
        self.statistic2.setObjectName("statistic2")
        self.plugnum1 = QtWidgets.QLabel(self.centralwidget)
        self.plugnum1.setGeometry(QtCore.QRect(110, 850, 200, 100))
        self.plugnum1.setMinimumSize(QtCore.QSize(200, 100))
        self.plugnum1.setMaximumSize(QtCore.QSize(200, 100))
        self.plugnum1.setStyleSheet("image:url(mainUI/frame2.png)")
        self.plugnum1.setText("")
        self.plugnum1.setObjectName("plugnum1")
        self.plugnum2 = QtWidgets.QLabel(self.centralwidget)
        self.plugnum2.setGeometry(QtCore.QRect(840, 850, 200, 100))
        self.plugnum2.setMinimumSize(QtCore.QSize(200, 100))
        self.plugnum2.setMaximumSize(QtCore.QSize(200, 100))
        self.plugnum2.setStyleSheet("image:url(mainUI/frame2.png)")
        self.plugnum2.setText("")
        self.plugnum2.setObjectName("plugnum2")
        self.carCountLabel = QtWidgets.QLabel(self.centralwidget)
        self.carCountLabel.setGeometry(QtCore.QRect(120, 870, 160, 45))
        self.carCountLabel.setMinimumSize(QtCore.QSize(160, 45))
        self.carCountLabel.setMaximumSize(QtCore.QSize(160, 45))
        self.carCountLabel.setStyleSheet("background:#1F2429;\n"
"color:white; font-size:28px; font-weight:bold;")
        self.carCountLabel.setText("")
        self.carCountLabel.setAlignment(QtCore.Qt.AlignCenter)
        self.carCountLabel.setObjectName("carCountLabel")
        self.peopleCountLabel = QtWidgets.QLabel(self.centralwidget)
        self.peopleCountLabel.setGeometry(QtCore.QRect(850, 870, 160, 45))
        self.peopleCountLabel.setMinimumSize(QtCore.QSize(160, 45))
        self.peopleCountLabel.setMaximumSize(QtCore.QSize(160, 45))
        self.peopleCountLabel.setStyleSheet("background:#1F2429;\n"
"color:white; font-size:28px; font-weight:bold;")
        self.peopleCountLabel.setText("")
        self.peopleCountLabel.setAlignment(QtCore.Qt.AlignCenter)
        self.peopleCountLabel.setObjectName("peopleCountLabel")
        self.carCountImg = GraphicsLayoutWidget(self.centralwidget)
        self.carCountImg.setGeometry(QtCore.QRect(380, 810, 250, 150))
        self.carCountImg.setMinimumSize(QtCore.QSize(250, 150))
        self.carCountImg.setMaximumSize(QtCore.QSize(251, 150))
        self.carCountImg.setStyleSheet("background:#1F2429;")
        self.carCountImg.setObjectName("carCountImg")
        self.peopleCountImg = GraphicsLayoutWidget(self.centralwidget)
        self.peopleCountImg.setGeometry(QtCore.QRect(1080, 810, 250, 150))
        self.peopleCountImg.setMinimumSize(QtCore.QSize(250, 150))
        self.peopleCountImg.setMaximumSize(QtCore.QSize(250, 150))
        self.peopleCountImg.setStyleSheet("background:#1F2429;")
        self.peopleCountImg.setObjectName("peopleCountImg")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(1410, 60, 400, 250))
        self.label_3.setMinimumSize(QtCore.QSize(400, 250))
        self.label_3.setMaximumSize(QtCore.QSize(400, 250))
        self.label_3.setStyleSheet("image:url(mainUI/frame3.png); background:transparent;")
        self.label_3.setText("")
        self.label_3.setObjectName("label_3")
        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        self.label_4.setGeometry(QtCore.QRect(1410, 370, 400, 250))
        self.label_4.setMinimumSize(QtCore.QSize(400, 250))
        self.label_4.setMaximumSize(QtCore.QSize(400, 250))
        self.label_4.setStyleSheet("image:url(mainUI/frame3.png)")
        self.label_4.setText("")
        self.label_4.setObjectName("label_4")
        self.label_5 = QtWidgets.QLabel(self.centralwidget)
        self.label_5.setGeometry(QtCore.QRect(1410, 680, 400, 250))
        self.label_5.setMinimumSize(QtCore.QSize(400, 250))
        self.label_5.setMaximumSize(QtCore.QSize(400, 250))
        self.label_5.setStyleSheet("image:url(mainUI/frame3.png)")
        self.label_5.setText("")
        self.label_5.setObjectName("label_5")
        self.illegalImg2 = QtWidgets.QLabel(self.centralwidget)
        self.illegalImg2.setGeometry(QtCore.QRect(1440, 400, 350, 150))
        self.illegalImg2.setMinimumSize(QtCore.QSize(350, 150))
        self.illegalImg2.setMaximumSize(QtCore.QSize(350, 150))
        self.illegalImg2.setStyleSheet("background:#1F2429")
        self.illegalImg2.setText("")
        self.illegalImg2.setObjectName("illegalImg2")
        self.illegalImg3 = QtWidgets.QLabel(self.centralwidget)
        self.illegalImg3.setGeometry(QtCore.QRect(1440, 710, 350, 150))
        self.illegalImg3.setMinimumSize(QtCore.QSize(350, 150))
        self.illegalImg3.setMaximumSize(QtCore.QSize(350, 150))
        self.illegalImg3.setStyleSheet("background:#1F2429")
        self.illegalImg3.setText("")
        self.illegalImg3.setObjectName("illegalImg3")
        self.illegalInfo1 = QtWidgets.QLabel(self.centralwidget)
        self.illegalInfo1.setGeometry(QtCore.QRect(1440, 240, 350, 40))
        self.illegalInfo1.setMinimumSize(QtCore.QSize(350, 40))
        self.illegalInfo1.setMaximumSize(QtCore.QSize(350, 40))
        self.illegalInfo1.setStyleSheet("BACKGROUND:RED;")
        self.illegalInfo1.setText("")
        self.illegalInfo1.setStyleSheet("background:red;color:white; font-size:18px; font-weight:bold;")
        self.illegalInfo1.setAlignment(QtCore.Qt.AlignCenter)
        self.illegalInfo1.setObjectName("illegalInfo1")
        self.illegalInfo2 = QtWidgets.QLabel(self.centralwidget)
        self.illegalInfo2.setGeometry(QtCore.QRect(1440, 550, 350, 40))
        self.illegalInfo2.setMinimumSize(QtCore.QSize(350, 40))
        self.illegalInfo2.setMaximumSize(QtCore.QSize(350, 40))
        self.illegalInfo2.setStyleSheet("BACKGROUND:RED;")
        self.illegalInfo2.setText("")
        self.illegalInfo2.setStyleSheet("background:red;\n"
                                        "color:white; font-size:18px; font-weight:bold;")
        self.illegalInfo2.setAlignment(QtCore.Qt.AlignCenter)
        self.illegalInfo2.setObjectName("illegalInfo2")
        self.illegalInfo3 = QtWidgets.QLabel(self.centralwidget)
        self.illegalInfo3.setGeometry(QtCore.QRect(1440, 860, 350, 40))
        self.illegalInfo3.setMinimumSize(QtCore.QSize(350, 40))
        self.illegalInfo3.setMaximumSize(QtCore.QSize(350, 40))
        self.illegalInfo3.setStyleSheet("background:red;")
        self.illegalInfo3.setText("")
        self.illegalInfo3.setStyleSheet("background:red;\n"
                                        "color:white; font-size:18px; font-weight:bold;")
        self.illegalInfo3.setAlignment(QtCore.Qt.AlignCenter)
        self.illegalInfo3.setObjectName("illegalInfo3")
        self.start_comboBox = QtWidgets.QComboBox(self.centralwidget)
        self.start_comboBox.setGeometry(QtCore.QRect(-40, 950, 150, 90))
        self.start_comboBox.setMinimumSize(QtCore.QSize(200, 90))
        self.start_comboBox.setMaximumSize(QtCore.QSize(200, 90))
        self.start_comboBox.setStyleSheet("QComboBox{\n"
"    image:url(mainUI/left.png);\n"
"    background: transparent;\n"
"    border-radius:40px;\n"
"    color:transparent;\n"
"    border: none;\n"
"}\n"
"\n"
"QComboBox::drop-down{border-style: none;}\n"
"\n"
"QComboBox::item {\n"
"     padding:8px 20px;\n"
"     background: white;\n"
"     width:120px; \n"
"     height:50px;\n"
"     color:#2dabf9;\n"
"     font-size:18px;\n"
"     border-bottom:2px solid #DBDBDB;\n"
" }\n"
"\n"
"QComboBox::item:selected{\n"
"    background-color: #2dabf9;\n"
"    color:white;\n"
"    font-weight:bold;\n"
"}")
        self.start_comboBox.setInsertPolicy(QtWidgets.QComboBox.InsertAtCurrent)
        self.start_comboBox.setObjectName("start_comboBox")
        self.start_comboBox.addItem("")
        self.start_comboBox.addItem("")
        self.start_comboBox.addItem("")
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.title_1.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-weight:600;\">交通检测</span></p></body></html>"))
        self.title_2.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-weight:600;\">违章检测</span></p></body></html>"))
        self.statistic1.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-size:18pt;\">&gt;&gt;当前车流量</span></p></body></html>"))
        self.statistic2.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-size:18pt;\">&gt;&gt;当前人流量</span></p></body></html>"))
        self.start_comboBox.setItemText(0, _translate("MainWindow", "选择视频源"))
        self.start_comboBox.setItemText(1, _translate("MainWindow", "设置抓取路径"))
        self.start_comboBox.setItemText(2, _translate("MainWindow", "设置路口地址"))

from pyqtgraph import GraphicsLayoutWidget
