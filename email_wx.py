import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

target_email = 'dcerta@oneeightycapital.com'
email_address = 'nash.wx.python@gmail.com'
email_password = 'NashWx007!!'
smpt_address = 'smtp-relay.gmail.com'
smpt_port = 587

def sendMail(messageText):
    s = smtplib.SMTP(host = f'{smpt_address}', port = f'{smpt_port}')
    s.starttls()
    s.login(email_address, email_password)

    msg = MIMEMultipart()
    msg['From'] = email_address
    msg['To'] = target_email
    msg['Subject'] = 'Nashville Weather - Brought To You By Python'
    msg['Body'] = messageText
    msg.attach(MIMEText(messageText, 'plain'))
    # print(msg)
    s.send_message(msg)
    del msg

    s.quit()
