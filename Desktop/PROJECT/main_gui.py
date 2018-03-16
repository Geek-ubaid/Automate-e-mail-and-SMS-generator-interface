import csv
from PyQt5 import QtGui,QtWidgets,QtCore
    #importing interface
from PROJECT.GUI.login import Ui_loginwindow
from PROJECT.GUI.main import Ui_MainWindow
import new
class Loginwindow(QtWidgets.QDialog,Ui_loginwindow):

    def __init__(self,parent=None):
        super(Loginwindow, self).__init__(parent)
        self.setupUi(self)
        self.setWindowIcon(QtGui.QIcon(r'gdg.png'))
        self.setWindowTitle("GOOGLE DEVELOPERS GROUP")
        self.login.clicked.connect(self.logincheck)
        self.reset.clicked.connect(self.resetcheck)

    def logincheck(self):
        passget = self.pass1.text()
        userget = self.user.text()
        if (userget == "asd" and passget == "qwe"):
            try:
                self.window= Automater(self)
                self.close()
                self.window.show()
            except:
                showmessagebox(2)
                self.resetcheck()
                pass
        else:
            if(showmessagebox(1) == Close):
                if(showmessagebox(4) == Yes):
                    sys.exit()
                else:
                    pass
    def resetcheck(self):
        self.pass1.setText("")
        self.user.setText("")
    


class Automater(QtWidgets.QMainWindow,Ui_MainWindow):
    def __init__(self,parent=None):
        super(Automater, self).__init__(parent)
        self.setupUi(self)
        self.setWindowIcon(QtGui.QIcon(r'gdg.png'))
        self.setWindowTitle("Email/Message Wizard")
        self.extract_email_recipients.clicked.connect(self.Email_extract)
        self.extract_message_recipients.clicked.connect(self.contact_extract)
        self.attachment.clicked.connect(self.open_file)
        self.send_message.clicked.connect(self.sendmessage)
        self.send_email.clicked.connect(self.sendmail)

    def open_file(self):
        import os
        options = QtWidgets.QFileDialog.Options()
        options |= QtWidgets.QFileDialog.DontUseNativeDialog
        self.fileName, _ = QtWidgets.QFileDialog.getOpenFileName(self, "Select File to upload", "","All Files (*);;Python Files (*.py)", options=options)

        file_size=os.path.getsize(self.fileName)
        if (file_size> 26214400):
            showmessagebox(6)
            self.close()
        else:
            self.file.setText(self.fileName)
            print("file attached")

    def contact_extract(self):
        message_rec = self.recipient_number.text()
        if (message_rec.split(".")[1] == "txt"):
            with open(message_rec, "r") as file:
                self.phone_number={}
                for i in file.readlines():
                    l = i.split(" ")
                    self.phone_number[l[2]] = (l[0], l[1])
                try:
                    if(showmessagebox(3)==Ok):
                        self.close()
                except:
                    print(1)
        else:
            showmessagebox(5)
            self.close()


    def Email_extract(self):
        mail_rec = self.recipients_email.text()
        if (mail_rec.split(".")[1] == "txt"):
            with open(mail_rec, "r") as file:
                self.email_id={}
                for i in file.readlines():
                    l = i.split(" ")
                    self.email_id[l[3].strip()] = (l[0].strip(), l[1].strip())
        else:
            showmessagebox(5)
            self.close()

    def sendmail(self):
        email = self.message_email.toPlainText()
        sub=self.subject.text()
        for i in self.email_id.keys():
            temp=email
            temp = temp.replace('#studentname', self.email_id[i][0])
            temp = temp.replace('#regno', self.email_id[i][1])
            new.logincred(i,temp,sub,self.filename)






    def sendmessage(self):
        Textmessage = self.message_text.toPlainText()
        sender_number=self.user_number.text()
        for i in self.phone_number.keys():
            temp=Textmessage
            temp = temp.replace('#studentname', self.phone_number[i][0])
            temp = temp.replace('#regno', self.phone_number[i][1])
            print(temp)

Yes=QtWidgets.QMessageBox.Yes
Ok=QtWidgets.QMessageBox.Ok
Close=QtWidgets.QMessageBox.Close

def showmessagebox(x):
    msg = QtWidgets.QMessageBox()
    msg.setWindowTitle("Status Window")
    msg.setIcon(QtWidgets.QMessageBox.Information)

    if x == 1:
        msg.setText('Invalid Credentials')
        msg.setStandardButtons(QtWidgets.QMessageBox.Ok | QtWidgets.QMessageBox.Close)
    if x == 2:
        msg.setText('Erorr in login!!')
        msg.setStandardButtons(QtWidgets.QMessageBox.Ok)
    if x == 3:
        msg.seText('Recipients added succesfully!')
        msg.setStandardButtons(QtWidgets.QMessageBox.Ok)
    if x == 4:
        msg.setText('Are you sure you wanna exit?')
        msg.setIcon(QtWidgets.QMessageBox.Question)
        msg.setStandardButtons(QtWidgets.QMessageBox.Yes | QtWidgets.QMessageBox.No)
    if x == 5:
        msg.setText('File no longer exists!')
        msg.setStandardButtons(QtWidgets.QMessageBox.Ok)
    if x == 6:
        msg.setText('Size of file exceeded! Select another file')
        msg.setIcon(QtWidgets.QMessageBox.Warning)
        msg.setStandardButtons(QtWidgets.QMessageBox.Ok)
    return msg.exec_()


if __name__ == '__main__':
    import sys
    global app
    app = QtWidgets.QApplication(sys.argv)
    window= Loginwindow()
    window.show()
    sys.exit(app.exec_())
