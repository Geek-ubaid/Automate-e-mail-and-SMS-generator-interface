import sys
import string
from PyQt5 import QtGui,QtWidgets,QtCore
    #importing interface
from PROJECT.GUI import main
from PROJECT.GUI import login
class Loginwindow(QtWidgets.QDialog,login.Ui_loginwindow):

    def __init__(self):
        super().__init__()
        self.setupUi(self)

        self.setWindowIcon(self,QtGui.QIcon(r'C:\Users\UBAID USMANI\Desktop\PROJECT\gdg.png'))

        self.login.clicked.connect(self.logincheck)
        self.reset.clicked.connect(self.resetcheck)

    def logincheck(self):
        passget = self.pass1.text()
        userget = self.user.text()
        if (userget == "asd" and passget == "qwe"):
            try:
                self.window=Automater()
                self.window.show()
            except:
                showmessagebox(2)
                self.resetcheck()
                self.close()

        else:
            if(showmessagebox(1) == Close):
                self.close()
                if(showmessagebox(4) == Yes):
                    app.quit()
                else:
                    self.close()

    def resetcheck(self):
        self.pass1.setText("")
        self.user.setText("")
    


class Automater(QtWidgets.QMainWindow,main.Ui_MainWindow):
    def _init_(self):
        super(Automater, self)._init_()
        self.setupUi(self)
        self.setWindowIcon(self,QtGui.QIcon(r'C:\Users\UBAID USMANI\Desktop\PROJECT\gdg.png'))
        self.Email_recipients.clicked.connect(self.Email_extract)
        self.Message_recipients.clicked.connect(self.contact_extract)
        self.attachment.clicked.connect(self.open_file)
        self.Send_Message.clicked.connect(self.sendmessage)
        self.Send_Email.clicked.connect(self.sendmail)

    def open_file(self):
        global file_name
        import os
        filename, _ = QtWidgets.QFileDialog.getOpenFileName(self, 'Open File',None, QFileDialog.DontUseNativeDialog)
        file_dir=str(QtWidgets.QFileDialog.getExistingDirectory())
        file_size=os.path.getsize('r'+file_dir)
        if (file_size> 26,214,400):
            showmessagebox(6)
            self.close()

    def contact_extract(self):
        rec = self.recipientsm.text()
        if (rec.split(".")[1] == "txt"):
            with open(rec, "r") as file:
                self.dic1 = {}
                for i in file.readlines():
                # the csv format shoulf be like name regno phoneno emailaddress
                    l = i.split(" ")
                    self.dic1[l[2]] = (l[0], l[1])
            if(showmessagebox(3)==Ok):
                self.close()

        else:
            showmessagebox(5)
            self.close()

    def Email_extract(self):
        recm = self.recipients.text()
        if (str(recm)[len(recm) - 4::] == ".txt"):
            with open(recm, "r") as file:
                self.dic2 = {}
                for i in file.readlines():
                    l = i.split(" ")
                    self.dic[l[3]] = (l[0], l[1])
            if(showmessagebox(3)==Ok):
                self.close()
        else:
            showmessagebox(5)
            self.close()

    def sendmail(self):
        message = self.messageE.text()
        print(message)
        for i in self.dic2.keys():
            print(i)
            message = message.replace('#studentname', self.dic2[i][0])
            message = message.replace('#regno', self.dic2[i][1])



    def sendmessage(self):
        Textmessage = self.messageText.text()
        print(Textmessage)
        for i in self.dic1:
            print(i)
            Textmessage = Textmessage.replace('#studentname', self.dic1[i][0])
            Textmessage = Textmessage.replace('#regno', self.dic1[i][1])
            print(Textmessage)

Yes=QtWidgets.QMessageBox.Yes
Ok=QtWidgets.QMessageBox.Ok
def showmessagebox():
    msg = QtWidgets.QMessageBox()
    msg.setWindowTitle("Status Window")
    msg.setIcon(QtWidgets.QMessageBox.Information)

    if x == 1:
        msg.setText('Invalid Credentials')
        msg.setStandardButtons(QtWidgets.QMessageBox.Ok | QtWidgets.QMessageBox.Close)
    if x == 2:
        msg.setText('Erorr in login!!')
        msg.setStandardButtons(QtWidgets.QMessageBox.Ok)
    if x== 3:
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
    app = QtGui.QGuiApplication(sys.argv)
    window= Loginwindow()
    window.show()
    sys.exit(app.exec_())