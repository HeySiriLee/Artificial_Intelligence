import sys
from PyQt5.QtWidgets import *
from PyQt5 import uic

form_main = uic.loadUiType("main.ui")[0]

class MyWindow(QMainWindow, form_main):
    searchText = ""

    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.btn1.clicked.connect(self.btn1_clicked)
        self.btn2.clicked.connect(self.btn2_clicked)

        self.btnSearch.clicked.connect(self.btnSearch_clicked)

    def btnSearch_clicked(self):
        self.searchText = self.lbSearch.text()
        QMessageBox.about(
            self, 
            "Search", 
            f"'{self.searchText}' 를 검색햇넹"
            )
        # print(self.lbSearch.text())

    def btn1_clicked(self):
        # print("1클릭함")
        QMessageBox.about(self, "Message", "버튼1눌려ㄸr!")
    def btn2_clicked(self):
        # print("2클릭함")
        btnQa = QMessageBox.information(
            self,
            "Delete",
            "지우고시펑?",
            QMessageBox.Yes | QMessageBox.Cancel
        )

        if btnQa == QMessageBox.Yes:
            QMessageBox.about(self, "Complete", "삭제완룡")
        if btnQa == QMessageBox.Cancel:
            QMessageBox.about(self, "Cancle", "삭제취숑")

app = QApplication(sys.argv)

window = MyWindow()
window.show()

app.exec_()