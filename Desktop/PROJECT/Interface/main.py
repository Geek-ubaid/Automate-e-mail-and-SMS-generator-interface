# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'main.ui'
#
# Created by: PyQt5 UI code generator 5.10
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(981, 629)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.tabWidget = QtWidgets.QTabWidget(self.centralwidget)
        self.tabWidget.setGeometry(QtCore.QRect(10, 10, 1101, 631))
        font = QtGui.QFont()
        font.setPointSize(8)
        self.tabWidget.setFont(font)
        self.tabWidget.setStyleSheet("")
        self.tabWidget.setObjectName("tabWidget")
        self.tab = QtWidgets.QWidget()
        self.tab.setObjectName("tab")
        self.subject = QtWidgets.QLineEdit(self.tab)
        self.subject.setGeometry(QtCore.QRect(190, 120, 471, 31))
        self.subject.setObjectName("subject")
        self.rercipientsE = QtWidgets.QLineEdit(self.tab)
        self.rercipientsE.setGeometry(QtCore.QRect(190, 30, 471, 31))
        self.rercipientsE.setObjectName("rercipientsE")
        self.label_2 = QtWidgets.QLabel(self.tab)
        self.label_2.setGeometry(QtCore.QRect(50, 120, 81, 31))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(13)
        font.setBold(True)
        font.setWeight(75)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.label = QtWidgets.QLabel(self.tab)
        self.label.setGeometry(QtCore.QRect(50, 30, 81, 31))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(13)
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.label_3 = QtWidgets.QLabel(self.tab)
        self.label_3.setGeometry(QtCore.QRect(50, 220, 81, 31))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(13)
        font.setBold(True)
        font.setWeight(75)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")
        self.attachment = QtWidgets.QPushButton(self.tab)
        self.attachment.setGeometry(QtCore.QRect(200, 170, 75, 23))
        self.attachment.setObjectName("attachment")
        self.sendE = QtWidgets.QPushButton(self.tab)
        self.sendE.setGeometry(QtCore.QRect(680, 550, 75, 23))
        self.sendE.setObjectName("sendE")
        self.extractErecipients = QtWidgets.QPushButton(self.tab)
        self.extractErecipients.setGeometry(QtCore.QRect(690, 30, 75, 23))
        self.extractErecipients.setObjectName("extractErecipients")
        self.messageE = QtWidgets.QPlainTextEdit(self.tab)
        self.messageE.setGeometry(QtCore.QRect(70, 270, 681, 251))
        self.messageE.setObjectName("messageE")
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
        self.messageText = QtWidgets.QPlainTextEdit(self.tab_2)
        self.messageText.setGeometry(QtCore.QRect(80, 250, 571, 251))
        self.messageText.setObjectName("messageText")
        self.sendM = QtWidgets.QPushButton(self.tab_2)
        self.sendM.setGeometry(QtCore.QRect(700, 280, 75, 23))
        self.sendM.setObjectName("sendM")
        self.label_5 = QtWidgets.QLabel(self.tab_2)
        self.label_5.setGeometry(QtCore.QRect(80, 120, 111, 16))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(13)
        font.setBold(True)
        font.setWeight(75)
        self.label_5.setFont(font)
        self.label_5.setObjectName("label_5")
        self.recipientsm = QtWidgets.QLineEdit(self.tab_2)
        self.recipientsm.setGeometry(QtCore.QRect(260, 110, 231, 31))
        self.recipientsm.setObjectName("recipientsm")
        self.extract_Mrecients = QtWidgets.QPushButton(self.tab_2)
        self.extract_Mrecients.setGeometry(QtCore.QRect(600, 110, 75, 23))
        self.extract_Mrecients.setObjectName("extract_Mrecients")
        self.label_6 = QtWidgets.QLabel(self.tab_2)
        self.label_6.setGeometry(QtCore.QRect(90, 50, 47, 13))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(13)
        font.setBold(True)
        font.setWeight(75)
        self.label_6.setFont(font)
        self.label_6.setObjectName("label_6")
        self.lineEdit = QtWidgets.QLineEdit(self.tab_2)
        self.lineEdit.setGeometry(QtCore.QRect(260, 40, 231, 31))
        self.lineEdit.setObjectName("lineEdit")
        self.tabWidget.addTab(self.tab_2, "")
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        self.tabWidget.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label_2.setText(_translate("MainWindow", "Subject"))
        self.label.setText(_translate("MainWindow", "Recipients:"))
        self.label_3.setText(_translate("MainWindow", "Message"))
        self.attachment.setText(_translate("MainWindow", "Attachment"))
        self.sendE.setText(_translate("MainWindow", "SEND "))
        self.extractErecipients.setText(_translate("MainWindow", "Extract"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab), _translate("MainWindow", "E-mail"))
        self.label_4.setText(_translate("MainWindow", "Your message"))
        self.sendM.setText(_translate("MainWindow", "SEND"))
        self.label_5.setText(_translate("MainWindow", "Recipients"))
        self.extract_Mrecients.setText(_translate("MainWindow", "Extract"))
        self.label_6.setText(_translate("MainWindow", "From"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_2), _translate("MainWindow", "SMS"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())

