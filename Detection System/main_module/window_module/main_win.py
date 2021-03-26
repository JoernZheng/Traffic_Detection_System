# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'road.ui'
#
# Created by: PyQt5 UI code generator 5.14.1
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *

class ClickLabel(QLabel):
    clicked = QtCore.pyqtSignal()

    def mousePressEvent(self, event):
        self.clicked.emit()
        QLabel.mousePressEvent(self, event)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1700, 880)
        MainWindow.setMinimumSize(QtCore.QSize(1700, 880))
        MainWindow.setMaximumSize(QtCore.QSize(1700, 880))
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.widget = QtWidgets.QWidget(self.centralwidget)
        self.widget.setGeometry(QtCore.QRect(90, 10, 261, 801))
        self.widget.setStyleSheet("background:white;")
        self.widget.setObjectName("widget")
        self.verticalLayoutWidget = QtWidgets.QWidget(self.widget)
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(0, 0, 261, 801))
        self.verticalLayoutWidget.setObjectName("verticalLayoutWidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.pushButton_5 = QtWidgets.QPushButton(self.verticalLayoutWidget)
        self.pushButton_5.setStyleSheet("height:80px;\n"
"margin:0 20px;\n"
"font-size:30px;\n"
"border:none;\n"
"border-top:2px solid black;\n"
"border-bottom:2px solid black;")
        self.pushButton_5.setObjectName("pushButton_5")
        self.verticalLayout.addWidget(self.pushButton_5)
        self.open_img_btn = QtWidgets.QPushButton(self.verticalLayoutWidget)
        self.open_img_btn.setStyleSheet("margin:0 10px;\n"
"height:70px;\n"
"background-color:#0483EC;\n"
"border-radius:35px;\n"
"border:none;\n"
"font: 14pt \"宋体\";\n"
"font-weight:bold;\n"
"color:white;")
        self.open_img_btn.setObjectName("open_img_btn")
        self.verticalLayout.addWidget(self.open_img_btn)
        self.open_video_btn = QtWidgets.QPushButton(self.verticalLayoutWidget)
        self.open_video_btn.setStyleSheet("margin:0 10px;\n"
"height:70px;\n"
"background-color:#0483EC;\n"
"border-radius:35px;\n"
"border:none;\n"
"font: 14pt \"宋体\";\n"
"font-weight:bold;\n"
"color:white;")
        self.open_video_btn.setObjectName("open_video_btn")
        self.verticalLayout.addWidget(self.open_video_btn)
        self.open_camera_btn = QtWidgets.QPushButton(self.verticalLayoutWidget)
        self.open_camera_btn.setStyleSheet("margin:0 10px;\n"
"height:70px;\n"
"background-color:#0483EC;\n"
"border-radius:35px;\n"
"border:none;\n"
"font: 14pt \"宋体\";\n"
"font-weight:bold;\n"
"color:white;")
        self.open_camera_btn.setObjectName("open_camera_btn")
        self.verticalLayout.addWidget(self.open_camera_btn)
        self.drag_paint_btn = QtWidgets.QPushButton(self.verticalLayoutWidget)
        self.drag_paint_btn.setStyleSheet("margin:0 10px;\n"
"height:70px;\n"
"background-color:#0483EC;\n"
"border-radius:35px;\n"
"border:none;\n"
"font: 14pt \"宋体\";\n"
"font-weight:bold;\n"
"color:white;")
        self.drag_paint_btn.setObjectName("drag_paint_btn")
        self.verticalLayout.addWidget(self.drag_paint_btn)
        self.widget_2 = QtWidgets.QWidget(self.centralwidget)
        self.widget_2.setGeometry(QtCore.QRect(350, 10, 921, 801))
        self.widget_2.setStyleSheet("")
        self.widget_2.setObjectName("widget_2")
        self.ans_label = ClickLabel(self.widget_2)
        self.ans_label.setGeometry(QtCore.QRect(0, 0, 941, 811))
        self.ans_label.setStyleSheet("background:gray;")
        self.ans_label.setObjectName("ans_label")
        self.widget_3 = QtWidgets.QWidget(self.centralwidget)
        self.widget_3.setGeometry(QtCore.QRect(1270, 10, 341, 801))
        self.widget_3.setStyleSheet("background:white;")
        self.widget_3.setObjectName("widget_3")
        self.verticalLayoutWidget_2 = QtWidgets.QWidget(self.widget_3)
        self.verticalLayoutWidget_2.setGeometry(QtCore.QRect(0, 0, 1922, 1232))
        self.verticalLayoutWidget_2.setObjectName("verticalLayoutWidget_2")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.verticalLayoutWidget_2)
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_2.setSpacing(0)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.show_1 = QtWidgets.QLabel(self.verticalLayoutWidget_2)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.show_1.sizePolicy().hasHeightForWidth())
        self.show_1.setSizePolicy(sizePolicy)
        self.show_1.setMinimumSize(QtCore.QSize(340, 270))
        self.show_1.setMaximumSize(QtCore.QSize(340, 270))
        self.show_1.setStyleSheet("background:#111;")
        self.show_1.setText("")
        self.show_1.setObjectName("show_1")
        self.verticalLayout_2.addWidget(self.show_1)
        self.show_2 = QtWidgets.QLabel(self.verticalLayoutWidget_2)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.show_2.sizePolicy().hasHeightForWidth())
        self.show_2.setSizePolicy(sizePolicy)
        self.show_2.setMinimumSize(QtCore.QSize(340, 270))
        self.show_2.setMaximumSize(QtCore.QSize(340, 270))
        self.show_2.setSizeIncrement(QtCore.QSize(340, 300))
        self.show_2.setStyleSheet("background:#111;")
        self.show_2.setObjectName("show_2")
        self.verticalLayout_2.addWidget(self.show_2)
        self.show_3 = QtWidgets.QLabel(self.verticalLayoutWidget_2)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.show_3.sizePolicy().hasHeightForWidth())
        self.show_3.setSizePolicy(sizePolicy)
        self.show_3.setMinimumSize(QtCore.QSize(340, 270))
        self.show_3.setMaximumSize(QtCore.QSize(340, 270))
        self.show_3.setStyleSheet("background:#111;")
        self.show_3.setObjectName("show_3")
        self.verticalLayout_2.addWidget(self.show_3)
        self.label_3 = QtWidgets.QLabel(self.verticalLayoutWidget_2)
        self.label_3.setStyleSheet("background:black;")
        self.label_3.setObjectName("label_3")
        self.verticalLayout_2.addWidget(self.label_3)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1700, 26))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.pushButton_5.setText(_translate("MainWindow", "智能交通检测"))
        self.open_img_btn.setText(_translate("MainWindow", "导入图片"))
        self.open_video_btn.setText(_translate("MainWindow", "导入视频"))
        self.open_camera_btn.setText(_translate("MainWindow", "打开摄像头"))
        self.drag_paint_btn.setText(_translate("MainWindow", "划定区域"))
