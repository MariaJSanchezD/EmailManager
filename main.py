import smtplib

from email.message import EmailMessage

from string import Template
from pathlib import Path

email = EmailMessage()

html = Template(Path('index.html').read_text())
email['from'] = 'Maria Sanchez'
email['to'] = 'y_loz@gmail.com'
email['subject'] = 'Hello, this is an Email'

email.set_content(html.substitute(name = 'Yushen'), 'html')

with smtplib.SMTP(host='smtp.gmail.com', port=587) as smtp:
    smtp.ehlo()
    smtp.starttls()
    smtp.login('pythonpracticexd@gmail.com', '123456Pp')
    smtp.send_message(email)
    print('all good')