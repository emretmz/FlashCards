# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'designerSioVku.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *
import pandas as pd

url="C:/Users/conko/OneDrive/Desktop/FlashCards/FlashCards_Team1/translatedCards.json"
df=pd.read_json(url)


class Ui_widget_levelWords(object):
    def setupUi(self, widget_levelWords):
        if not widget_levelWords.objectName():
            widget_levelWords.setObjectName(u"widget_levelWords")
        self.frame_levelWords = QFrame(widget_levelWords)
        self.frame_levelWords.setObjectName(u"frame_levelWords")
        self.frame_levelWords.setGeometry(QRect(10, 10, 441, 551))
        self.frame_levelWords.setStyleSheet(u"background-color: rgb(35, 35, 35);\n"
"font: 75 10pt \\Yu Gothic UI;\n"
"border-radius:20px")
        self.frame_levelWords.setFrameShape(QFrame.StyledPanel)
        self.frame_levelWords.setFrameShadow(QFrame.Raised)
        self.label_1 = QLabel(self.frame_levelWords)
        self.label_1.setObjectName(u"label_1")
        self.label_1.setGeometry(QRect(30, 60, 181, 441))
        self.label_1.setStyleSheet(u"background-color: rgb(83, 83, 83);\n"
"font: 75 12pt \"Yu Gothic UI\";")
        self.label_1.setAlignment(Qt.AlignCenter)
        self.label_2 = QLabel(self.frame_levelWords)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setGeometry(QRect(230, 60, 181, 441))
        self.label_2.setStyleSheet(u"background-color: rgb(83, 83, 83);\n"
"font: 75 12pt \"Yu Gothic UI\";")
        self.label_2.setAlignment(Qt.AlignCenter)
        self.retranslateUi(widget_levelWords)
        QMetaObject.connectSlotsByName(widget_levelWords)
    # setupUi
    def retranslateUi(self, widget_levelWords):
        widget_levelWords.setWindowTitle(QCoreApplication.translate("widget_levelWords", u"Form", None))
        self.label_1.setText(QCoreApplication.translate("widget_levelWords", u"10 kelime", None))
        self.label_2.setText(QCoreApplication.translate("widget_levelWords", u"10 kelime", None))
    # retranslateUi


class level_word(QWidget, Ui_widget_levelWords):
        def __init__(self):
            super(level_word,self).__init__()
            self.setupUi(self)
            
        j=1    
        def words_pressed(self):
            url="C:/Users/conko/OneDrive/Desktop/FlashCards/FlashCards_Team1/translatedCards.json"
            df=pd.read_json(url)
            ten_words=[]
            ten_words2=[]
            
                
            for i in range(20):                   
                a=df["Nederlands"][f"('Level{self.j}', '{i}')"]
                print(a)
                if i<10:
                    ten_words.append(a)
                    self.label_1.setText("\n".join(ten_words))
                #a=str(ten_words)        
                #self.label_1.setText(a) 
                else :           
                    ten_words2.append(a)
                    self.label_2.setText("\n".join(ten_words2)) 
                    
            return None 
            

if __name__ == "__main__":
    import sys
    app = QApplication(sys.argv)
    level_words= level_word()
    level_words.show()
    sys.exit(app.exec_())
