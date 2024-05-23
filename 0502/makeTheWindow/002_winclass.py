import sys
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *

class MyWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setGeometry(100, 200, 400, 300)
        self.setWindowTitle("PyQt겅부듕")
        self.setWindowIcon(QIcon("d:/ai_exam/python_exam/0502/makeTheWindow/pavicon.png"))
       
        btn = QPushButton("나버튼", self)
        btn.clicked.connect(self.btn_click)
    def btn_click(self):
        print("눌럿넴?")

app = QApplication(sys.argv)

windowMain = MyWindow()
windowMain.show()

app.exec_()