#!/usr/bin/python
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.image import MIMEImage
import os

filename = 'E:\\20180223085328.png'
msg = MIMEMultipart()
msg['From'] = 'Me <xxx@xx.com>'
msg['To'] = 'You <xx@163.com>'
msg['Subject'] = 'Your picture'
text = MIMEText("Here's that picture I took of you.")
msg.attach(text)
image = MIMEImage(open(filename, 'rb').read(), name=os.path.split(filename)[1])
msg.attach(image)
print(str(msg))
