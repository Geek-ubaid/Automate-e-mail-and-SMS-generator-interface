# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'login.ui'
#
# Created by: PyQt5 UI code generator 5.6
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
import sys
import smtplibaio
class Ui_loginwindow(object):
    def logincheck(self):
        passget = self.pass1.text()
        userget=self.user.text()
        server = smtplibaio.SMTP_SSL('smtp.gmail.com', 587)
        server.ehlo()
        server.starttls()
        try:
            server.login(userget, passget)
        except:
           print("error")
           self.msg=QtWidgets.QMessageBox(loginwindow)
           self.msg.setIcon(self,"critical")
           self.msg.setText("Invalid Credentials")
           self.msg.setWindowTitle("Error in Login")
           self.msg.show()



    def resetcheck(self):
        self.pass1.setText("")
        self.user.setText("")

    def setupUi(self, loginwindow):
        loginwindow.setObjectName("loginwindow")
        loginwindow.resize(719, 392)
        self.title = QtWidgets.QLabel(loginwindow)
        self.title.setGeometry(QtCore.QRect(220, 60, 251, 41))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(24)
        font.setBold(True)
        font.setWeight(75)
        self.title.setFont(font)
        self.title.setObjectName("title")
        self.username = QtWidgets.QLabel(loginwindow)
        self.username.setGeometry(QtCore.QRect(150, 160, 111, 16))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.username.setFont(font)
        self.username.setObjectName("username")
        self.password = QtWidgets.QLabel(loginwindow)
        self.password.setGeometry(QtCore.QRect(150, 230, 101, 21))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.password.setFont(font)
        self.password.setObjectName("password")
        self.login = QtWidgets.QPushButton(loginwindow)
        self.login.setGeometry(QtCore.QRect(350, 310, 75, 23))
        self.login.setObjectName("login")
        self.login.clicked.connect(self.logincheck)
        self.reset = QtWidgets.QPushButton(loginwindow)
        self.reset.setGeometry(QtCore.QRect(470, 310, 75, 23))
        self.reset.setObjectName("reset")
        self.reset.clicked.connect(self.resetcheck)
        self.user = QtWidgets.QLineEdit(loginwindow)
        self.user.setGeometry(QtCore.QRect(380, 150, 151, 31))
        self.user.setObjectName("user")
        self.pass1= QtWidgets.QLineEdit(loginwindow)
        self.pass1.setGeometry(QtCore.QRect(380, 220, 151, 31))
        self.pass1.setObjectName("pass")
        self.pass1.setEchoMode(QtWidgets.QLineEdit.Password )

        self.retranslateUi(loginwindow)
        QtCore.QMetaObject.connectSlotsByName(loginwindow)

    def retranslateUi(self, loginwindow):
        _translate = QtCore.QCoreApplication.translate
        loginwindow.setWindowTitle(_translate("loginwindow", "Pymail"))
        self.title.setText(_translate("loginwindow", "E-MAIL LOGIN"))
        self.username.setText(_translate("loginwindow", "USERNAME"))
        self.password.setText(_translate("loginwindow", "PASSWORD"))
        self.login.setText(_translate("loginwindow", "OK"))
        self.reset.setText(_translate("loginwindow", "RESET"))





if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    loginwindow = QtWidgets.QDialog()
    ui = Ui_loginwindow()
    ui.setupUi(loginwindow)
    loginwindow.show()
    sys.exit(app.exec_())

