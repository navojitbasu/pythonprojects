import smtplib

to = input("Enter the email of the recipent: \n")

content = input("Enter the content for mail: \n")

def sendEmail(to, content):
    server = smtplib.SMTP('smtp.gmail.com', 507)
    server.ehlo()
    server.starttls()
    server.login('senderemail@gmail.com', '1234') #Replace with our own email address
    server.sendmail('senderemail@gmail.com', to, content)
    server.close()

sendEmail(to, content)
