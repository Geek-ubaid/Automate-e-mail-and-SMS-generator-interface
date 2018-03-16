import sys
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QAction, QLineEdit, QMessageBox, QLabel
from PyQt5.QtCore import pyqtSlot


class main_window(QWidget):

    def __init__(self):
        super().__init__()
        
        self.initUI()
        

    def initUI(self):
        self.resize(1000, 600)
        self.setWindowTitle('GMAIL-EMULATOR')

        #username
        self.sender = QLineEdit(self)
        self.sender.move(20,20)
        self.sender.resize(280,20)
        self.fromlabel = QLabel(self)
        self.fromlabel.setText('GMAIL Username:')
        self.fromlabel.move(20,0)

        #password
        self.password = QLineEdit(self)
        self.password.setEchoMode(QLineEdit.Password)
        self.password.move(20,60)
        self.password.resize(280,20)
        self.passwordlabel = QLabel(self)
        self.passwordlabel.setText('Password:')
        self.passwordlabel.move(20,40)
        

        #to
        self.reciever = QLineEdit(self)
        self.reciever.move(20,140)
        self.reciever.resize(280,20)
        self.recieverlabel = QLabel(self)
        self.recieverlabel.setText('To')
        self.recieverlabel.move(20,120)
        

        #subject
        self.subject = QLineEdit(self)
        self.subject.move(20,180)
        self.subject.resize(280,20)
        self.subjectlabel = QLabel(self)
        self.subjectlabel.setText('Subject:')
        self.subjectlabel.move(20,160)
        
        #text
        self.text = QLineEdit(self)
        self.text.move(20,220)
        self.text.resize(280,20)
        self.textlabel = QLabel(self)
        self.textlabel.setText ('Body:')
        self.textlabel.move(20,200)

        #repetetions
        self.iterations = QLineEdit(self)
        self.iterations.move(20,260)
        self.iterations.resize(80,20)
        self.itlabel = QLabel(self)
        self.itlabel.setText('# Of Times Email Sent:')
        self.itlabel.move(20,240)

        #create button
        spambutton = QPushButton("SEND", self)
        spambutton.setToolTip("Press to send email")
        spambutton.move(500,500)
        spambutton.clicked.connect(self.on_click)

        
        self.show()



    @pyqtSlot()
    def on_click(self):
        send_email.send_email(str(self.sender.text()), str(self.password.text()), str(self.reciever.text()), str(self.subject.text()), str(self.text.text()), int(self.iterations.text()))


#starts main loop
if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = main_window()

    sys.exit(app.exec_())
    
