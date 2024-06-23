import smtplib
from email.mime.text import MIMEText
import os

smtp_server = 'smtp.gmail.com'
smtp_port = 587
smtp_username = os.environ.get('MAIL_USERNAME')
smtp_password = os.environ.get('MAIL_PASSWORD')

msg = MIMEText('This is a test email')
msg['Subject'] = 'Test Email'
msg['From'] = smtp_username
msg['To'] = '<example@example.com>'

try:
    server = smtplib.SMTP(smtp_server, smtp_port)
    server.starttls()
    server.login(smtp_username, smtp_password)
    server.sendmail(smtp_username, ['example@example.com'], msg.as_string())
    server.quit()
    print('Mail sent successfully')
except Exception as e:
    print(f'Failed to send mail: {e}')
