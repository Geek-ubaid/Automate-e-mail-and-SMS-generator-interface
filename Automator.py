# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'main.ui'
#
# Created by: PyQt5 UI code generator 5.10
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
import re
import string

class Ui_MainWindow(object):
    def fileextractm(self):
        rec = self.recipientsm.text()
        if (str(rec)[len(rec) - 4::] == ".txt"):
            with open(rec,"r") as file:
                for i in file.readlines():      #the csv format shoulf be like name regno phoneno emailaddress
                    l=i.split(" ")
                    self.dic1={}
                    self.dic1[l[2]]=(l[0],l[1])
            print("Recipients added")
        else:
            print("Wrong file type or no longer exist")

    def fileextract(self):
        recm=self.recipients.text()
        if (str(recm)[len(recm)-4::]==".txt"):
            with open(recm,"r") as file :
                for i in file.readlines():
                    l=i.split(" ")
                    self.dic2={}
                    self.dic[l[3]]=(l[0],l[1])
            print("Recipients added")
        else:
            print("Wrong file type")


    def sendmail(self):
        self.msg=self.message.text()
        print(self.msg)
        for i in self.dic2.keys():
            print(i)
            self.msg=self.msg.replace("#studentname",self.dic2[i][0])
            self.msg=self.msg.replace("#regno",self.dic2[i][1])


    def sendmess(self):
        self.msgm=self.messaget.text()
        print(self.msgm)
        for i in dic1.keys():
            self.msgm=self.msgm.replace("#studentname",self.dic1[i][0])
            self.msgm=self.msgm.replace("#regno",self.dic1[i][1])
            print(self.msgm)



    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(893, 654)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.tabWidget = QtWidgets.QTabWidget(self.centralwidget)
        self.tabWidget.setGeometry(QtCore.QRect(10, 10, 861, 621))
        font = QtGui.QFont()
        font.setPointSize(8)
        self.tabWidget.setFont(font)
        self.tabWidget.setObjectName("tabWidget")
        self.tab = QtWidgets.QWidget()
        self.tab.setObjectName("tab")
        self.subject = QtWidgets.QLineEdit(self.tab)
        self.subject.setGeometry(QtCore.QRect(190, 120, 471, 31))
        self.subject.setObjectName("subject")
        sub=self.subject.text()
        self.recipients = QtWidgets.QLineEdit(self.tab)
        self.recipients.setGeometry(QtCore.QRect(190, 30, 471, 31))
        self.recipients.setObjectName("rercipients")

        self.label_2 = QtWidgets.QLabel(self.tab)
        self.label_2.setGeometry(QtCore.QRect(50, 120, 81, 31))
        self.label_2.setObjectName("label_2")
        self.label = QtWidgets.QLabel(self.tab)
        self.label.setGeometry(QtCore.QRect(50, 30, 71, 31))
        self.label.setObjectName("label")
        self.label_3 = QtWidgets.QLabel(self.tab)
        self.label_3.setGeometry(QtCore.QRect(50, 200, 81, 31))
        self.label_3.setObjectName("label_3")
        self.attachment = QtWidgets.QPushButton(self.tab)
        self.attachment.setGeometry(QtCore.QRect(200, 170, 75, 23))
        self.attachment.setObjectName("attachment")
        self.send = QtWidgets.QPushButton(self.tab)
        self.send.setGeometry(QtCore.QRect(680, 550, 75, 23))
        self.send.setObjectName("send")
        self.send.clicked.connect(self.sendmail)
        self.extract = QtWidgets.QPushButton(self.tab)
        self.extract.setGeometry(QtCore.QRect(690, 30, 75, 23))
        self.extract.setObjectName("extract")
        self.extract.clicked.connect(self.fileextract)
        self.message = QtWidgets.QPlainTextEdit(self.tab)
        self.message.setGeometry(QtCore.QRect(70, 270, 681, 251))
        self.message.setObjectName("message")
        self.tabWidget.addTab(self.tab, "")
        self.tab_2 = QtWidgets.QWidget()
        self.tab_2.setObjectName("tab_2")
        self.label_4 = QtWidgets.QLabel(self.tab_2)
        self.label_4.setGeometry(QtCore.QRect(90, 180, 121, 51))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.label_4.setFont(font)
        self.label_4.setObjectName("label_4")
        self.messaget = QtWidgets.QPlainTextEdit(self.tab_2)
        self.messaget.setGeometry(QtCore.QRect(80, 250, 571, 251))
        self.messaget.setObjectName("messaget")
        self.sendm = QtWidgets.QPushButton(self.tab_2)
        self.sendm.setGeometry(QtCore.QRect(700, 280, 75, 23))
        self.sendm.setObjectName("sendm")
        self.sendm.clicked.connect(self.sendmess)
        self.label_5 = QtWidgets.QLabel(self.tab_2)
        self.label_5.setGeometry(QtCore.QRect(100, 70, 111, 16))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(13)
        font.setBold(True)
        font.setWeight(75)
        self.label_5.setFont(font)
        self.label_5.setObjectName("label_5")
        self.recipientsm = QtWidgets.QLineEdit(self.tab_2)
        self.recipientsm.setGeometry(QtCore.QRect(290, 60, 231, 31))
        self.recipientsm.setObjectName("recipientsm")
        self.extractm = QtWidgets.QPushButton(self.tab_2)
        self.extractm.setGeometry(QtCore.QRect(600, 70, 75, 23))
        self.extractm.setObjectName("extractm")
        self.extractm.clicked.connect(self.fileextractm)
        self.tabWidget.addTab(self.tab_2, "")
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        self.tabWidget.setCurrentIndex(1)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label_2.setText(_translate("MainWindow", "Subject"))
        self.label.setText(_translate("MainWindow", "Recipients:"))
        self.label_3.setText(_translate("MainWindow", "Message"))
        self.attachment.setText(_translate("MainWindow", "Attachment"))
        self.send.setText(_translate("MainWindow", "SEND "))
        self.extract.setText(_translate("MainWindow", "Extract"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab), _translate("MainWindow", "E-mail"))
        self.label_4.setText(_translate("MainWindow", "Your message"))
        self.sendm.setText(_translate("MainWindow", "SEND"))
        self.label_5.setText(_translate("MainWindow", "Recipients"))
        self.extractm.setText(_translate("MainWindow", "Extract"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_2), _translate("MainWindow", "SMS"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())

