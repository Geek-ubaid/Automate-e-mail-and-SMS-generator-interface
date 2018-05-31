
# using SendGrid's Python Library
# https://github.com/sendgrid/sendgrid-python

import sendgrid
import os
from sendgrid.helpers.mail import *


def mail(sender,to,message,subject):
    sg = sendgrid.SendGridAPIClient(apikey='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')
    from_email = Email(sender)
    to_email = Email(to)
    content = Content("text/plain",message)
    
    try:
        mail = Mail(from_email, subject, to_email, content)
        response = sg.client.mail.send.post(request_body=mail.get())
        print(response.status_code)
        print(response.body)
        print(response.headers)
    except:
        pass
if __name__  == "__main__":
    wmail("usmaniubaid@gmail.com","ubaid.usmani2017@vitstudent.ac.in","hello","test")