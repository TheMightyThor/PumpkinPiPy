import picamera
import logging
import time
import schedule
import uploadtobucket
import postpicture



logging.basicConfig(filename='pumpkinpi.log', level=logging.DEBUG, format='%(asctime)s %(message)s')

logging.info('script has been loaded waiting to start loop')


def start_timelapse():
    PICTURE_FILENAMES = []
    with picamera.PiCamera() as cam:
        counter = 1

        while counter < 48:
            cam.start_preview()
            time.sleep(1)

            imageName = ('%s.jpg' % time.strftime('%H:%M:%S-%m-%d-%Y'))

            cam.capture(imageName, resize=(1024, 768))

            try:
                logging.info('Uploading %s to AWS' % imageName)
                print('uploading to aws')
                uploadtobucket.upload_picture(imageName)
                logging.info('Posting %s to server' % imageName)
                print('uploading to server')
                postpicture.post_image_to_server(imageName)
            except Exception, e:
                logging.error('Error uploading to services')
                print('something happened' + str(e))

            PICTURE_FILENAMES.append(imageName)

            cam.stop_preview()
            if counter % 20 == 0:
                logging.info('Emailing bros')
                # emailbros.send_mail(PICTURE_FILENAMES)
                PICTURE_FILENAMES = []
            time.sleep(1800)
            counter += 1


schedule.every().day.at("08:00").do(start_timelapse)

schedule.run_pending()
