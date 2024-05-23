import sys

from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from PyQt5 import uic

from memdb_edit import MemDbEdit

memEditMain = uic.loadUiType("ui/mem_edit.ui")[0]

class MemEditMain(QDialog, memEditMain):
    def __init__(self):
        super().__init__()
        self.setupUi(self)

        self.btnEdit.clicked.connect(self.btnEdit_clicked)
        self.btnClose.clicked.connect(self.btnClose_clicked)
    
    def loadData (self, idx, mail, name, telno, addrs, sns):
        self.editIdx = idx
        self.leMail.setText(mail)
        self.leName.setText(name)
        self.lePhone.setText(telno)
        self.leAddrs.setText(addrs)
        self.leSns.setText(sns)

    def btnEdit_clicked(self):
        if self.leMail.text() == "":
            QMessageBox.about(self, "Input error", "Enter the u r email!")
        if self.leName.text() == "":
            QMessageBox.about(self, "Input error", "Enter the u r name!")
        if self.lePhone.text() == "":
            QMessageBox.about(self, "Input error", "Enter the u r phone number!")
            return
        
        # Save a data
        try:
            MemDbEdit(
                self.editIdx,
                self.leMail.text(),
                self.leName.text(),
                self.lePhone.text(),
                self.leAddrs.text(),
                self.leSns.text()
            )
            QMessageBox.about(self, "Completed register", "Success the register!")
        except:
            QMessageBox.about(self, "Input error", "Database Error")
    
    def btnClose_clicked(self):
        self.close()

    def showModal(self):
        return super().exec_()