import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import sys

#in gmail settings of your account make sure to 'allow less secure apps' option to be 'ON'

#to parse csv file

def logincred():
#to get login credentials
    eid=input("Enter admin email address:  ")
    epass=input("Enter password:  ")
    global mail
    mail = smtplib.SMTP('smtp.gmail.com', 587)  # to inititalise smtp server and port
    mail.ehlo()  # for ESMTP encryption
    mail.starttls()  # transport security layer for encryption
    try:
        mail.login(eid, epass)  # login credentials
    except:
        print("Invalid credentials, try logging in again or in gmail settings of your account allow less secure apps option to be ON")
        sys.exit()
    message=input()

#to set up SMTP server and login
    msg=MIMEMultipart()
    body=message
    msg.attach( MIMEText(body,'plain') )
    try:
        mail.sendmail(eid,'usmaniubaid@gmail.com',msg.as_string() )        #to send a mail
    except:   # to raise an exception when there is failure in mail delivery
        print("invalid")
        pass
    mail.close()
logincred()

