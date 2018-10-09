import sys
from PyQt5.QtWidgets import QMainWindow, QApplication, QWidget, QPushButton, QAction, QLineEdit, QMessageBox, QLabel
from PyQt5.QtGui import QIcon, QFont, QPixmap
from PyQt5.QtCore import Qt
from PyQt5.QtCore import QThread
from PyQt5.QtCore import QWaitCondition
from PyQt5.QtCore import QMutex
from PyQt5.QtCore import pyqtSignal
from PyQt5.QtCore import pyqtSlot

import sqlite3
import pymysql
import recordingSnd
import threading,requests,time

class WorkerThread(QThread):

    def __init__(self):
        QThread.__init__(self)
        self.cond = QWaitCondition()
        self.mutex = QMutex()
        self._status = False
        self.userID = ""

    def __del__(self):
        self.wait()

    def run(self):
        while True:
            self.mutex.lock()
            print("start thread")

            if not self._status:
                self.cond.wait(self.mutex)
            #print(userID)
            recordingSnd.recording(self.userID)
            print("going to another work")
            
            self.msleep(100)

            self.mutex.unlock()

    def toggle_status(self,userID):
        self.userID = userID
        self._status = not self._status
        if self._status:
            self.cond.wakeAll() 

    @property
    def status(self):
        return self._status
 
class App(QMainWindow):
 
    def __init__(self):
        super().__init__()
        self.title = 'withHome'
        self.left = 100
        self.top = 100
        self.width = 900
        self.height = 880
        self.th = WorkerThread()
        self.initUI()
        self.th.start()     
        
 
    def initUI(self):
        self.userID = ""
        self.userPW = ""
        print("in initUI, userID is "+self.userID+"and userPW is "+self.userPW)
        self.setWindowTitle(self.title)
        self.setGeometry(self.left, self.top, self.width, self.height)

        font = QFont()
        font.setFamily("KoPub돋움체 Medium")
        font.setPointSize(12)

        # Create logo GUI
        self.logoGUI = QLabel(self)
        self.logoGUI.move(240,80)
        self.logoGUI.resize(442,442)
        self.logoGUI.setText("")
        self.logoGUI.setPixmap(QPixmap("그림1.png"))

        # Create idLabel and pwLabel
        self.idLabel = QLabel(self)
        self.idLabel.move(220,580)
        self.idLabel.resize(152,40)
        self.idLabel.setText("아이디   :")
        self.idLabel.setFont(font)

        self.pwLabel = QLabel(self)
        self.pwLabel.move(220,660)
        self.pwLabel.resize(152,40)
        self.pwLabel.setText("비밀번호: ")
        self.pwLabel.setFont(font)
        
        # Create idTextbox
        self.idTextbox = QLineEdit(self)
        self.idTextbox.move(400, 560)
        self.idTextbox.resize(262,62)
        self.idTextbox.setFont(font)

        # Create pwTextbox
        self.pwTextbox = QLineEdit(self)
        self.pwTextbox.move(400, 640)
        self.pwTextbox.resize(262,62)
        self.pwTextbox.setFont(font)
 
        # Create a button in the window
        self.button = QPushButton('로그인', self)
        self.button.move(380,720)
        self.button.resize(162,62)
        self.button.setFont(font)

        #Create label for success login
        self.sucessloginLabel = QLabel(self)
        self.sucessloginLabel.move(320,580)
        self.sucessloginLabel.resize(262,62)
        self.sucessloginLabel.setFont(font)
        self.sucessloginLabel.setText('녹음 중 입니다...')
        self.sucessloginLabel.hide()
 
        # connect button to function on_click
        self.button.clicked.connect(self.on_click)
        self.show()
 
    @pyqtSlot()
    def on_click(self):
        self.userID = self.idTextbox.text()
        self.userPW = self.pwTextbox.text()
        
        awsConn = pymysql.connect(host='ec2-18-222-86-176.us-east-2.compute.amazonaws.com', port=3306,
                     user='mozzi', passwd='testMozzi2!', db='withhome', charset='utf8')
        select_sql = "select userPassword from users_record where userID = %s"
        cur = awsConn.cursor()
        cur.execute(select_sql,(self.userID,))
        row = cur.fetchall()

        if len(row) != 0:
            for i in row :
                print(i[0])
                if self.userPW == i[0]:
                    self.idLabel.hide()
                    self.pwLabel.hide()
                    self.idTextbox.hide()
                    self.pwTextbox.hide()
                    self.button.hide()
                    self.sucessloginLabel.show()

                    localConn = sqlite3.connect('database.db')
                    localConn.execute("CREATE TABLE if not exists classifiedSound (userID VARCHAR(16) DEFAULT " + self.userID +", soundIndex INT, time TIMESTAMP)")
                    localConn.close()

                    self.th.toggle_status(userID = self.userID)
                    
                else:
                    QMessageBox.question(self, '오류!', '잘못된 비밀번호입니다!', QMessageBox.Ok, QMessageBox.Ok)
        else :
            QMessageBox.question(self, '오류!','존재하지 않는 아이디입니다!', QMessageBox.Ok, QMessageBox.Ok)

            
        awsConn.close()
 
 
if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = App()
    sys.exit(app.exec_())
