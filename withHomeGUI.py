import sys
from PyQt5.QtWidgets import QMainWindow, QApplication, QWidget, QPushButton, QAction, QLineEdit, QMessageBox, QLabel
from PyQt5.QtGui import QIcon, QFont, QPixmap
from PyQt5.QtCore import pyqtSlot

import sqlite3
import pymysql
import recordingSnd
 
class App(QMainWindow):
 
    def __init__(self):
        super().__init__()
        self.title = 'withHome'
        self.left = 100
        self.top = 100
        self.width = 450
        self.height = 440
        self.initUI()
 
    def initUI(self):
        self.setWindowTitle(self.title)
        self.setGeometry(self.left, self.top, self.width, self.height)

        font = QFont()
        font.setFamily("KoPub돋움체 Medium")
        font.setPointSize(12)

        # Create logo GUI
        self.logoGUI = QLabel(self)
        self.logoGUI.move(120,40)
        self.logoGUI.resize(221,221)
        self.logoGUI.setText("")
        self.logoGUI.setPixmap(QPixmap("프로토타입_2.png"))

        # Create idLabel and pwLabel
        self.idLabel = QLabel(self)
        self.idLabel.move(120,290)
        self.idLabel.resize(71,16)
        self.idLabel.setText("아이디    :")
        self.idLabel.setFont(font)

        self.pwLabel = QLabel(self)
        self.pwLabel.move(120,330)
        self.pwLabel.resize(71,16)
        self.pwLabel.setText("비밀번호 : ")
        self.pwLabel.setFont(font)
        
        # Create idTextbox
        self.idTextbox = QLineEdit(self)
        self.idTextbox.move(200, 280)
        self.idTextbox.resize(131,31)
        self.idTextbox.setFont(font)

        # Create pwTextbox
        self.pwTextbox = QLineEdit(self)
        self.pwTextbox.move(200, 320)
        self.pwTextbox.resize(131,31)
        self.pwTextbox.setFont(font)
 
        # Create a button in the window
        self.button = QPushButton('로그인', self)
        self.button.move(190,360)
        self.button.resize(81,31)
        self.button.setFont(font)

        #Create label for success login
        self.sucessloginLabel = QLabel(self)
        self.sucessloginLabel.move(160,290)
        self.sucessloginLabel.resize(131,31)
        self.sucessloginLabel.setFont(font)
        self.sucessloginLabel.setText('녹음 중 입니다...')
        self.sucessloginLabel.hide()
 
        # connect button to function on_click
        self.button.clicked.connect(self.on_click)
        self.show()
 
    @pyqtSlot()
    def on_click(self):
        userID = self.idTextbox.text()
        userPW = self.pwTextbox.text()

        print("id is",userID,"and pw is "+userPW)
        #QMessageBox.question(self, 'Message - pythonspot.com', ("You typed: " + idValue+" "+pwValue), QMessageBox.Ok, QMessageBox.Ok)
        awsConn = pymysql.connect(host='ec2-18-222-86-176.us-east-2.compute.amazonaws.com', port=3306,
                     user='mozzi', passwd='testMozzi2!', db='withhome', charset='utf8')
        select_sql = "select userPassword from users_record where userID = %s"
        cur = awsConn.cursor()
        cur.execute(select_sql,(userID,))
        row = cur.fetchall()

        if len(row) != 0:
            for i in row :
                print(i[0])
                if userPW == i[0]:
                    self.idLabel.hide()
                    self.pwLabel.hide()
                    self.idTextbox.hide()
                    self.pwTextbox.hide()
                    self.button.hide()

                    self.sucessloginLabel.show()

                    
                    localConn = sqlite3.connect('database.db')
                    localConn.execute("CREATE TABLE if not exists classifiedSound (userID VARCHAR(16) DEFAULT " + userID +", soundIndex INT, time TIMESTAMP)")
                    localConn.close()
                   # recordingSnd.recording(userID)
                else:
                    QMessageBox.question(self, '오류!', '잘못된 비밀번호입니다!', QMessageBox.Ok, QMessageBox.Ok)
        else :
            QMessageBox.question(self, '오류!','존재하지 않는 아이디입니다!', QMessageBox.Ok, QMessageBox.Ok)


        awsConn.close()
 
 
if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = App()
    sys.exit(app.exec_())
