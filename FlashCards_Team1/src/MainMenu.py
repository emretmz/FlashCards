from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *
 
from cdialog import CustomDialog


class Ui_widget_menu(object):
    def setupUi(self, widget_menu):
            
        if not widget_menu.objectName():
            widget_menu.setObjectName(u"widget_menu")
        widget_menu.resize(481, 541)
        self.frame_menu = QFrame(widget_menu)
        self.frame_menu.setObjectName(u"frame_menu")
        self.frame_menu.setGeometry(QRect(10, 10, 461, 521))
        self.frame_menu.setStyleSheet(u"background-color: rgb(35, 35, 35);\n"
"font: 75 10pt \"Yu Gothic UI\";\n"
"border-radius:20px;")
        self.frame_menu.setFrameShape(QFrame.StyledPanel)
        self.frame_menu.setFrameShadow(QFrame.Raised)
        self.label_menu = QLabel(self.frame_menu)
        self.label_menu.setObjectName(u"label_menu")
        self.label_menu.setGeometry(QRect(150, 40, 161, 41))
        self.label_menu.setStyleSheet(u"color:white;\n"
"font: 75 11pt \"Yu Gothic UI\";\n"
"\n"
"")
        self.button_play = QPushButton(self.frame_menu)
        self.button_play.setObjectName(u"button_play")
        self.button_play.setGeometry(QRect(50, 110, 361, 81))
        self.button_play.setStyleSheet(u"QPushButton{background-color: rgb(58, 58, 58);\n"
"color:white;\n"
"border:none;\n"
"border-radius:20px;}\n"
"QPushButton::hover{\n"
"color:red;}")
        self.button_levels = QPushButton(self.frame_menu)
        self.button_levels.setObjectName(u"button_levels")
        self.button_levels.setGeometry(QRect(50, 210, 361, 81))
        self.button_levels.setStyleSheet(u"QPushButton{background-color: rgb(58, 58, 58);\n"
"color:white;\n"
"border:none;\n"
"border-radius:20px;}\n"
"QPushButton::hover{\n"
"color:red;}")
        self.button_yourlevel = QPushButton(self.frame_menu)
        self.button_yourlevel.setObjectName(u"button_yourlevel")
        self.button_yourlevel.setGeometry(QRect(50, 310, 361, 81))
        self.button_yourlevel.setStyleSheet(u"QPushButton{background-color: rgb(58, 58, 58);\n"
"color:white;\n"
"border:none;\n"
"border-radius:20px;}\n"
"QPushButton::hover{\n"
"color:red;}")
        self.button_exit = QPushButton(self.frame_menu)
        self.button_exit.setObjectName(u"button_exit")
        self.button_exit.setGeometry(QRect(50, 410, 361, 81))
        self.button_exit.setStyleSheet(u"QPushButton{background-color: rgb(58, 58, 58);\n"
"color:white;\n"
"border:none;\n"
"border-radius:20px;}\n"
"QPushButton::hover{\n"
"color:red;}")

        self.retranslateUi(widget_menu)

        QMetaObject.connectSlotsByName(widget_menu)
    # setupUi

    def retranslateUi(self, widget_menu):
        widget_menu.setWindowTitle(QCoreApplication.translate("widget_menu", u"FLASHCARDS FOR DUTCH LEARNING", None))
        self.label_menu.setText(QCoreApplication.translate("widget_menu", u"Welcome Username", None))
        self.button_play.setText(QCoreApplication.translate("widget_menu", u"PLAY", None))
        self.button_levels.setText(QCoreApplication.translate("widget_menu", u"LEVELS", None))
        self.button_yourlevel.setText(QCoreApplication.translate("widget_menu", u"YOUR LEVEL", None))
        self.button_exit.setText(QCoreApplication.translate("widget_menu", u"EXIT", None))
    # retranslateUi

class GetMenuFrame(QWidget, Ui_widget_menu):
    def __init__(self):
        super(GetMenuFrame,self).__init__()
        self.setupUi(self)

        self.button_yourlevel.clicked.connect(self.YLevel_Pressed)
 

    def YLevel_Pressed(self):
 
        dlg = CustomDialog()
        if dlg.exec_():
            print("Success!")
        else:
            print("Cancel!")

    def Exit_Pressed(self):
            sys.exit()

 
if __name__ == "__main__":
        import sys
        app = QApplication(sys.argv)
        GetMenu= GetMenuFrame()
        GetMenu.show()
        sys.exit(app.exec_())