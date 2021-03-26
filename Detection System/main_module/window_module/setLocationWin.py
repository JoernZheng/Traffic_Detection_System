# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'setLocation.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_widget(object):
    def setupUi(self, widget):
        widget.setObjectName("widget")
        widget.resize(415, 260)
        widget.setMinimumSize(QtCore.QSize(415, 260))
        widget.setMaximumSize(QtCore.QSize(415, 260))
        widget.setStyleSheet("background:white;")
        self.label = QtWidgets.QLabel(widget)
        self.label.setGeometry(QtCore.QRect(140, 20, 151, 51))
        self.label.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.label.setStyleSheet("font-size:32px;\n"
"font-weight:bold;")
        self.label.setObjectName("label")
        self.textEdit = QtWidgets.QTextEdit(widget)
        self.textEdit.setGeometry(QtCore.QRect(140, 105, 250, 45))
        self.textEdit.setMinimumSize(QtCore.QSize(250, 45))
        self.textEdit.setMaximumSize(QtCore.QSize(250, 45))
        self.textEdit.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.textEdit.setStyleSheet("font-size:24px;\n"
"margin:4px 0 0 0;")
        self.textEdit.setObjectName("textEdit")
        self.pushButton = QtWidgets.QPushButton(widget)
        self.pushButton.setGeometry(QtCore.QRect(130, 190, 150, 40))
        self.pushButton.setMinimumSize(QtCore.QSize(150, 40))
        self.pushButton.setMaximumSize(QtCore.QSize(150, 40))
        self.pushButton.setStyleSheet("border-radius:20px;\n"
"background:#4662D9;\n"
"font-size:24px;\n"
"font-weight:bold;")
        self.pushButton.setObjectName("pushButton")
        self.label_2 = QtWidgets.QLabel(widget)
        self.label_2.setGeometry(QtCore.QRect(20, 110, 111, 31))
        self.label_2.setStyleSheet("font-size:24px;\n"
"font-weight:bold;")
        self.label_2.setObjectName("label_2")

        self.retranslateUi(widget)
        QtCore.QMetaObject.connectSlotsByName(widget)

    def retranslateUi(self, widget):
        _translate = QtCore.QCoreApplication.translate
        widget.setWindowTitle(_translate("widget", "Form"))
        self.label.setText(_translate("widget", "路口设置"))
        self.pushButton.setText(_translate("widget", "确认"))
        self.label_2.setText(_translate("widget", "路口地址:"))

