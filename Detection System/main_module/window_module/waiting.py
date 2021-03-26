# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'weiting.ui'
#
# Created by: PyQt5 UI code generator 5.14.1
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(239, 220)
        self.label = QtWidgets.QLabel(Form)
        self.label.setGeometry(QtCore.QRect(30, 30, 181, 41))
        self.label.setStyleSheet("font-size:28px;\n"
"font-weight:bold;")
        self.label.setObjectName("label")
        self.verify_btn = QtWidgets.QPushButton(Form)
        self.verify_btn.setGeometry(QtCore.QRect(30, 150, 181, 41))
        self.verify_btn.setStyleSheet("font-size:24px;\n"
"color:white;\n"
"border:none;\n"
"border-radius:20px;\n"
"height:50px;\n"
"background-color:#317EF3;")
        self.verify_btn.setObjectName("verify_btn")
        self.wait_time = QtWidgets.QLineEdit(Form)
        self.wait_time.setGeometry(QtCore.QRect(30, 90, 181, 41))
        self.wait_time.setStyleSheet("font-size:28px;\n"
"font-weight:bold;\n"
"")
        self.wait_time.setObjectName("wait_time")

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.label.setText(_translate("Form", "违停时间(s):"))
        self.verify_btn.setText(_translate("Form", "确定"))
