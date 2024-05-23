import sys

# PyQt5.QtWidgets: Window core
from PyQt5.QtWidgets import *

# Window creation command
app = QApplication(sys.argv)

btn = QPushButton("아임푸시버튼")
btn.show()

# It is activated until the user presses the end button.
app.exec_()