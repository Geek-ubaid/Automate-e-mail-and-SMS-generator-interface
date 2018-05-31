import csv
from PyQt5 import QtGui,QtWidgets,QtCore
#importing interface
from PROJECT.GUI.login import Ui_loginwindow
from PROJECT.GUI.main import Ui_MainWindow
import template_email,mailto,textlocal
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
        if (userget == "set username" and passget == "set password"):
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
                    app.quit()
                else:
                    pass
    def resetcheck(self):
        self.pass1.setText("")
        self.user.setText("")

Yes=QtWidgets.QMessageBox.Yes
ok=QtWidgets.QMessageBox.Ok
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
    if x == 7:
        msg.setText('All Mail sent successfully')
        msg.setStandardButtons(QtWidgets.QMessageBox.Ok)
    return msg.exec_()
    


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
        finish = QtWidgets.QAction("Quit",self)
        finish.triggered.connect(self.closeEvent)

    def closeEvent(self, event):
        close=showmessagebox(4)
        if close == Yes:
            event.accept()
        else:
            event.ignore()
            self.window = Automater()
            self.close()
            self.window.show()

    def open_file(self):
        import os
        options = QtWidgets.QFileDialog.Options()
        options |= QtWidgets.QFileDialog.DontUseNativeDialog
        self.fileName, _ = QtWidgets.QFileDialog.getOpenFileName(self, "Select File to upload", "","All Files (*);;Python Files (*.py)", options=options)
        try:
            file_size=os.path.getsize(self.fileName)
            if (file_size> 26214400):
                showmessagebox(6)
                self.close()
            else:
                self.file.setText(self.fileName)
                print("file attached")
        except:
            pass

    def contact_extract(self):
        message_rec = self.recipient_number.text()
        if (message_rec.split(".")[1] == "txt"):
            with open(message_rec, "r") as file:
                self.phone_number={}
                for i in file.readlines():
                    l = i.split(" ")
                    self.phone_number[l[2].strip()] = (l[0].strip(), l[1].strip())
            try:
                if(showmessagebox(3)== ok):
                    pass
            except:
                pass

        else:
            if(showmessagebox(5) == ok):
                pass


    def Email_extract(self):
        mail_rec = self.recipients_email.text()
        if (mail_rec.split(".")[1] == "txt"):
            with open(mail_rec, "r") as file:
                self.email_id={}
                for i in file.readlines():
                    l = i.split(" ")
                    self.email_id[l[3].strip()] = (l[0].strip(), l[1].strip())

            try:
                if(showmessagebox(3)== ok):
                    pass
            except:
                pass

        else:
            if(showmessagebox(5) == ok):
                pass

    def sendmail(self):
        email = self.message_email.toPlainText()
        sub = self.subject.text()
        sender="gdgvit@vitstudent.ac.in"
        #mail without html body, for using this uncomment it and comment the template email part
        '''for i in self.email_id.keys():
             temp = email
             temp = temp.replace('#studentname', self.email_id[i][0])  
             temp = temp.replace('#regno', self.email_id[i][1])
             try:
                 mailto.mail(sender,i,temp,sub)
                 print("mail send to",i)
             except:
                 print("Mail not send to",i)
        '''
        #template email part
        for i in self.email_id.keys():
            data={"name":self.email_id[i][0],"regno":self.email_id[i][1])
            try:
                template_email(i,data,aub,sender)
                print("Mail sent to",i)
            except:
                print("Mail not sent to ",i)
        if(showmessagebox(7)==ok):
            self.window = Automater()
            self.close()
            self.window.show()

    def sendmessage(self):
        Textmessage = self.message_text.toPlainText()
        sender_number=self.user_number.text()
        for i in self.phone_number.keys():
            temp=Textmessage
            temp = temp.replace('#studentname', self.phone_number[i][0])
            temp = temp.replace('#regno', self.phone_number[i][1])
            try:
                textlocal.message(i,temp)
                print("Message sent to", i)
            except:
                print("Mail not sent to",i)
    
        if(showmessagebox(7)==ok):
            self.window = Automater()
            self.close()
            self.window.show()



if __name__ == '__main__':
    import sys
    global app
    app = QtWidgets.QApplication(sys.argv)
    window= Loginwindow()
    window.show()
    sys.exit(app.exec_())
