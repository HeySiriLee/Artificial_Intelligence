import sys

from PyQt5.QtWidgets import *
from PyQt5 import uic
from mem_add import MemAddMain

mem_main = uic.loadUiType("ui/main.ui")[0]

class MyWindow(QMainWindow, mem_main):

    def __init__(self):
        super().__init__()
        self.setupUi(self)

        self.btnSearch.clicked.connect(self.btnSearch_clicked)
        self.btnClose.clicked.connect(self.btnClose_clicked)

        self.btnAdd.clicked.connect(self.btnAdd_clicked)
        self.btnEdit.clicked.connect(self.btnEdit_clicked)
        self.btnDelete.clicked.connect(self.btnDelete_clicked)

    def btnSearch_clicked(self):
        print("Click the Search")

    def btnClose_clicked(self):
        exit()

    def btnAdd_clicked(self):
        mem_add_main = MemAddMain()
        mem_add_main.showmodal()
        print("Add")

    def btnEdit_clicked(self):
        print("Edit")

    def btnDelete_clicked(self):
        print("Delete")

app = QApplication(sys.argv)

window = MyWindow()
window.show()

app.exec_()