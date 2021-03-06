import time
import logging
import smtplib
from email.MIMEMultipart import MIMEMultipart
from email.MIMEText import MIMEText
from pumpkinpiconfig import PAPER_PLATE

FROM = PAPER_PLATE['specialsauce']
TO = PAPER_PLATE['theman']
SUBJECT = 'Error in Pi'
SERVER = 'smtp.mail.yahoo.com'
PORT = 587


def send_mail(error):
    msg = MIMEMultipart()
    msg['From'] = 'SoFloPiInTheSky'
    msg['Subject'] = SUBJECT
    msg['To'] = TO

    text = MIMEText(error)
    msg.attach(text)

    print('connecting to smtp server')
    try:
        s = smtplib.SMTP(SERVER, PORT)
        s.ehlo()
        s.starttls()
        s.ehlo()
        s.login(FROM, PAPER_PLATE['ketchup'])
        s.sendmail(FROM, TO, msg.as_string())
        s.quit()
        logging.info('sent mail!')
    except Exception, ex:
        logging.error('something bad happened error message = %s' % str(ex))

def send_mail_with_video(fileName):
    msg = MIMEMultipart()
    msg['From'] = 'SoFloPiInTheSky'
    msg['Subject'] = SUBJECT
    msg['To'] = TO

    part = MIMEBase('application', "octet-stream")
    part.set_payload(open(fileName, "rb").read())
    Encoders.encode_base64(part)
    part.add_header('Content-Disposition', 'attachment; filename=currentMovie')
    msg.attach(part)
    try:
        s = smtplib.SMTP(SERVER, PORT)
        s.ehlo()
        s.starttls()
        s.ehlo()
        s.login(FROM, PAPER_PLATE['ketchup'])
        s.sendmail(FROM, TO, msg.as_string())
        s.quit()
        logging.info('sent mail!')
    except Exception, ex:
        logging.error('something bad happened error message = %s' % str(ex))
