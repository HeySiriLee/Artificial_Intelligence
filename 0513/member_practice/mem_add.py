import sys

from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from PyQt5 import uic

from memdb_add import MemDbAdd

memAddMain = uic.loadUiType("ui/mem_add.ui")[0]

class MemAddMain(QDialog, memAddMain):
    def __init__(self):
        super().__init__()
        self.setupUi(self)

        self.btnRes.clicked.connect(self.btnRes_clicked)
        self.btnClose.clicked.connect(self.btnClose_clicked)

    def btnRes_clicked(self):
        if self.leMail.text() == "":
            QMessageBox.about(self, "Input error", "Enter the u r email!")
        if self.leName.text() == "":
            QMessageBox.about(self, "Input error", "Enter the u r name!")
        if self.lePhone.text() == "":
            QMessageBox.about(self, "Input error", "Enter the u r phone number!")
            return
        
        # # Save a data
        # try:
        #     MemDbAdd(
        #     self.leMail.text(),
        #     self.leName.text(),
        #     self.lePhone.text(),
        #     self.leAddrs.text(),text
        #     self.leSns.text()
        #     )
        #     QMessageBox.about(self, "Completed register", "Success the register!")
        # except:
        #     QMessageBox.about(self, "Input error", "Database Error")
    
    def btnClose_clicked(self):
        self.close()

    def showModal(self):
        return super().exec_()