import smtplib

def sendEmail():
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.starttls()
    server.login('senderEmail', 'password')
    server.sendEmail(senderEmail, to, 'Testing email automation')
    server.close()             
                 

sendEmail()