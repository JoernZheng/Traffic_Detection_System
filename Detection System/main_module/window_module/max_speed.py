# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'max_speed.ui'
#
# Created by: PyQt5 UI code generator 5.14.1
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(270, 310)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(Form.sizePolicy().hasHeightForWidth())
        Form.setSizePolicy(sizePolicy)
        Form.setMinimumSize(QtCore.QSize(270, 310))
        Form.setMaximumSize(QtCore.QSize(270, 310))
        Form.setStyleSheet("background-color:white;")
        self.verify_btn = QtWidgets.QPushButton(Form)
        self.verify_btn.setGeometry(QtCore.QRect(40, 260, 191, 41))
        self.verify_btn.setStyleSheet("font-size:24px;\n"
"font-weight:bold;\n"
"background-color:#317EF3;\n"
"color:white;\n"
"border:none;\n"
"height:40px;\n"
"border-radius:20px;")
        self.verify_btn.setObjectName("verify_btn")
        self.label = QtWidgets.QLabel(Form)
        self.label.setGeometry(QtCore.QRect(40, 20, 191, 41))
        self.label.setStyleSheet("font-size:20px;\n"
"font-weight:bold;")
        self.label.setObjectName("label")
        self.speed_text = QtWidgets.QLineEdit(Form)
        self.speed_text.setGeometry(QtCore.QRect(40, 80, 191, 41))
        self.speed_text.setStyleSheet("font-size:32px;\n"
"font-weight:bold;")
        self.speed_text.setText("")
        self.speed_text.setObjectName("speed_text")
        self.label_2 = QtWidgets.QLabel(Form)
        self.label_2.setGeometry(QtCore.QRect(40, 150, 131, 31))
        self.label_2.setStyleSheet("font-size:20px;\n"
"font-weight:bold;")
        self.label_2.setObjectName("label_2")
        self.area_len = QtWidgets.QLineEdit(Form)
        self.area_len.setGeometry(QtCore.QRect(40, 190, 191, 41))
        self.area_len.setObjectName("area_len")
        self.area_len.setStyleSheet("font-size:32px;\n"
                                      "font-weight:bold;")

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.verify_btn.setText(_translate("Form", "确定"))
        self.label.setText(_translate("Form", "最大车速值:(Km/h)"))
        self.label_2.setText(_translate("Form", "区间长度:(m)"))
