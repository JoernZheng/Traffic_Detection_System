from PyQt5 import QtCore, QtWidgets


class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(300, 300)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(Form.sizePolicy().hasHeightForWidth())
        Form.setSizePolicy(sizePolicy)
        Form.setMinimumSize(QtCore.QSize(300, 300))
        Form.setMaximumSize(QtCore.QSize(300, 300))
        Form.setSizeIncrement(QtCore.QSize(300, 300))
        Form.setStyleSheet("background-color:white;")
        self.item_list = QtWidgets.QComboBox(Form)
        self.item_list.setGeometry(QtCore.QRect(60, 130, 191, 41))
        self.item_list.setStyleSheet("QComboBox::item:selected{background-color:#2dabf9;color:white;};")
        self.item_list.setObjectName("item_list")
        self.item_list.addItem("")
        self.item_list.addItem("")
        self.item_list.addItem("")
        self.item_list.addItem("")
        self.item_list.addItem("")
        self.label = QtWidgets.QLabel(Form)
        self.label.setGeometry(QtCore.QRect(60, 50, 191, 41))
        self.label.setStyleSheet("font-size:32px;\n"
"font-weight:bold;")
        self.label.setObjectName("label")
        self.verify_btn = QtWidgets.QPushButton(Form)
        self.verify_btn.setGeometry(QtCore.QRect(60, 210, 181, 51))
        self.verify_btn.setStyleSheet("font-size:30px;\n"
"font-weight:bold;\n"
"background-color:#0274FD;\n"
"height:50px;\n"
"border-radius:25px;\n"
"border:none;")
        self.verify_btn.setObjectName("verify_btn")
        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.item_list.setItemText(0, _translate("Form", "左转车道"))
        self.item_list.setItemText(1, _translate("Form", "右转车道"))
        self.item_list.setItemText(2, _translate("Form", "直行车道"))
        self.item_list.setItemText(3, _translate("Form", "左转或直行车道"))
        self.item_list.setItemText(4, _translate("Form", "右转或直行车道"))
        self.label.setText(_translate("Form", "行车道方向:"))
        self.verify_btn.setText(_translate("Form", "确定"))
