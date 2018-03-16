import smtplib
from tkinter import *

message="we coordially invite you to our event -GDG VIT"
flag=0
window=Tk()
def logincred():
    label =Label(window, text="MyMail",foreground = "Red", font=("Courier", 30, "bold"))
    label.pack(side="top")
    sublabel =Label(window, text="Bringing you the\n the easiest way of communication",font=("Courier", 15))
    sublabel.pack()

    label1 = Label(window, text="Personal Information", foreground="blue")
    label1.pack(side="top", fill="x", pady=10)
##    global optionv
##    optionv=StringVar()
##    optionv.set("---Select one---")
##    optionm=OptionMenu(window,optionv,"---Select One---","@gmail.com","@yahoo.com","@hotmail.com")
    l1=Label(window,text='USERNAME:')
    l2=Label(window,text='PASSWORD:')
    user=StringVar()
    user.set("")
    t1=Entry(window,textvariable=user)
    passw=StringVar()
    passw.set("")
    
    t2=Entry(window,show='*',textvariable=passw)

    def valid():
        global Password, Email, Server 
        Password =t1.get()
        Email = t2.get()
        Server = smtplib.SMTP("smtp.gmail.com", 587)
        Server.ehlo()
        Server.starttls()
        try:
            Server.login(Email, Password)
            print("Login Succesful")
            window.destroy()
            composemail()
            
        except:
            print("Login Failed")

    b1=Button(window,text='Log-In',command=valid)
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
    print("success mail sent to all")
    server.close()
    
    return


logincred()

if flag==1:
    l5 = Label(window, text='mail sent succesfully')
    l5.pack()
window.mainloop()








