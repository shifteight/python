# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '/Users/kevin/Documents/Git/python/pyside2/gui/cal.ui',
# licensing of '/Users/kevin/Documents/Git/python/pyside2/gui/cal.ui' applies.
#
# Created: Sun May 26 23:05:12 2019
#      by: pyside2-uic  running on PySide2 5.12.3
#
# WARNING! All changes made in this file will be lost!

from PySide2 import QtCore, QtGui, QtWidgets

class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(477, 364)
        self.calendarWidget = QtWidgets.QCalendarWidget(Form)
        self.calendarWidget.setGeometry(QtCore.QRect(0, 0, 471, 361))
        self.calendarWidget.setObjectName("calendarWidget")

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        Form.setWindowTitle(QtWidgets.QApplication.translate("Form", "Form", None, -1))

