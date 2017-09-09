import picamera
import logging
import time
import schedule
import uploadtoserver
import postpicture
import emailerror

logging.basicConfig(filename='pumpkinpi.log', level=logging.DEBUG, format='%(asctime)s %(message)s')
logging.getLogger().addHandler(logging.StreamHandler())
logging.info('script has been loaded waiting to start loop')


def start_timelapse(numba):

    logging.info('Starting timelapse')

    index = 0
    with picamera.PiCamera() as cam:
        while index < 1:
            cam.start_preview()
            time.sleep(1)
            impage_name = ('%s.jpg' % time.strftime('%H:%M:%S-%m-%d-%Y'))
            cam.vflip = True
            cam.capture(impage_name, resize=(1920, 1080))
            cam.stop_preview()

            try:
                logging.info('Uploading %s to server' % impage_name)
                uploadtoserver.upload_picture(impage_name)
                logging.info('Success uploading to server...Posting %s to server' % impage_name)
                postpicture.post_image_to_server(impage_name, numba)
                logging.info('Success posting to site')
            except Exception, e:
                logging.error('Error uploading to services %s' % e.message)
                emailerror.send_mail(e.message)

            index += 1
            logging.info("index = " + str(index) + " numba = " + str(numba))



schedule.every().day.at("08:00").do(start_timelapse, 1)
schedule.every().day.at("09:00").do(start_timelapse, 2)
schedule.every().day.at("10:00").do(start_timelapse, 3)
schedule.every().day.at("11:00").do(start_timelapse, 4)
schedule.every().day.at("12:00").do(start_timelapse, 5)
schedule.every().day.at("13:00").do(start_timelapse, 5)
schedule.every().day.at("14:00").do(start_timelapse, 6)
schedule.every().day.at("15:00").do(start_timelapse, 7)
schedule.every().day.at("16:00").do(start_timelapse, 8)
schedule.every().day.at("17:00").do(start_timelapse, 9)
schedule.every().day.at("18:00").do(start_timelapse, 10)
schedule.every().day.at("19:00").do(start_timelapse, 11)
while 1:
    schedule.run_pending()
    time.sleep(60)
