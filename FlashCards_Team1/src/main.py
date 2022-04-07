from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2 import QtWidgets,QtCore
from PySide2.QtWidgets import *
from PySide2.QtWidgets import QApplication,QMainWindow,QBoxLayout,QWidget
from PySide2 import  QtCore
import sys
import pandas as pd


from MainMenu import GetMenuFrame
from Levels import  Get_LevelPage
from GamePage import  Get_GamePage
from LoginPage import Login_Page
from leveldesign import level_word
 

class MainWindow(QMainWindow):
    
    def __init__(self): 
        super(MainWindow,self).__init__()

        self.df=pd.read_json("C:/Users/conko/OneDrive/Desktop/FlashCards/FlashCards_Team1/translatedCards.json")

        self.win_log = Login_Page()
        self.win_menu=GetMenuFrame()
        self.win_level=Get_LevelPage()
        #self.win_game=Get_GamePage()
        self.win_levelWord=level_word()

        #login buttons
        self.win_log.button_login.clicked.connect(self.clicked_button_login)
        #main menu buttons
        self.win_menu.button_levels.clicked.connect(self.clicked_button_levels)
        self.win_menu.button_exit.clicked.connect(self.clicked_button_exit)
        self.win_menu.button_play.clicked.connect(self.clicked_button_game)
        #self.win_menu.button_yourlevel.clicked.connect(GetMenuFrame.YLevel_Pressed)

        #game screen buttons
        win_game=Get_GamePage()
        win_game.button_back.clicked.connect(self.clicked_button_back)
        
        

        #level buttons
        self.win_level.button_lvl_back.clicked.connect(self.button_lvl_back_Pressed)        
        self.win_level.button_level1.clicked.connect(self.button_level1_Pressed)
        self.win_level.button_level2.clicked.connect(self.button_level2_Pressed)
        self.win_level.button_level3.clicked.connect(self.button_level3_Pressed)
        self.win_level.button_level4.clicked.connect(self.button_level4_Pressed)
        self.win_level.button_level5.clicked.connect(self.button_level5_Pressed)
        self.win_level.button_level6.clicked.connect(self.button_level6_Pressed)
        self.win_level.button_level7.clicked.connect(self.button_level7_Pressed)
        self.win_level.button_level8.clicked.connect(self.button_level8_Pressed)
        self.win_level.button_level9.clicked.connect(self.button_level9_Pressed)
        self.win_level.button_level10.clicked.connect(self.button_level10_Pressed)
        self.win_level.button_level11.clicked.connect(self.button_level11_Pressed)
        self.win_level.button_level12.clicked.connect(self.button_level12_Pressed)
        self.win_level.button_level13.clicked.connect(self.button_level13_Pressed)
        self.win_level.button_level14.clicked.connect(self.button_level14_Pressed)
        self.win_level.button_level15.clicked.connect(self.button_level15_Pressed)
        self.win_level.button_level16.clicked.connect(self.button_level16_Pressed)
        self.win_level.button_level17.clicked.connect(self.button_level17_Pressed)
        self.win_level.button_level18.clicked.connect(self.button_level18_Pressed)
        self.win_level.button_level19.clicked.connect(self.button_level19_Pressed)
        self.win_level.button_level20.clicked.connect(self.button_level20_Pressed)

        #show your widget
        self.win_log.show()

        #button methods
    def clicked_button_login(self):
        print("button login clicked")
        self.win_log.hide()                     
        self.win_menu.show()

    def clicked_button_game(self):    
        print("button game clicked")
        self.win_menu.hide()                     
        self.win_game.show()
        
        
    def clicked_button_back(self):
        print("button back clicked")
        self.win_game.hide()                     
        self.win_menu.show()

    def clicked_button_levels(self):
        print("button levels clicked")
        self.win_menu.hide()                     
        self.win_level.show()

    def clicked_button_exit(self):
        sys.exit()    

    #level methods
    def button_lvl_back_Pressed(self):
        print("button levels back clicked")
        self.win_level.hide()                     
        self.win_menu.show()

    def button_level1_Pressed(self):
        #for i in range(20):
        #    a=self.df["Nederlands"][f"('Level1', '{i}')"]
        #    print(a)
        self.win_levelWord.j=1
        self.win_levelWord.words_pressed()
        #self.win_level.hide()
        self.win_levelWord.show()  
        
        #print(self.df[self.df['Unnamed: 0']=='Level1']['Nederlands'])
    def button_level2_Pressed(self):
        self.win_levelWord.j=2
        self.win_levelWord.words_pressed()
        self.win_levelWord.show()
        
    def button_level3_Pressed(self):
        self.win_levelWord.j=3
        self.win_levelWord.words_pressed()
        self.win_levelWord.show()

    def button_level4_Pressed(self):
        self.win_levelWord.j=4
        self.win_levelWord.words_pressed()
        self.win_levelWord.show()
        
    def button_level5_Pressed(self):
        self.win_levelWord.j=5
        self.win_levelWord.words_pressed()
        self.win_levelWord.show()
    def button_level6_Pressed(self):
        self.win_levelWord.j=6
        self.win_levelWord.words_pressed()
        self.win_levelWord.show()
    def button_level7_Pressed(self):
        self.win_levelWord.j=7
        self.win_levelWord.words_pressed()
        self.win_levelWord.show()
    def button_level8_Pressed(self):
        self.win_levelWord.j=8
        self.win_levelWord.words_pressed()
        self.win_levelWord.show()
    def button_level9_Pressed(self):
        self.win_levelWord.j=9
        self.win_levelWord.words_pressed()
        self.win_levelWord.show()                                
    def button_level10_Pressed(self):
        self.win_levelWord.j=10
        self.win_levelWord.words_pressed()
        self.win_levelWord.show()
    def button_level11_Pressed(self):
        self.win_levelWord.j=11
        self.win_levelWord.words_pressed()
        self.win_levelWord.show()
    def button_level12_Pressed(self):
        self.win_levelWord.j=12
        self.win_levelWord.words_pressed()
        self.win_levelWord.show()
    def button_level13_Pressed(self):
        self.win_levelWord.j=13
        self.win_levelWord.words_pressed()
        self.win_levelWord.show()
    def button_level14_Pressed(self):
        self.win_levelWord.j=14
        self.win_levelWord.words_pressed()
        self.win_levelWord.show()
    def button_level15_Pressed(self):
        self.win_levelWord.j=15
        self.win_levelWord.words_pressed()
        self.win_levelWord.show()
    def button_level16_Pressed(self):
        self.win_levelWord.j=16
        self.win_levelWord.words_pressed()
        self.win_levelWord.show()
    def button_level17_Pressed(self):
        self.win_levelWord.j=17
        self.win_levelWord.words_pressed()
        self.win_levelWord.show()
    def button_level18_Pressed(self):
        self.win_levelWord.j=18
        self.win_levelWord.words_pressed()
        self.win_levelWord.show() 
    def button_level19_Pressed(self):
        self.win_levelWord.j=19
        self.win_levelWord.words_pressed()
        self.win_levelWord.show()
    def button_level20_Pressed(self):
        self.win_levelWord.j=20
        self.win_levelWord.words_pressed()
        self.win_levelWord.show()     

def main():
    import sys
    app = QtWidgets.QApplication(sys.argv)
    w = MainWindow()
    w.show()  
    sys.exit(app.exec_())

if __name__ == "__main__":
    main()
         
  

