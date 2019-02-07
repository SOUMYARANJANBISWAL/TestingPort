# Python Program to Get IP Address 
import socket    
hostname = socket.gethostname()    
IPAddr = socket.gethostbyname(hostname)    
print("Your Computer Name is:" + hostname)    
print("Your Computer IP Address is:" + IPAddr)   


#sending mail
import smtplib
sender = 'from@fromdomain.com'
receivers = ['to@todomain.com']
message = """From: From Person <from@fromdomain.com>
To: To Person <to@todomain.com>
Subject: SMTP e-mail test
This is a test e-mail message.
"""
try:
   smtpObj = smtplib.SMTP('localhost')
   smtpObj.sendmail(sender, receivers, message)         
   print "Successfully sent email"
except SMTPException:
   print "Error: unable to send email"
    
import smtplib
from email.mime.text import MIMEText
fromx = 'xxx@gmail.com'
to  = 'xxx@gmail.com'
msg = MIMEText('example')
msg['Subject'] = 'subject'
msg['From'] = fromx
msg['To'] = to
body = "Body_of_the_mail"
msg.attach(MIMEText(body, 'plain'))
server = smtplib.SMTP('smtp.gmail.com:587')
server.starttls()
server.ehlo()
server.login('xxx@gmail.com', 'xxx')
server.sendmail(fromx, to, msg.as_string())
server.quit()
