from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *
import pandas as pd
import json

class Ui_widget_levels(object):
    def setupUi(self, widget_levels):
        if not widget_levels.objectName():
            widget_levels.setObjectName(u"widget_levels")
        widget_levels.resize(477, 548)
        self.frame_levels = QFrame(widget_levels)
        self.frame_levels.setObjectName(u"frame_levels")
        self.frame_levels.setGeometry(QRect(10, 0, 461, 541))
        self.frame_levels.setStyleSheet(u"background-color: rgb(35, 35, 35);\n"
"font: 75 10pt \"Yu Gothic UI\";\n"
"border-radius:20px;")
        self.frame_levels.setFrameShape(QFrame.StyledPanel)
        self.frame_levels.setFrameShadow(QFrame.Raised)
        self.label_levels = QLabel(self.frame_levels)
        self.label_levels.setObjectName(u"label_levels")
        self.label_levels.setGeometry(QRect(180, 40, 100, 41))
        self.label_levels.setStyleSheet(u"color:white;\n"
"font: 75 20pt \"Yu Gothic UI\";\n"
"\n"
"")
        self.button_lvl_back = QPushButton(self.frame_levels)
        self.button_lvl_back.setObjectName(u"button_back")
        self.button_lvl_back.setGeometry(QRect(50, 20, 111, 41))
        self.button_lvl_back.setStyleSheet(u"QPushButton{background-color: rgb(58, 58, 58);\n"
"color:white;\n"
"border:none;\n"
"border-radius:20px;}\n"
"QPushButton::hover{\n"
"color:red;}")

        self.gridLayoutWidget = QWidget(self.frame_levels)
        self.gridLayoutWidget.setObjectName(u"gridLayoutWidget")
        self.gridLayoutWidget.setGeometry(QRect(40, 100, 191, 401))
        self.gridLayout_levels_left = QGridLayout(self.gridLayoutWidget)
        self.gridLayout_levels_left.setObjectName(u"gridLayout_levels_left")
        self.gridLayout_levels_left.setContentsMargins(0, 0, 0, 0)
        self.button_level1 = QPushButton(self.gridLayoutWidget)
        self.button_level1.setObjectName(u"button_level1")
        self.button_level1.setStyleSheet(u"QPushButton{background-color: rgb(58, 58, 58);\n"
"color:white;\n"
"border:none;\n"
"border-radius:20px;}\n"
"QPushButton::hover{\n"
"color:red;}")

        self.gridLayout_levels_left.addWidget(self.button_level1, 0, 0, 1, 1)

        self.button_level7 = QPushButton(self.gridLayoutWidget)
        self.button_level7.setObjectName(u"button_level7")
        self.button_level7.setStyleSheet(u"QPushButton{background-color: rgb(58, 58, 58);\n"
"color:white;\n"
"border:none;\n"
"border-radius:20px;}\n"
"QPushButton::hover{\n"
"color:red;}")

        self.gridLayout_levels_left.addWidget(self.button_level7, 6, 0, 1, 1)

        self.button_level6 = QPushButton(self.gridLayoutWidget)
        self.button_level6.setObjectName(u"button_level6")
        self.button_level6.setStyleSheet(u"QPushButton{background-color: rgb(58, 58, 58);\n"
"color:white;\n"
"border:none;\n"
"border-radius:20px;}\n"
"QPushButton::hover{\n"
"color:red;}")

        self.gridLayout_levels_left.addWidget(self.button_level6, 5, 0, 1, 1)

        self.button_level10 = QPushButton(self.gridLayoutWidget)
        self.button_level10.setObjectName(u"button_level10")
        self.button_level10.setStyleSheet(u"QPushButton{background-color: rgb(58, 58, 58);\n"
"color:white;\n"
"border:none;\n"
"border-radius:20px;}\n"
"QPushButton::hover{\n"
"color:red;}")

        self.gridLayout_levels_left.addWidget(self.button_level10, 9, 0, 1, 1)

        self.button_level3 = QPushButton(self.gridLayoutWidget)
        self.button_level3.setObjectName(u"button_level3")
        self.button_level3.setStyleSheet(u"QPushButton{background-color: rgb(58, 58, 58);\n"
"color:white;\n"
"border:none;\n"
"border-radius:20px;}\n"
"QPushButton::hover{\n"
"color:red;}")

        self.gridLayout_levels_left.addWidget(self.button_level3, 2, 0, 1, 1)

        self.button_level2 = QPushButton(self.gridLayoutWidget)
        self.button_level2.setObjectName(u"button_level2")
        self.button_level2.setStyleSheet(u"QPushButton{background-color: rgb(58, 58, 58);\n"
"color:white;\n"
"border:none;\n"
"border-radius:20px;}\n"
"QPushButton::hover{\n"
"color:red;}")

        self.gridLayout_levels_left.addWidget(self.button_level2, 1, 0, 1, 1)

        self.button_level4 = QPushButton(self.gridLayoutWidget)
        self.button_level4.setObjectName(u"button_level4")
        self.button_level4.setStyleSheet(u"QPushButton{background-color: rgb(58, 58, 58);\n"
"color:white;\n"
"border:none;\n"
"border-radius:20px;}\n"
"QPushButton::hover{\n"
"color:red;}")

        self.gridLayout_levels_left.addWidget(self.button_level4, 3, 0, 1, 1)

        self.button_level8 = QPushButton(self.gridLayoutWidget)
        self.button_level8.setObjectName(u"button_level8")
        self.button_level8.setStyleSheet(u"QPushButton{background-color: rgb(58, 58, 58);\n"
"color:white;\n"
"border:none;\n"
"border-radius:20px;}\n"
"QPushButton::hover{\n"
"color:red;}")

        self.gridLayout_levels_left.addWidget(self.button_level8, 7, 0, 1, 1)

        self.button_level9 = QPushButton(self.gridLayoutWidget)
        self.button_level9.setObjectName(u"button_level9")
        self.button_level9.setStyleSheet(u"QPushButton{background-color: rgb(58, 58, 58);\n"
"color:white;\n"
"border:none;\n"
"border-radius:20px;}\n"
"QPushButton::hover{\n"
"color:red;}")

        self.gridLayout_levels_left.addWidget(self.button_level9, 8, 0, 1, 1)

        self.button_level5 = QPushButton(self.gridLayoutWidget)
        self.button_level5.setObjectName(u"button_level5")
        self.button_level5.setStyleSheet(u"QPushButton{background-color: rgb(58, 58, 58);\n"
"color:white;\n"
"border:none;\n"
"border-radius:20px;}\n"
"QPushButton::hover{\n"
"color:red;}")

        self.gridLayout_levels_left.addWidget(self.button_level5, 4, 0, 1, 1)

        self.gridLayoutWidget_2 = QWidget(self.frame_levels)
        self.gridLayoutWidget_2.setObjectName(u"gridLayoutWidget_2")
        self.gridLayoutWidget_2.setGeometry(QRect(240, 100, 181, 401))
        self.gridLayout_levels_right = QGridLayout(self.gridLayoutWidget_2)
        self.gridLayout_levels_right.setObjectName(u"gridLayout_levels_right")
        self.gridLayout_levels_right.setContentsMargins(0, 0, 0, 0)
        self.button_level20 = QPushButton(self.gridLayoutWidget_2)
        self.button_level20.setObjectName(u"button_level20")
        self.button_level20.setStyleSheet(u"QPushButton{background-color: rgb(58, 58, 58);\n"
"color:white;\n"
"border:none;\n"
"border-radius:20px;}\n"
"QPushButton::hover{\n"
"color:red;}")

        self.gridLayout_levels_right.addWidget(self.button_level20, 9, 0, 1, 1)

        self.button_level19 = QPushButton(self.gridLayoutWidget_2)
        self.button_level19.setObjectName(u"button_level19")
        self.button_level19.setStyleSheet(u"QPushButton{background-color: rgb(58, 58, 58);\n"
"color:white;\n"
"border:none;\n"
"border-radius:20px;}\n"
"QPushButton::hover{\n"
"color:red;}")

        self.gridLayout_levels_right.addWidget(self.button_level19, 8, 0, 1, 1)

        self.button_level12 = QPushButton(self.gridLayoutWidget_2)
        self.button_level12.setObjectName(u"button_level12")
        self.button_level12.setStyleSheet(u"QPushButton{background-color: rgb(58, 58, 58);\n"
"color:white;\n"
"border:none;\n"
"border-radius:20px;}\n"
"QPushButton::hover{\n"
"color:red;}")

        self.gridLayout_levels_right.addWidget(self.button_level12, 1, 0, 1, 1)

        self.button_level11 = QPushButton(self.gridLayoutWidget_2)
        self.button_level11.setObjectName(u"button_level11")
        self.button_level11.setStyleSheet(u"QPushButton{background-color: rgb(58, 58, 58);\n"
"color:white;\n"
"border:none;\n"
"border-radius:20px;}\n"
"QPushButton::hover{\n"
"color:red;}")

        self.gridLayout_levels_right.addWidget(self.button_level11, 0, 0, 1, 1)

        self.button_level14 = QPushButton(self.gridLayoutWidget_2)
        self.button_level14.setObjectName(u"button_level14")
        self.button_level14.setStyleSheet(u"QPushButton{background-color: rgb(58, 58, 58);\n"
"color:white;\n"
"border:none;\n"
"border-radius:20px;}\n"
"QPushButton::hover{\n"
"color:red;}")

        self.gridLayout_levels_right.addWidget(self.button_level14, 3, 0, 1, 1)

        self.button_level17 = QPushButton(self.gridLayoutWidget_2)
        self.button_level17.setObjectName(u"button_level17")
        self.button_level17.setStyleSheet(u"QPushButton{background-color: rgb(58, 58, 58);\n"
"color:white;\n"
"border:none;\n"
"border-radius:20px;}\n"
"QPushButton::hover{\n"
"color:red;}")

        self.gridLayout_levels_right.addWidget(self.button_level17, 6, 0, 1, 1)

        self.button_level18 = QPushButton(self.gridLayoutWidget_2)
        self.button_level18.setObjectName(u"button_level18")
        self.button_level18.setStyleSheet(u"QPushButton{background-color: rgb(58, 58, 58);\n"
"color:white;\n"
"border:none;\n"
"border-radius:20px;}\n"
"QPushButton::hover{\n"
"color:red;}")

        self.gridLayout_levels_right.addWidget(self.button_level18, 7, 0, 1, 1)
        self.button_level13 = QPushButton(self.gridLayoutWidget_2)
        self.button_level13.setObjectName(u"button_level13")
        self.button_level13.setStyleSheet(u"QPushButton{background-color: rgb(58, 58, 58);\n"
"color:white;\n"
"border:none;\n"
"border-radius:20px;}\n"
"QPushButton::hover{\n"
"color:red;}")

        self.gridLayout_levels_right.addWidget(self.button_level13, 2, 0, 1, 1)

        self.button_level16 = QPushButton(self.gridLayoutWidget_2)
        self.button_level16.setObjectName(u"button_level16")
        self.button_level16.setStyleSheet(u"QPushButton{background-color: rgb(58, 58, 58);\n"
"color:white;\n"
"border:none;\n"
"border-radius:20px;}\n"
"QPushButton::hover{\n"
"color:red;}")

        self.gridLayout_levels_right.addWidget(self.button_level16, 5, 0, 1, 1)

        self.button_level15 = QPushButton(self.gridLayoutWidget_2)
        self.button_level15.setObjectName(u"button_level15")
        self.button_level15.setStyleSheet(u"QPushButton{background-color: rgb(58, 58, 58);\n"
"color:white;\n"
"border:none;\n"
"border-radius:20px;}\n"
"QPushButton::hover{\n"
"color:red;}")

        self.gridLayout_levels_right.addWidget(self.button_level15, 4, 0, 1, 1)
        self.retranslateUi(widget_levels)

        QMetaObject.connectSlotsByName(widget_levels)
    # setupUi

    def retranslateUi(self, widget_levels):
        widget_levels.setWindowTitle(QCoreApplication.translate("widget_levels", u"FLASHCARDS FOR DUTCH LEARNING", None))

        self.button_lvl_back.setText(QCoreApplication.translate("widget_game", u"BACK", None))   
        self.label_levels.setText(QCoreApplication.translate("widget_levels", u"LEVELS", None))
        self.button_level1.setText(QCoreApplication.translate("widget_levels", u"LEVEL 1", None))
        self.button_level7.setText(QCoreApplication.translate("widget_levels", u"LEVEL 7", None))
        self.button_level6.setText(QCoreApplication.translate("widget_levels", u"LEVEL 6", None))
        self.button_level10.setText(QCoreApplication.translate("widget_levels", u"LEVEL 10", None))
        self.button_level3.setText(QCoreApplication.translate("widget_levels", u"LEVEL 3", None))
        self.button_level2.setText(QCoreApplication.translate("widget_levels", u"LEVEL 2", None))
        self.button_level4.setText(QCoreApplication.translate("widget_levels", u"LEVEL 4", None))
        self.button_level8.setText(QCoreApplication.translate("widget_levels", u"LEVEL 8", None))
        self.button_level9.setText(QCoreApplication.translate("widget_levels", u"LEVEL 9", None))
        self.button_level5.setText(QCoreApplication.translate("widget_levels", u"LEVEL 5", None))
        self.button_level20.setText(QCoreApplication.translate("widget_levels", u"LEVEL 20", None))
        self.button_level19.setText(QCoreApplication.translate("widget_levels", u"LEVEL 19", None))
        self.button_level12.setText(QCoreApplication.translate("widget_levels", u"LEVEL 12", None))
        self.button_level11.setText(QCoreApplication.translate("widget_levels", u"LEVEL 11", None))
        self.button_level14.setText(QCoreApplication.translate("widget_levels", u"LEVEL 14", None))
        self.button_level17.setText(QCoreApplication.translate("widget_levels", u"LEVEL 17", None))
        self.button_level18.setText(QCoreApplication.translate("widget_levels", u"LEVEL 18", None))
        self.button_level13.setText(QCoreApplication.translate("widget_levels", u"LEVEL 13", None))
        self.button_level16.setText(QCoreApplication.translate("widget_levels", u"LEVEL 16", None))
        self.button_level15.setText(QCoreApplication.translate("widget_levels", u"LEVEL 15", None)) 
    # retranslateUi
