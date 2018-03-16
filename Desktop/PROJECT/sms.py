import nexmo
NEXMO_API_KEY='e03d14a5'
NEXMO_API_SECRET='bkxpUadCp2fCythb'

client = nexmo.Client(key=NEXMO_API_KEY, secret=NEXMO_API_SECRET)
response=client.send_message({
    'from': 'Acme Inc',
    'country' : 'IN',
    'to': '+917905438879',
    'text': 'A text message sent using the Nexmo SMS API',
})
print(response)