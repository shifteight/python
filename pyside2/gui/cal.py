import sys
from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *
from Ui_cal import Ui_Form

class Test_Form(QDialog):
    def __init__(self, parent=None):
        QDialog.__init__(self, parent)
        self.ui = Ui_Form()
        self.ui.setupUi(self)

if __name__ == '__main__':
    app =QApplication(sys.argv)
    form = Test_Form()
    form.show()
    sys.exit(app.exec_())