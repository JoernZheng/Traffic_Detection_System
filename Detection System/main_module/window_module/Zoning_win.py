# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'road2.ui'
#
# Created by: PyQt5 UI code generator 5.14.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("区域划定")
        Form.resize(1280, 720)
        self.widget = QtWidgets.QWidget(Form)
        self.widget.setGeometry(QtCore.QRect(270, 10, 921, 791))
        self.widget.setStyleSheet("")
        self.widget.setObjectName("widget")
        self.widget_2 = QtWidgets.QWidget(Form)
        self.widget_2.setGeometry(QtCore.QRect(10, 10, 261, 791))
        self.widget_2.setObjectName("widget_2")
        self.label = QtWidgets.QLabel(self.widget_2)
        self.label.setGeometry(QtCore.QRect(40, 100, 161, 61))
        self.label.setStyleSheet("font-weight:bold;\n""font-size:32px;")
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.widget_2)
        self.label_2.setGeometry(QtCore.QRect(50, 150, 151, 61))
        self.label_2.setStyleSheet("font-weight:bold;font-weight:24px;")
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(self.widget_2)
        self.label_3.setGeometry(QtCore.QRect(50, 200, 161, 71))
        self.label_3.setStyleSheet("font-weight:bold;font-weight:24px;")
        self.label_3.setObjectName("label_3")
        self.label_4 = QtWidgets.QLabel(self.widget_2)
        self.label_4.setGeometry(QtCore.QRect(50, 250, 151, 71))
        self.label_4.setStyleSheet("font-weight:bold;font-weight:24px;")
        self.label_4.setObjectName("label_4")
        self.label_5 = QtWidgets.QLabel(self.widget_2)
        self.label_5.setGeometry(QtCore.QRect(50, 300, 151, 71))
        self.label_5.setStyleSheet("font-weight:bold;font-weight:24px;")
        self.label_5.setObjectName("label_5")
        self.label_6 = QtWidgets.QLabel(self.widget_2)
        self.label_6.setGeometry(QtCore.QRect(50, 350, 151, 71))
        self.label_6.setStyleSheet("font-weight:bold;font-weight:24px;")
        self.label_6.setObjectName("label_6")
        # self.label_7 = QtWidgets.QLabel(self.widget_2)
        # self.label_7.setGeometry(QtCore.QRect(50, 450, 150, 71))
        # self.label_7.setStyleSheet("font-weight:bold;font-weight:24px;")
        # self.label_7.setObjectName("label_7")
        self.label_8 = QtWidgets.QLabel(self.widget_2)
        self.label_8.setGeometry(QtCore.QRect(50, 400, 150, 71))
        self.label_8.setStyleSheet("font-weight:bold;font-weight:24px;")
        self.label_8.setObjectName("label_8")
        self.label_9 = QtWidgets.QLabel(self.widget_2)
        self.label_9.setGeometry(QtCore.QRect(50, 450, 150, 71))
        self.label_9.setStyleSheet("font-weight:bold;font-weight:24px;")
        self.label_9.setObjectName("label_9")
        self.label_10 = QtWidgets.QLabel(self.widget_2)
        self.label_10.setGeometry(QtCore.QRect(50, 500, 150, 71))
        self.label_10.setStyleSheet("font-weight:bold;font-weight:24px;")
        self.label_10.setObjectName("label_10")

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "区域划定"))
        self.label.setText(_translate("Form", "Tip:"))
        self.label_2.setText(_translate("Form", "1.车辆统计区域划定"))
        self.label_3.setText(_translate("Form", "2.车辆违停区域划定"))
        self.label_4.setText(_translate("Form", "3.车速计算区域划定"))
        self.label_5.setText(_translate("Form", "4.压道线划定"))
        self.label_6.setText(_translate("Form", "5.车道方向区域划定"))
        self.label_8.setText(_translate("Form", "6:逆向行驶区域划定"))
        # self.label_7.setText(_translate("Form", "m:切换窗口大小"))
        self.label_9.setText(_translate("Form", "z:撤回 c:清空"))
        self.label_10.setText(_translate("Form", "e:保存退出"))