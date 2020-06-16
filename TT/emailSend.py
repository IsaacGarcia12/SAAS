from socket import gethostname
from email.mime.application import MIMEApplication
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import smtplib
import json

server = smtplib.SMTP('smtp.gmail.com', 587)
server.starttls()
server.login('cob.log.cof@gmail.com', 'graveworm')
    
    # Craft message (obj)
msg = MIMEMultipart()
message = 'Your results are ready'
msg['Subject'] = 'SAAS results'
msg['From'] = 'cob.log.cof@gmail.com'
msg['To'] = 'isaacgama120392@outlook.com'
    
    # Insert the text to the msg going by e-mail
msg.attach(MIMEText(message, "plain"))
    # Attach the pdf to the msg going by e-mail
with open("/home/isaac/Escritorio/SAmin/TT/PDF_Prueba2020-Jun-15__14_04_39.pdf", "rb") as f:
    leer = f.read()
    attach = MIMEApplication(leer,_subtype="pdf")
            #attach = email.mime.application.MIMEApplication(f.read(),_subtype="pdf")
attach.add_header('Content-Disposition','attachment',filename=str("/home/isaac/Escritorio/SAmin/TT/PDF_Prueba2020-Jun-15__14_04_39.pdf"))
msg.attach(attach)
        # send msg
server.send_message(msg)