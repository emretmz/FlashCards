from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *

class CustomDialog(QDialog):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Info!")
        self.layout = QVBoxLayout()
        message = QLabel( "Player:  Level:   Avg Time:  ")
        self.setStyleSheet(u"background-color: rgb(35, 35, 35);\n"
        "color:white;\n"
        "font: 75 10pt \"Yu Gothic UI\";\n"
        "border-radius:20px;")
        self.layout.addWidget(message)
        self.setLayout(self.layout)