class Get_LevelPage(QWidget, Ui_widget_levels):
    def __init__(self):
        super(Get_LevelPage,self).__init__()
        self.setupUi(self)
        """  
        self.df=pd.read_json("C:/Users/conko/OneDrive/Desktop/FlashCards/FlashCards_Team1/translatedCards.json")
        self.button_level1.clicked.connect(self.button_level1_Pressed)
        self.button_level2.clicked.connect(self.button_level2_Pressed)
        self.button_level3.clicked.connect(self.button_level3_Pressed)
        self.button_level4.clicked.connect(self.button_level4_Pressed)
        self.button_level5.clicked.connect(self.button_level5_Pressed)
        self.button_level6.clicked.connect(self.button_level6_Pressed)
        self.button_level7.clicked.connect(self.button_level7_Pressed)
        self.button_level8.clicked.connect(self.button_level8_Pressed)
        self.button_level9.clicked.connect(self.button_level9_Pressed)
        self.button_level10.clicked.connect(self.button_level10_Pressed)
        self.button_level11.clicked.connect(self.button_level11_Pressed)
        self.button_level12.clicked.connect(self.button_level12_Pressed)
        self.button_level13.clicked.connect(self.button_level13_Pressed)
        self.button_level14.clicked.connect(self.button_level14_Pressed)
        self.button_level15.clicked.connect(self.button_level15_Pressed)
        self.button_level16.clicked.connect(self.button_level16_Pressed)
        self.button_level17.clicked.connect(self.button_level17_Pressed)
        self.button_level18.clicked.connect(self.button_level18_Pressed)
        self.button_level19.clicked.connect(self.button_level19_Pressed)
        self.button_level20.clicked.connect(self.button_level20_Pressed)

    
    def button_level1_Pressed(self):
        print(self.df[self.df['Unnamed: 0']=='Level1']['Nederlands'])
    def button_level2_Pressed(self):
        print(self.df[self.df['Unnamed: 0']=='Level2']['Nederlands'])
    def button_level3_Pressed(self):
        print(self.df[self.df['Unnamed: 0']=='Level3']['Nederlands'])
    def button_level4_Pressed(self):
        print(self.df[self.df['Unnamed: 0']=='Level4']['Nederlands'])
    def button_level5_Pressed(self):
        print(self.df[self.df['Unnamed: 0']=='Level5']['Nederlands'])
    def button_level6_Pressed(self):
        print(self.df[self.df['Unnamed: 0']=='Level6']['Nederlands'])
    def button_level7_Pressed(self):
        print(self.df[self.df['Unnamed: 0']=='Level7']['Nederlands'])
    def button_level8_Pressed(self):
        print(self.df[self.df['Unnamed: 0']=='Level8']['Nederlands'])
    def button_level9_Pressed(self):
        print(self.df[self.df['Unnamed: 0']=='Level9']['Nederlands'])                                
    def button_level10_Pressed(self):
        print(self.df[self.df['Unnamed: 0']=='Level10']['Nederlands'])
    def button_level11_Pressed(self):
        print(self.df[self.df['Unnamed: 0']=='Level11']['Nederlands'])
    def button_level12_Pressed(self):
        print(self.df[self.df['Unnamed: 0']=='Level12']['Nederlands'])
    def button_level13_Pressed(self):
        print(self.df[self.df['Unnamed: 0']=='Level13']['Nederlands'])
    def button_level14_Pressed(self):
        print(self.df[self.df['Unnamed: 0']=='Level14']['Nederlands'])
    def button_level15_Pressed(self):
        print(self.df[self.df['Unnamed: 0']=='Level15']['Nederlands'])
    def button_level16_Pressed(self):
        print(self.df[self.df['Unnamed: 0']=='Level16']['Nederlands'])
    def button_level17_Pressed(self):
        print(self.df[self.df['Unnamed: 0']=='Level17']['Nederlands'])
    def button_level18_Pressed(self):
        print(self.df[self.df['Unnamed: 0']=='Level18']['Nederlands']) 
    def button_level19_Pressed(self):
        print(self.df[self.df['Unnamed: 0']=='Level19']['Nederlands'])
    def button_level20_Pressed(self):
        print(self.df[self.df['Unnamed: 0']=='Level20']['Nederlands']) 
         """
if __name__ == "__main__":
    import sys
    app = QApplication(sys.argv)
    Get_LevelPage= Get_LevelPage()
    Get_LevelPage.show()
    sys.exit(app.exec_())
