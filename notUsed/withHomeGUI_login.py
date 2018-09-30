# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'withHomeGUI_login.ui'
#
# Created by: PyQt5 UI code generator 5.6
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
import sqlite3
import pymysql
import recordingSnd

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(450, 440)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.logoGUI = QtWidgets.QLabel(self.centralwidget)
        self.logoGUI.setGeometry(QtCore.QRect(120, 40, 221, 221))
        self.logoGUI.setText("")
        self.logoGUI.setPixmap(QtGui.QPixmap("프로토타입_2.png"))
        self.logoGUI.setObjectName("logoGUI")
        self.idLabel = QtWidgets.QLabel(self.centralwidget)
        self.idLabel.setGeometry(QtCore.QRect(120, 290, 91, 16))
        font = QtGui.QFont()
        font.setFamily("KoPub돋움체 Medium")
        font.setPointSize(12)
        self.idLabel.setFont(font)
        self.idLabel.setObjectName("idLabel")
        self.pwLabel = QtWidgets.QLabel(self.centralwidget)
        self.pwLabel.setGeometry(QtCore.QRect(120, 330, 71, 16))
        font = QtGui.QFont()
        font.setFamily("KoPub돋움체 Medium")
        font.setPointSize(12)
        self.pwLabel.setFont(font)
        self.pwLabel.setObjectName("pwLabel")
        self.idTextFIeld = QtWidgets.QPlainTextEdit(self.centralwidget)
        self.idTextFIeld.setGeometry(QtCore.QRect(200, 280, 131, 31))
        font = QtGui.QFont()
        font.setFamily("KoPub돋움체 Medium")
        font.setPointSize(12)
        self.idTextFIeld.setFont(font)
        self.idTextFIeld.setPlainText("")
        self.idTextFIeld.setObjectName("idTextFIeld")
        self.pwTextField = QtWidgets.QPlainTextEdit(self.centralwidget)
        self.pwTextField.setGeometry(QtCore.QRect(200, 320, 131, 31))
        font = QtGui.QFont()
        font.setFamily("KoPub돋움체 Medium")
        font.setPointSize(12)
        self.pwTextField.setFont(font)
        self.pwTextField.setPlainText("")
        self.pwTextField.setObjectName("pwTextField")
        self.loginButton = QtWidgets.QPushButton(self.centralwidget)
        self.loginButton.setGeometry(QtCore.QRect(190, 360, 81, 31))
        font = QtGui.QFont()
        font.setFamily("KoPub돋움체 Medium")
        font.setPointSize(12)
        self.loginButton.setFont(font)
        self.loginButton.setObjectName("loginButton")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 450, 21))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

        self.loginButton.clicked.connect(self.loginBtn_clicked)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "withHome"))
        self.idLabel.setText(_translate("MainWindow", "아이디    :"))
        self.pwLabel.setText(_translate("MainWindow", "비밀번호 : "))
        self.loginButton.setText(_translate("MainWindow", "로그인"))

    def loginBtn_clicked(self):
        print("called")
        userID = self.idTextField.toPlainText()
        userPW = self.pwTextField.toPlainText()

        print("readed")

        print(userID+", "+userPW)
        
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
                    localConn = sqlite3.connect('database.db')
                    localConn.execute("CREATE TABLE if not exists classifiedSound (userID VARCHAR(16) DEFAULT " + userID +", soundIndex INT, time TIMESTAMP)")
                    localConn.close()
                    recordingSnd.recording(userID)
                else:
                    print("맞는 pw가 아닙니다")
        else :
            print("존재하지 않는 id입니다")


        awsConn.close()



if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())

