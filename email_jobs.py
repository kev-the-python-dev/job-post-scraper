from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.application import MIMEApplication

import smtplib
import ssl


contxt = ssl.create_default_context()
password = '#'
sender = '#@gmail.com'
receiver = '#@gmail.com'

message = MIMEMultipart('mixed')
message['Subject'] = 'DB of Job Posts'
message['From'] = sender
message['To'] = receiver

message.attach(MIMEText('DB File', 'plain'))

filename= './db.csv'
with open(filename, 'rb') as db_file:
    file = MIMEApplication(db_file.read())
disposition = f'attachment; filename={filename}'
file.add_header('Content-Disposition', disposition)
message.attach(file)
print('Database attached')

with smtplib.SMTP_SSL('smtp.gmail.com', port=465, context=contxt) as email_server:
    print('Connecting to mail server')
    email_server.login(sender, password)
    print(f'Logging in with appplication password {password}')
    email_server.sendmail(sender, receiver, message.as_string())
    print('Message sent')


