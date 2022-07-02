import smtplib
import ssl

contxt = ssl.create_default_context()
password = 'mtmwvwauzcofavcx'
sender = 'jobpostscraperdb@gmail.com'
receiver = 'jobpostscraperdb@gmail.com'

message = ''

with smtplib.SMTP_SSL('smtp.gmail.com', port=465, context=contxt) as email_server:
    email_server.login(sender, password)
    email_server.sendmail(sender, receiver, message)


