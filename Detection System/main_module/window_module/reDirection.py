# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'reDirection.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(370, 250)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(Form.sizePolicy().hasHeightForWidth())
        Form.setSizePolicy(sizePolicy)
        Form.setMinimumSize(QtCore.QSize(370, 250))
        Form.setMaximumSize(QtCore.QSize(370, 250))
        Form.setStyleSheet("background:white;")
        self.radioButton = QtWidgets.QRadioButton(Form)
        self.radioButton.setGeometry(QtCore.QRect(50, 50, 20, 21))
        self.radioButton.setStyleSheet("font-size:24px;")
        self.radioButton.setText("")
        self.radioButton.setObjectName("radioButton")
        self.radioButton_2 = QtWidgets.QRadioButton(Form)
        self.radioButton_2.setGeometry(QtCore.QRect(50, 140, 16, 20))
        self.radioButton_2.setStyleSheet("font-size:24px;")
        self.radioButton_2.setText("")
        self.radioButton_2.setObjectName("radioButton_2")
        self.label = QtWidgets.QLabel(Form)
        self.label.setGeometry(QtCore.QRect(70, 30, 261, 61))
        self.label.setStyleSheet("font-size:32px;\n"
"font-weight:bold;")
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(Form)
        self.label_2.setGeometry(QtCore.QRect(70, 120, 261, 51))
        self.label_2.setStyleSheet("font-size:32px;\n"
"font-weight:bold;")
        self.label_2.setObjectName("label_2")
        self.pushButton = QtWidgets.QPushButton(Form)
        self.pushButton.setGeometry(QtCore.QRect(110, 190, 171, 51))
        self.pushButton.setStyleSheet("font-size:32px;\n"
"color:white;\n"
"border:none;\n"
"font-weight:bold;\n"
"background-color:blue;\n"
"border-radius:25px;\n"
"")
        self.pushButton.setObjectName("pushButton")

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.label.setText(_translate("Form", "顶部到底部(T2B)"))
        self.label_2.setText(_translate("Form", "底部到顶部(B2T)"))
        self.pushButton.setText(_translate("Form", "确定"))

