def send_with_template(reciever,data,subject,sender):  #subject is optional
    import sendwithus
    api = sendwithus.api(api_key='live_0b13ba36f466dceb99fa1134b1a208a12299b830')#sendwithus API key
    r = api.send(
    email_id='tem_wrMv7tQkY77WRJRxRP4Hc6gB',   #template ID
    recipient= {# give the reciever here
                'address': reciever
              },
    email_data={#you can change the tags and variables here
                'company_name':'DSC VIT',
                'name': data['name'],
                'reg_no':data['regno']
            },
    locale='en-IN'      #specify the location
    
    #you can also add sender details if required
    '''sender={
        'address': sender,
        'reply_to':'info@company.com',  # Optional
        'name': 'Company'  # Optional
            }'''
    #esp_account='Your esp ID'
    #you can also add this param if you want to use email delivering service
     )
    print (r.status_code)   #response code
if __name__=="__main__":
    send_with_template("usmaniubaid@gmail.com",{"name":"Ubaid Usmani","regno":"17BCE0983"},"test","sdfsd")
