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

cam = picamera.PiCamera()


def start_timelapse(numba):

    logging.info('Starting timelapse')

    cam.start_preview()
    time.sleep(1)
    index = 0
    while index < 50:
        imageName = ('%s.jpg' % time.strftime('%H:%M:%S-%m-%d-%Y'))

        cam.capture(imageName)
        cam.stop_preview()

        try:
            logging.info('Uploading %s to server' % imageName)
            uploadtoserver.upload_picture(imageName)
            logging.info('Success uploading to server...Posting %s to server' % imageName)
            postpicture.post_image_to_server(imageName, numba)
            logging.info('Success posting to site')
        except Exception, e:
            logging.error('Error uploading to services %s' % e.message)
            emailerror.send_mail(e.message)

        index += 1
        time.sleep(300)


# schedule.every().day.at("08:00").do(start_timelapse, 1)
# schedule.every().day.at("11:00").do(start_timelapse, 2)
# schedule.every().day.at("14:00").do(start_timelapse, 3)
# schedule.every().day.at("17:00").do(start_timelapse, 4)
#
# while 1:
#     schedule.run_pending()
#     time.sleep(300)
