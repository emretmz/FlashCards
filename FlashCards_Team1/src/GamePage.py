from enum import unique
from turtle import update
from LoginPage import *
from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *
from PySide2.QtCore import QTimer
from PySide2.QtWidgets import QLCDNumber
import pandas as pd
import json


class Ui_widget_game(object):
    def setupUi(self, widget_game):
        if not widget_game.objectName():
            widget_game.setObjectName(u"widget_game")
        widget_game.resize(483, 550)
        self.frame_game = QFrame(widget_game)
        self.frame_game.setObjectName(u"frame_game")
        self.frame_game.setGeometry(QRect(10, 10, 461, 531))
        self.frame_game.setStyleSheet(u"background-color: rgb(35, 35, 35);\n"
"font: 75 10pt \"Yu Gothic UI\";\n"
"border-radius:20px;")
        self.frame_game.setFrameShape(QFrame.StyledPanel)
        self.frame_game.setFrameShadow(QFrame.Raised)
        self.label_card = QLabel(self.frame_game)
        self.label_card.setObjectName(u"label_card")

        self.label_card.setGeometry(QRect(50, 120, 361, 251))
        self.label_card.setStyleSheet(u"color:black;\n"
"background-color: rgb(83, 83, 83);\n"
"font: 75 20pt \"Yu Gothic UI\";\n"
"\n"
"")
        self.label_language = QLabel(self.frame_game)
        self.label_language.setObjectName(u"label_language")
        self.label_language.setGeometry(QRect(190, 70, 61, 41))
        self.label_language.setStyleSheet(u"color:white;\n"
"font: 75 11pt \"Yu Gothic UI\";\n"
"\n"
"")
        self.button_ok = QPushButton(self.frame_game)
        self.button_ok.setObjectName(u"button_ok")
        self.button_ok.setGeometry(QRect(60, 390, 161, 81))
        self.button_ok.setStyleSheet(u"background-color: white;\n"
"color: rgb(0, 0, 0);\n"
"font: 75 12pt \"Yu Gothic UI\";\n"
"border:none;\n"
"border-radius:20px;\n"
"")
        self.button_cancel = QPushButton(self.frame_game)
        self.button_cancel.setObjectName(u"button_cancel")
        self.button_cancel.setGeometry(QRect(240, 390, 161, 81))
        self.button_cancel.setStyleSheet(u"background-color:white;\n"
"font: 75 12pt \"Yu Gothic UI\";\n"
"color: rgb(0, 0, 0);\n"
"border:none;\n"
"border-radius:20px;\n"
"")
        self.label_time = QLabel(self.frame_game)
        self.label_time.setObjectName(u"label_language")
        self.label_time.setGeometry(QRect(367, 20, 71, 22))
        self.label_time.setStyleSheet(u"color:white;\n"
"font: 75 11pt \"Yu Gothic UI\";\n"
"\n"
"")
        self.button_back = QPushButton(self.frame_game)
        self.button_back.setObjectName(u"button_back")
        self.button_back.setGeometry(QRect(50, 20, 111, 41))
        self.button_back.setStyleSheet(u"QPushButton{background-color: rgb(58, 58, 58);\n"
"color:white;\n"
"border:none;\n"
"border-radius:20px;}\n"
"QPushButton::hover{\n"
"color:red;}")
        self.label_check = QLabel(self.frame_game)
        self.label_check.setObjectName(u"label_check")
        self.label_check.setGeometry(QRect(350, 130,60, 21))
        self.label_check.setStyleSheet(u"background-color: rgb(83, 83, 83);\n"
"font: 75 12pt \"Yu Gothic UI\";\n"
"border:none;\n"
"border-radius:20px;")

        self.label_word = QLabel(self.frame_game)
        self.label_word.setObjectName(u"label_word")
        self.label_word.setGeometry(QRect(190, 230, 70, 30))
        self.label_word.setStyleSheet(u"background-color: rgb(83, 83, 83);\n"
"font: 75 12pt \"Yu Gothic UI\";\n"
"border:none;\n"
"border-radius:20px;")

        self.retranslateUi(widget_game)

        QMetaObject.connectSlotsByName(widget_game)
    # setupUi

    def retranslateUi(self, widget_game):
        widget_game.setWindowTitle(QCoreApplication.translate("widget_game", u"FLASHCARDS FOR DUTCH LEARNING", None))
        self.label_card.setText("")
        self.label_language.setText(QCoreApplication.translate("widget_game", u"DUTCH", None))
        self.button_ok.setText(QCoreApplication.translate("widget_game", u"OK", None))
        self.button_cancel.setText(QCoreApplication.translate("widget_game", u"CANCEL", None))
        #self.timeEdit.setDisplayFormat(QCoreApplication.translate("widget_game", u"mm:ss", None))
        self.label_time.setText(QCoreApplication.translate("widget_game", u"TIME", None))
        self.button_back.setText(QCoreApplication.translate("widget_game", u"BACK", None))
#if QT_CONFIG(whatsthis)
        self.label_check.setWhatsThis(QCoreApplication.translate("widget_game", u"<html><head/><body><p align=\"center\"><br/></p></body></html>", None))
#endif // QT_CONFIG(whatsthis)
        self.label_check.setText(QCoreApplication.translate("widget_game", u"0/20", None))
        self.label_word.setText(QCoreApplication.translate("widget_game", u"Vocabulary", None))
    # retranslateUi    
        self.label_word.setText("START!")
        
        
