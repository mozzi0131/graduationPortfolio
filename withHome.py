# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'withHomeGui.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_withHome(object):
    def setupUi(self, withHome):
        withHome.setObjectName("withHome")
        withHome.resize(800, 600)
        self.centralwidget = QtWidgets.QWidget(withHome)
        self.centralwidget.setObjectName("centralwidget")
        self.idTextField = QtWidgets.QPlainTextEdit(self.centralwidget)
        self.idTextField.setGeometry(QtCore.QRect(358, 290, 251, 51))
        self.idTextField.setPlainText("")
        self.idTextField.setObjectName("idTextField")
        self.pwTextField = QtWidgets.QPlainTextEdit(self.centralwidget)
        self.pwTextField.setGeometry(QtCore.QRect(358, 360, 251, 51))
        self.pwTextField.setPlainText("")
        self.pwTextField.setObjectName("pwTextField")
        self.idLabel = QtWidgets.QLabel(self.centralwidget)
        self.idLabel.setGeometry(QtCore.QRect(178, 300, 161, 30))
        font = QtGui.QFont()
        font.setFamily("KoPub돋움체 Light")
        font.setBold(True)
        font.setWeight(75)
        self.idLabel.setFont(font)
        self.idLabel.setObjectName("idLabel")
        self.pwLabel = QtWidgets.QLabel(self.centralwidget)
        self.pwLabel.setGeometry(QtCore.QRect(180, 370, 141, 30))
        font = QtGui.QFont()
        font.setFamily("KoPub돋움체 Medium")
        self.pwLabel.setFont(font)
        self.pwLabel.setObjectName("pwLabel")
        self.loginButton = QtWidgets.QPushButton(self.centralwidget)
        self.loginButton.setGeometry(QtCore.QRect(310, 440, 187, 57))
        font = QtGui.QFont()
        font.setFamily("KoPub돋움체 Medium")
        self.loginButton.setFont(font)
        self.loginButton.setObjectName("loginButton")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(290, 50, 221, 191))
        self.label.setText("")
        self.label.setPixmap(QtGui.QPixmap("./withHome.png"))
        self.label.setObjectName("label")
        withHome.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(withHome)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 47))
        self.menubar.setObjectName("menubar")
        withHome.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(withHome)
        self.statusbar.setObjectName("statusbar")
        withHome.setStatusBar(self.statusbar)

        self.retranslateUi(withHome)
        QtCore.QMetaObject.connectSlotsByName(withHome)

    def retranslateUi(self, withHome):
        _translate = QtCore.QCoreApplication.translate
        withHome.setWindowTitle(_translate("withHome", "withHome"))
        self.idLabel.setText(_translate("withHome", "아이디    : "))
        self.pwLabel.setText(_translate("withHome", "비밀번호 : "))
        self.loginButton.setText(_translate("withHome", "로그인"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    withHome = QtWidgets.QMainWindow()
    ui = Ui_withHome()
    ui.setupUi(withHome)
    withHome.show()
    sys.exit(app.exec_())

