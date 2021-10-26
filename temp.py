from string import Template
from datetime import datetime

from email.mime.multipart import MIMEMultipart #assunto e quem está enviando
from email.mime.text import MIMEText # corpo do email
from email.mime.image import MIMEImage #receber email
import smtplib


with open('template.html', 'r') as html:
    template = Template(html.read())
    data_atual = datetime.now().strftime('%d/%m/%Y')
    corpo_msg = template.substitute(nome='Ane Caroline', data=data_atual)

msg = MIMEMultipart()
msg['from'] = 'Ane Caroline'
msg['to'] = 'anecarolinemaciel7@gmail.com'
msg['subject'] = 'Atenção: este é um email de testes.'

corpo = MIMEText(corpo_msg, 'html') #corpo do texto em html
msg.attach(corpo)

with open('3Sem título.png','rb') as img:
    img = MIMEImage(img.read())
    msg.attach(img)




with smtplib.SMTP(host='smtp.gmail.com', port=587) as smtp: #SERVIDOR DO EMAIL
    smtp.ehlo()
    smtp.starttls()
    smtp.login('nhtyfmajgufl7@gmail.com', '354845157')
    smtp.send_message(msg)
    print('Email enviado com sucesso')