class Get_GamePage(QWidget, Ui_widget_game):
        def __init__(self):
                super(Get_GamePage,self).__init__()
                self.setupUi(self)
                #buttons functions
                self.button_ok.clicked.connect(self.my_word)
                self.button_cancel.clicked.connect(self.my_canceled_word)
                #dataframe of the cards
                self.df=pd.read_json("C:/Users/conko/OneDrive/Desktop/FlashCards/FlashCards_Team1/translatedCards.json")

                #get the current username
                my_login_object=Login_Page()
                self.username=my_login_object.username

                #get the current level of player
                url="C:/Users/conko/OneDrive/Desktop/FlashCards/FlashCards_Team1/Loginsystem.json"
                with open(url, 'r+') as f:
                        data = json.load(f)
                res=list(filter(lambda x: x["username"] == self.username, data))
                self.df_level=res[0]['level']
                              
                #create vocabulary lists
                self.woorden_lijst=self.df[self.df['Unnamed: 0']==f'Level{self.df_level}']['Nederlands']
                self.vocab_list=self.df[self.df['Unnamed: 0']==f'Level{self.df_level}']['English']
                print(self.woorden_lijst )

                #it adjust the counter according to length of the list 
                c=self.df[self.df['Unnamed: 0']==f'Level{self.df_level}']['English'].index                
                self.counter=c[0]

                #unknown vocaabulary
                self.unknown_words=[]

                #white button sign
                self.flag=True

        #other functions        
        def update_background(self):
                #it makes white buttons colorful
                if self.flag:

                        self.button_ok.setStyleSheet("background-color: white;")
                        self.button_cancel.setStyleSheet("background-color: white;")
                else:                       
                        self.button_ok.setStyleSheet("background-color: green ;")
                        self.button_cancel.setStyleSheet("background-color: red ;")
                          
                self.flag = not self.flag  

   
        def configureButton(self, button, begin, duration):

                end = begin.addSecs(duration)#duration: configuration total duration
              
                now = QTime.currentTime()
                button.setEnabled(begin <= now <= end)

              #This part works after 3 secs are finished
                if now < begin: 
                        self.update_background()

                        #Set enable button_ok and button_cancel
                        QTimer.singleShot(
                                now.msecsTo(begin), lambda: button.setEnabled(True))

                        #activate Engels  
                        my_word=self.df[self.df['Unnamed: 0']==f'Level{self.df_level}']['English'][self.counter]        
                        QTimer.singleShot(
                                now.msecsTo(begin),lambda: self.label_word.setText(my_word))

                        #change Language Title to English
                        change_title="ENGLISH"
                        QTimer.singleShot(
                                now.msecsTo(begin),lambda: self.label_language.setText(change_title))   

                #This part works when 3 sec begins again / deactivate butons           
                if now < end:
                        self.update_background()
                        QTimer.singleShot(
                                now.msecsTo(end), lambda: button.setEnabled(False))
                                

        def activateButton(self):
                #set 3 seconds to activate button_ok 
                begin = QTime.currentTime().addSecs(1)#delay the begin time 3 sec
                self.configureButton(self.button_ok, begin, 120)#every activating has 120 sec total duration to keep in activate
                #set 3 seconds to activate button_cancel
                begin = QTime.currentTime().addSecs(1)
                self.configureButton(self.button_cancel, begin, 120)
                #change language title to Dutch
                change_title="DUTCH"
                self.label_language.setText(change_title)
                print("activitate button calisti")
        
        def flashcard(self):              

                try:                                                
                        #activate the buttons with timer
                        self.activateButton()
                        
                        #test 
                        print(self.woorden_lijst[self.counter])   
                                
                        #run the game/print word on the screen
                        my_word=self.woorden_lijst[self.counter]
                        self.label_word.setText(my_word)

                        #check label update etme
                        check_lbl=f"{self.counter}"+f"/{self.woorden_lijst.index[19]}"
                        self.label_check.setText(check_lbl)

                        #update counter
                        self.counter +=1

                except KeyError:
                        #Later we can add a back button
                        print("Key Error Olustu")
                        self.label_word.setText("KLAAR")
                        print(self.unknown_words)
                        #self.update_level()

        #create a new list 
        def my_canceled_word(self):
                print("CANCEL CLICKED")
                self.flashcard() 
                self.unknown_words.append(self.df[self.df['Unnamed: 0']==f'Level{self.df_level}']['Nederlands'][self.counter-2])
                 
        #update level in the json file
        def update_level(self):
                #set the current level to the json file
                url="C:/Users/conko/OneDrive/Desktop/FlashCards/FlashCards_Team1/Loginsystem.json"
                with open(url, 'r+') as f:
                        data = json.load(f)
                        data[0]['level'] = self.df_level+1 
                        f.seek(0)        
                        json.dump(data, f )
                        f.truncate() 

        #game works with this method
        def my_word(self):
                #call the flashcard function
                self.flashcard() 

        #update list(unknown vocabulary list)
        def last_list(self):
                pass
        #update counter 
        def last_counter(self):
                pass        


def main():
    import sys
    app = QApplication(sys.argv)
    get_GamePage= Get_GamePage()
    get_GamePage.show()
    sys.exit(app.exec_())

if __name__ == "__main__":
    main()
         
  