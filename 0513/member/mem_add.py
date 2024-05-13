import sys

from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from PyQt5 import uic

mem_add_main = uic.loadUiType("ui/mem_add.ui")[0]

class MemAddMain(QDialog, mem_add_main):
    def __init__(self):
        super().__init__()
        self.setupUi(self)

        self.btnClose_clicked.connect(self.btnClose_clicked)

    
    def btnClose_clicked(self):
        self.close()

    def showModal(self):
        return super().exec_()