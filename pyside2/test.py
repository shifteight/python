import sys
from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *

class Window(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()
    
    def initUI(self):
        self.setWindowTitle("老子是标题")
        self.resize(300, 300)
        self.move(500, 200)
        self.show()

if __name__ == '__main__':
    app = QApplication(sys.argv)
    test = Window()
    sys.exit(app.exec_())