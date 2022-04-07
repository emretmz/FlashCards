import sys
from PyQt5 import QtWidgets
from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *
import json
import os

from MainMenu import GetMenuFrame
from Levels import  Get_LevelPage
from GamePage import  Get_GamePage
from leveldesign import level_word 

class Ui_widget_Login(object):
    def setupUi(self, Login):
        if not Login.objectName():
            Login.setObjectName(u"Login")
        Login.resize(479, 560)
        self.frame_login = QFrame(Login)
        self.frame_login.setObjectName(u"frame_login")
        self.frame_login.setGeometry(QRect(10, 10, 461, 540))
        self.frame_login.setStyleSheet(u"background-color: rgb(35, 35, 35);\n"
"font: 75 10pt \"Yu Gothic UI\";\n"
"border-radius:20px;")
        self.frame_login.setFrameShape(QFrame.StyledPanel)
        self.frame_login.setFrameShadow(QFrame.Raised)
        self.label_login = QLabel(self.frame_login)
        self.label_login.setObjectName(u"label_login")
        self.label_login.setGeometry(QRect(60, 60, 351, 41))
        self.label_login.setStyleSheet(u"color:white;\n"
"font: 75 11pt \"Yu Gothic UI\";\n"
"\n"
"")
        self.button_login = QPushButton(self.frame_login)
        self.button_login.setObjectName(u"button_login")
        self.button_login.setGeometry(QRect(50, 310, 361, 81))
        self.button_login.setStyleSheet(u"QPushButton{background-color: rgb(58, 58, 58);\n"
"color:white;\n"
"border:none;\n"
"border-radius:20px;}\n"
"QPushButton::hover{\n"
"color:red;}")
        self.button_login.setCursor(QCursor(Qt.PointingHandCursor))
        self.button_signup = QPushButton(self.frame_login)
        self.button_signup.setObjectName(u"button_signup")
        self.button_signup.setGeometry(QRect(50, 410, 361, 81))
        self.button_signup.setStyleSheet(u"QPushButton{background-color: rgb(58, 58, 58);\n"
"color:white;\n"
"border:none;\n"
"border-radius:20px;}\n"
"QPushButton::hover{\n"
"color:red;}")
        self.button_signup.setCursor(QCursor(Qt.PointingHandCursor))
        self.label_username = QLabel(self.frame_login)
        self.label_username.setObjectName(u"label_username")
        self.label_username.setGeometry(QRect(60, 140, 111, 21))
        self.line_login = QLineEdit(self.frame_login)
        self.line_login.setObjectName(u"line_login")
        self.line_login.setGeometry(QRect(50, 180, 351, 51))
        self.line_login.setStyleSheet(u"color:white;\n"
"background-color: rgb(58, 58, 58);\n"
"padding-left:10px;")

        self.label_usercontrol = QLabel(self.frame_login)
        self.label_usercontrol.setObjectName(u"label_usercontrol")
        self.label_usercontrol.setGeometry(QRect(60, 250, 341, 31))
        self.label_usercontrol.setStyleSheet(u"color:red;")
        self.retranslateUi(Login)
        QMetaObject.connectSlotsByName(Login)
    #setupUi
    def retranslateUi(self, Login):
        Login.setWindowTitle(QCoreApplication.translate("Login", u"FLASHCARDS FOR DUTCH LEARNING", None))
        self.label_login.setText(QCoreApplication.translate("Login", u"Learn the 500 most used Dutch words easily!", None))
        self.button_login.setText(QCoreApplication.translate("Login", u"LOG IN", None))
        self.button_signup.setText(QCoreApplication.translate("Login", u"SIGN UP", None))
        self.label_username.setText(QCoreApplication.translate("Login", u"Username", None))
        self.label_usercontrol.setText(QCoreApplication.translate("Login", u"Username Control", None))
    #retranslateUi
filename = 'C:/Users/conko/OneDrive/Desktop/FlashCards/FlashCards_Team1/Loginsystem.json'
listObj =[]
if os.stat(filename).st_size == 0:
    with open(filename, 'r+') as json_file:
        json.dump(listObj, json_file)
else:
    print('File is not empty')

class Login_Page(QWidget, Ui_widget_Login):
        def __init__(self):

                super(Login_Page,self).__init__()
                self.setupUi(self)
                self.button_login.clicked.connect(self.Login_pressed)
                self.button_signup.clicked.connect(self.Register_pressed)
                self.username="emre"
    

        def Login_pressed(self): 
                username_list=[]               
                #self.username=Ui_widget_Login.line_login.text()##############
                print(self.label_usercontrol.text)


                with open('C:/Users/conko/OneDrive/Desktop/FlashCards/FlashCards_Team1/Loginsystem.json', 'r', encoding="utf-8") as f:
                        readable = json.load(f)
                        for x in readable:
                                username_list.append(x["username"])
                                #print(username_list)
                        self.username = self.line_login.text()
                        print(self.username)
                        if self.username in username_list:
                                print("Menüye gecis yapabilirsiniz")
                                self.label_usercontrol.setText("Succesfully Logined!")
                        else:
                                self.label_usercontrol.setText("Wrong Username!")
                        
        def Register_pressed(self):
        
                self.username = self.line_login.text()
        
                with open(filename, 'r+', encoding="utf-8") as file:
                        readable = file.read()
                        lines = readable.split('\"')
                        user = list(filter(lambda x: x == self.username or x ==
                                        self.username.lower() or x == self.username.upper(), lines))
            
                        if not user:
                                with open(filename, "r") as file:
                                        data = json.load(file)
                                        data.append({
                                                "username": self.username,
                                                "level": 0
                                                })
                                
                                with open(filename, "w") as file:
                                        json.dump(data, file)
                                        self.label_usercontrol.setText("Succesfully registered. Please login!")
                        else:
                                self.label_usercontrol.setText("Invalid! Please enter another Username!")



if __name__ == "__main__":
 
        import sys
        app = QApplication(sys.argv)
        mylogin= Login_Page()
        mylogin.show()
        sys.exit(app.exec_())
