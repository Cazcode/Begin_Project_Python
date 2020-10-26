import smtplib

GMAIL_USER = 'ingcastro214@gmail.com'
GMAIL_PASSWORD = 'Colombia12345'
FROM_EMAIL = GMAIL_USER

TO = ['carloscastro010@gmail.com']
SUBJECT = 'Tema del Correo'
BODY = 'Contenido del Correo'

MAIL = """
From: {}
To: {}
Subject: {}

{}
""".format(FROM_EMAIL, TO, SUBJECT, BODY)

try:
    server = smtplib.SMTP_SSL('smtp.gmail.com', 465)
    server.ehlo()
    server.login(GMAIL_USER, GMAIL_PASSWORD)
    server.sendmail(FROM_EMAIL, TO, MAIL)
    server.close()
    print('Correo enviado!')
except Exception as e:
    print('Error al enviar correo: ', e)