import os
import smtplib

from email.message import EmailMessage

from string import Template
from pathlib import Path

email = EmailMessage()

html = Template(Path('index.html').read_text())
email['from'] = os.environ['from']
email['to'] = os.environ['to']
email['subject'] = 'Hello, this is an Email'

email.set_content(html.substitute(name = os.environ['name']), 'html')

with smtplib.SMTP(host='smtp.gmail.com', port=587) as smtp:
    smtp.ehlo()
    smtp.starttls()
    smtp.login(os.environ['email'], os.environ['password'])
    smtp.send_message(email)
    print('all good')