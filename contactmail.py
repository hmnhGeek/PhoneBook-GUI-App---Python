import smtplib, ttk
from Tkinter import *

def check_credentials(username, password, SERVER = 'smtp.gmail.com', port = 587):
    try:
        server = smtplib.SMTP(SERVER, port)
        server.ehlo()
        server.starttls()
        server.login(username,password)
        server.quit()
        
        return 1

    except smtplib.SMTPAuthenticationError:
        return 0

    except:
        return -1


