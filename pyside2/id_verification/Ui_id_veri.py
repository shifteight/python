# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '/Users/kevin/Documents/Git/python/pyside2/id_verification/id_veri.ui',
# licensing of '/Users/kevin/Documents/Git/python/pyside2/id_verification/id_veri.ui' applies.
#
# Created: Sun May 26 23:21:08 2019
#      by: pyside2-uic  running on PySide2 5.12.3
#
# WARNING! All changes made in this file will be lost!

from PySide2 import QtCore, QtGui, QtWidgets

class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(477, 364)
        self.widget = QtWidgets.QWidget(Form)
        self.widget.setGeometry(QtCore.QRect(51, 51, 208, 149))
        self.widget.setObjectName("widget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.widget)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout()
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.label = QtWidgets.QLabel(self.widget)
        self.label.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label.setObjectName("label")
        self.verticalLayout_2.addWidget(self.label)
        self.label_2 = QtWidgets.QLabel(self.widget)
        self.label_2.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_2.setObjectName("label_2")
        self.verticalLayout_2.addWidget(self.label_2)
        self.label_3 = QtWidgets.QLabel(self.widget)
        self.label_3.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_3.setObjectName("label_3")
        self.verticalLayout_2.addWidget(self.label_3)
        self.label_4 = QtWidgets.QLabel(self.widget)
        self.label_4.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_4.setObjectName("label_4")
        self.verticalLayout_2.addWidget(self.label_4)
        self.label_5 = QtWidgets.QLabel(self.widget)
        self.label_5.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_5.setObjectName("label_5")
        self.verticalLayout_2.addWidget(self.label_5)
        self.horizontalLayout.addLayout(self.verticalLayout_2)
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.lEditId = QtWidgets.QLineEdit(self.widget)
        self.lEditId.setObjectName("lEditId")
        self.verticalLayout.addWidget(self.lEditId)
        self.lEditResult = QtWidgets.QLineEdit(self.widget)
        self.lEditResult.setObjectName("lEditResult")
        self.verticalLayout.addWidget(self.lEditResult)
        self.lEditArea = QtWidgets.QLineEdit(self.widget)
        self.lEditArea.setObjectName("lEditArea")
        self.verticalLayout.addWidget(self.lEditArea)
        self.lEditBirth = QtWidgets.QLineEdit(self.widget)
        self.lEditBirth.setObjectName("lEditBirth")
        self.verticalLayout.addWidget(self.lEditBirth)
        self.lEditSex = QtWidgets.QLineEdit(self.widget)
        self.lEditSex.setObjectName("lEditSex")
        self.verticalLayout.addWidget(self.lEditSex)
        self.horizontalLayout.addLayout(self.verticalLayout)
        self.widget1 = QtWidgets.QWidget(Form)
        self.widget1.setGeometry(QtCore.QRect(270, 50, 68, 72))
        self.widget1.setObjectName("widget1")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.widget1)
        self.verticalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.btnQuery = QtWidgets.QPushButton(self.widget1)
        self.btnQuery.setObjectName("btnQuery")
        self.verticalLayout_3.addWidget(self.btnQuery)
        self.btnClear = QtWidgets.QPushButton(self.widget1)
        self.btnClear.setObjectName("btnClear")
        self.verticalLayout_3.addWidget(self.btnClear)

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        Form.setWindowTitle(QtWidgets.QApplication.translate("Form", "Form", None, -1))
        self.label.setText(QtWidgets.QApplication.translate("Form", "18位身份证", None, -1))
        self.label_2.setText(QtWidgets.QApplication.translate("Form", "查询结果", None, -1))
        self.label_3.setText(QtWidgets.QApplication.translate("Form", "地区", None, -1))
        self.label_4.setText(QtWidgets.QApplication.translate("Form", "生日", None, -1))
        self.label_5.setText(QtWidgets.QApplication.translate("Form", "性别", None, -1))
        self.btnQuery.setText(QtWidgets.QApplication.translate("Form", "查询", None, -1))
        self.btnClear.setText(QtWidgets.QApplication.translate("Form", "清除", None, -1))

