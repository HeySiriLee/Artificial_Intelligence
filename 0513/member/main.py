import sys

from PyQt5.QtWidgets import *
from PyQt5 import uic

from mem_add import MemAddMain
from mem_edit import MemEditMain
from memdb_list import MemDbList
from memdb_del import MemDbDel

mem_main = uic.loadUiType("ui/main.ui")[0]

class MyWindow(QMainWindow, mem_main):
    deleteIdx = ""
    editIdx = ""
    editMail = ""
    editName = ""
    editTelno = ""
    editAddrs = ""
    editSns = ""

    def __init__(self):
        super().__init__()
        self.setupUi(self)

        self.btnSearch.clicked.connect(self.btnSearch_clicked)
        self.btnClose.clicked.connect(self.btnClose_clicked)

        self.btnAdd.clicked.connect(self.btnAdd_clicked)
        # self.tblMem.setEditTriggers(QAbstractItemView.AllEditTriggers)
        self.tblMem.cellClicked.connect(self.cellclicked_event)
        self.btnEdit.clicked.connect(self.btnEdit_clicked)
        self.btnDelete.clicked.connect(self.btnDelete_clicked)

        # Reset tblMem
        self.tblMem.setColumnCount(6)
        self.tblMem.setHorizontalHeaderLabels(
            ["Id", "Mail", "Name", "Telno", "Addrs", "SNS"]
        )
        self.deleteIdx = ""
            
    def btnSearch_clicked(self):
        datas = MemDbList(self.leSearch.text())
        print("Data size: ", len(datas))

        self.tblMem.setRowCount(len(datas))

        for idx, data in enumerate(datas):
            self.tblMem.setItem(idx, 0, QTableWidgetItem(str(data[0])))
            self.tblMem.setItem(idx, 1, QTableWidgetItem(data[1]))
            self.tblMem.setItem(idx, 2, QTableWidgetItem(data[2]))
            self.tblMem.setItem(idx, 3, QTableWidgetItem(data[3]))
            self.tblMem.setItem(idx, 4, QTableWidgetItem(data[4]))
            self.tblMem.setItem(idx, 5, QTableWidgetItem(data[5]))
            
    def btnClose_clicked(self):
        exit()

    def btnAdd_clicked(self):
        memAddMain = MemAddMain()
        memAddMain.showModal()
        self.btnSearch_clicked()

    def cellclicked_event(self, row, col):
        print(f"row: {row}, col: {col}")
        
        # Delete
        self.deleteIdx = self.tblMem.item(row, 0).text()
        print("idx: ", self.deleteIdx)

        # Edit
        self.editIdx   = self.tblMem.item(row, 0).text()
        self.editMail  = self.tblMem.item(row, 1).text()
        self.editName  = self.tblMem.item(row, 2).text()
        self.editTelno = self.tblMem.item(row, 3).text()
        self.editAddrs = self.tblMem.item(row, 4).text()
        self.editSns   = self.tblMem.item(row, 5).text()  

    def btnEdit_clicked(self):
        memEditMain = MemEditMain()
        memEditMain.loadData(
            self.editIdx,
            self.editMail,
            self.editName,
            self.editTelno,
            self.editAddrs,
            self.editSns,
        )
        memEditMain.showModal()
        self.btnSearch_clicked()

    def btnDelete_clicked(self):
        if not self.deleteIdx:
            QMessageBox.about(self, "Warning", "Please select a row to delete.")
            return

        if MemDbDel(self.deleteIdx) == True:
            QMessageBox.about(self, "Success", "Data deleted successfully!")
            self.btnSearch_clicked()  
        else:
            QMessageBox.about(self, "Error", "Failed to delete data. Please check the database.")

        self.deleteIdx = ""  

app = QApplication(sys.argv)
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

window = MyWindow()
window.show()

app.exec_()