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
        MainWindow.resize(998, 662)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.tabWidget = QtWidgets.QTabWidget(self.centralwidget)
        self.tabWidget.setGeometry(QtCore.QRect(10, 10, 901, 651))
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
        self.recipients_email = QtWidgets.QLineEdit(self.tab)
        self.recipients_email.setGeometry(QtCore.QRect(190, 30, 471, 31))
        self.recipients_email.setObjectName("recipients_email")
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
        self.label_3.setGeometry(QtCore.QRect(50, 250, 81, 31))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(13)
        font.setBold(True)
        font.setWeight(75)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")
        self.attachment = QtWidgets.QPushButton(self.tab)
        self.attachment.setGeometry(QtCore.QRect(200, 200, 81, 31))
        self.attachment.setObjectName("attachment")
        self.send_email = QtWidgets.QPushButton(self.tab)
        self.send_email.setGeometry(QtCore.QRect(700, 420, 81, 31))
        self.send_email.setObjectName("send_email")
        self.extract_email_recipients = QtWidgets.QPushButton(self.tab)
        self.extract_email_recipients.setGeometry(QtCore.QRect(690, 30, 81, 31))
        self.extract_email_recipients.setObjectName("extract_email_recipients")
        self.file = QtWidgets.QLineEdit(self.tab)
        self.file.setGeometry(QtCore.QRect(360, 200, 301, 31))
        self.file.setObjectName("file")
        self.message_email = QtWidgets.QTextEdit(self.tab)
        self.message_email.setGeometry(QtCore.QRect(40, 300, 641, 281))
        self.message_email.setObjectName("message_email")
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
        self.send_message = QtWidgets.QPushButton(self.tab_2)
        self.send_message.setGeometry(QtCore.QRect(700, 350, 81, 31))
        self.send_message.setObjectName("send_message")
        self.label_5 = QtWidgets.QLabel(self.tab_2)
        self.label_5.setGeometry(QtCore.QRect(90, 120, 111, 16))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(13)
        font.setBold(True)
        font.setWeight(75)
        self.label_5.setFont(font)
        self.label_5.setObjectName("label_5")
        self.recipient_number = QtWidgets.QLineEdit(self.tab_2)
        self.recipient_number.setGeometry(QtCore.QRect(260, 110, 331, 31))
        self.recipient_number.setObjectName("recipient_number")
        self.extract_message_recipients = QtWidgets.QPushButton(self.tab_2)
        self.extract_message_recipients.setGeometry(QtCore.QRect(710, 110, 81, 31))
        self.extract_message_recipients.setObjectName("extract_message_recipients")
        self.label_6 = QtWidgets.QLabel(self.tab_2)
        self.label_6.setGeometry(QtCore.QRect(90, 50, 47, 13))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(13)
        font.setBold(True)
        font.setWeight(75)
        self.label_6.setFont(font)
        self.label_6.setObjectName("label_6")
        self.user_number = QtWidgets.QLineEdit(self.tab_2)
        self.user_number.setGeometry(QtCore.QRect(260, 40, 331, 31))
        self.user_number.setObjectName("user_number")
        self.message_text = QtWidgets.QTextEdit(self.tab_2)
        self.message_text.setGeometry(QtCore.QRect(90, 240, 511, 271))
        self.message_text.setObjectName("message_text")
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
        self.send_email.setText(_translate("MainWindow", "SEND "))
        self.extract_email_recipients.setText(_translate("MainWindow", "Extract"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab), _translate("MainWindow", "E-mail"))
        self.label_4.setText(_translate("MainWindow", "Your message"))
        self.send_message.setText(_translate("MainWindow", "SEND"))
        self.label_5.setText(_translate("MainWindow", "Recipients"))
        self.extract_message_recipients.setText(_translate("MainWindow", "Extract"))
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

