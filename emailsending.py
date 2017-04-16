import smtplib

def start_server(username, password, to, msg, SERVER = 'smtp.gmail.com', port = 587):
    try:
        server = smtplib.SMTP(SERVER, port)
        server.ehlo()
        server.starttls()
        server.login(username,password)

        server.sendmail(username, to, msg)
        server.quit()

        return 1

    except smtplib.SMTPAuthenticationError:
        return 0

    except:
        return -1


