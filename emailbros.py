import time
import logging
import smtplib
from email.MIMEMultipart import MIMEMultipart
from email.MIMEText import MIMEText
from email.mime.image import MIMEImage
from pumpkinpiconfig import PAPER_PLATE

FROM = PAPER_PLATE['specialsauce']
TO = PAPER_PLATE['bros']
SUBJECT = 'Pool Pictures '
SERVER = 'smtp.mail.yahoo.com'
PORT = 587
PICTURE_FILENAMES = []


def send_mail(filenames):
        PICTURE_FILENAMES = filenames

        msg = MIMEMultipart()
        msg['From'] = 'SoFloPiInTheSky'
        msg['Subject'] = SUBJECT + time.strftime('%H:%M %p')
        msg['To'] = TO

        text = MIMEText('Check out all the cool stuff going on at the pool for the last hour!')
        msg.attach(text)
        for filename in PICTURE_FILENAMES:
                image_data = open(filename, 'rb').read()
                msg.attach(MIMEImage(image_data, filename))
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