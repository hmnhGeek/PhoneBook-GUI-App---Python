import smtplib
from  email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

def start_server():
    ''' For plain text '''
    loginID = raw_input("Username: ")
    password = raw_input("Password: ")

    try:
        server = smtplib.SMTP('smtp.gmail.com', 587)
        server.ehlo()
        server.starttls()
        server.login(loginID,password)

        msg = raw_input("Message: ")
        to = raw_input("To: ")
        server.sendmail(loginID, to, msg)
        server.quit()

    except smtplib.SMTPAuthenticationError:
        print "Wrong login id or password."

def mimeMail(me, password, SERVER = 'smtp.gmail.com', port = 587):
##    me = raw_input("Username: ")
##    password = raw_input("Enter password: ")

    msg = MIMEMultipart('alternative')
    msg['subject'] = raw_input("Subject: ")
    msg['from'] = me
    msg['To'] = raw_input("To: ")

    text = raw_input("Enter message: ")
    part1 = MIMEText(text, 'plain')
    msg.attach(part1)
    try:
        server = smtplib.SMTP('smtp.gmail.com', 587)
        server.ehlo()
        server.starttls()
        server.login(me,password)

        server.sendmail(me, msg['To'], msg.as_string())
        server.quit()
        print "Sent!!"
    except smtplib.SMTPAuthenticationError:
        print "Sending Failed!!"

    
    
