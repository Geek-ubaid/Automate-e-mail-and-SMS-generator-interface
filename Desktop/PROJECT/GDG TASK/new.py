import smtplib
import tkinter
from tkinter import *
window=tkinter.Tk()
email_username=""
email_password=""
subject=""
message=""
flag=0

def logincred():
    l4=Label(window,text='EMAIL CREDENTIALS')
    l1=Label(window,text='USERNAME:')
    l2=Label(window,text='PASSWORD:')
    user=StringVar()
    passw=StringVar()
    t1=Entry(window,textvariable=user)
    t2=Entry(window,show='*',textvariable=passw)

    def valid():
        email_username=t1.get()
        email_password=t2.get()
        if(email_username=='zafarbaba09@gmail.com' and email_password=='dolluamma'):
            l3=Label(window,text='logged in successfully')
            l3.pack()
            composemail()
        else:
            l3=Label(window,text='invalid credentials')
            l3.pack()

    b1=Button(window,text='Log-In',command=valid)
    l4.pack()
    l1.pack()
    t1.pack()
    l2.pack()
    t2.pack()
    b1.pack()

def composemail():
    print(email_password, email_username)
    root=tkinter.Tk()
    l7=Label(root,text='COMPOSE MAIL')
    l1=Label(root,text='SUBJECT')
    l2=Label(root,text='BODY')
    subject=StringVar()
    message=StringVar()
    t1=Entry(root,textvariable=subject)
    t2=Entry(root,textvariable=message)
    def valid():
        u=t1.get()
        v=t2.get()
        if(u!="" or v!=""):
            print('cvbcv')
            sende_mail()
    b1=Button(root,text='Send Mail to all recipients',command=valid)
    l7.pack()
    l1.pack()
    t1.pack()
    l2.pack()
    t2.pack()
    b1.pack()
    root.mainloop()

def sende_mail():
    server=smtplib.SMTP('smtp.gmail.com',587)
    server.ehlo()
    server.starttls()
    server.ehlo()
    server.login(email_username,email_password)
    server.sendmail(email_username,'usmaniubaid@gmail.com',subject,message)
    server.close()
    return


logincred()
'''
if flag==1:
    l5 = Label(window, text='mail sent succesfully')
    l5.pack()
else:
    l5 = Label(window, text='mail not sent')
    l5.pack()
'''
window.mainloop()








