import boto
import logging
from boto.s3.key import Key
from pumpkinpiconfig import PAPER_PLATE


def upload_picture(fileName):
    print(' starting upload uploading to server')
    s3_connection = boto.connect_s3(PAPER_PLATE['peanutbutter'], PAPER_PLATE['jelly'])
    bucket = s3_connection.get_bucket(PAPER_PLATE['bread'])

    k = Key(bucket)
    k.key = fileName
    k.set_contents_from_filename(fileName, policy='public-read')
    k.make_public()
    logging.info('success upload to bucket')
    print('upload to server was success')

