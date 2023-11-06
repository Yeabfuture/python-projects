from email.message import EmailMessage
import ssl
import smtplib
import json

# Load configuration from config.json
with open('C:/python projects/Email Sender/config.json', 'r') as file:
    config = json.load(file)

email_sender = 'youremail@gmail'
email_password = config['email_password']  # Access the password from the config

email_receiver = 'youremail@gmail.com'

subject = "Write your email subject here"

body = '''
This is a sample email body.
'''

em = EmailMessage()
em['From'] = email_sender
em['To'] = email_receiver
em['Subject'] = subject
em.set_content(body)

context = ssl.create_default_context()

with smtplib.SMTP_SSL('smtp.gmail.com', 465, context=context) as smtp:
    smtp.login(email_sender, email_password)
    smtp.sendmail(email_sender, email_receiver, em.as_string())

print("Email sent successfully!")
