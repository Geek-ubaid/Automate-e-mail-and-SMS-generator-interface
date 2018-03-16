import smtplib
from tkinter import *
email_username="zafarbaba09@gmail.com"
email_password="Ub@!d120898"
message="we coordially invite you to our event -GDG VIT"
flag=0
window=Tk()
def logincred():
    l4=Label(window,text='EMAIL CREDENTIALS')
    l1=Label(window,text='USERNAME:')
    l2=Label(window,text='PASSWORD:')
    user=StringVar()
    passw=StringVar()
    t1=Entry(window,textvariable=user)
    t2=Entry(window,show='*',textvariable=passw)

    def valid():
        global email_username
        global email_password
        email_username=t1.get()
        email_password=t2.get()
        if(email_username=='zafarbaba09@gmail.com' and email_password=='Ub@!d120898'):
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
    root=Tk()
    l7=Label(root,text='COMPOSE MAIL')
    l1=Label(root,text='SUBJECT')
    l2=Label(root,text='BODY')
    subj=StringVar()
    mess=StringVar()
    t1=Entry(root,textvariable=subj)
    t2=Entry(root,textvariable=mess)
    global message
    global subject
    subject=t1.get()
    message=t2.get()
    def valid():
        u=t1.get()
        v=t2.get()
        if(u!="" or v!=""):
            sendemail()
    b1=Button(root,text='Send Mail to all recipients',command=valid)
    l7.pack()
    l1.pack()
    t1.pack()
    l2.pack()
    t2.pack()
    b1.pack()
    root.mainloop()

def sendemail():
    server=smtplib.SMTP('smtp.gmail.com',587)
    server.ehlo()
    server.starttls()
    server.login(email_username,email_password)
    global flag
    f=open("mail.txt")
    for i in f.readlines():
        server.sendmail(email_username,i,message)
        flag=1
    server.close()
    return


logincred()

if flag==1:
    l5 = Label(window, text='mail sent succesfully')
    l5.pack()
else:
    l5 = Label(window, text='mail not sent')
    l5.pack()
window.mainloop()








