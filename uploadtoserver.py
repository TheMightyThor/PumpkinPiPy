import boto
from boto.s3.key import Key
from pumpkinpiconfig import PAPER_PLATE


def upload_picture(filename):

    s3_connection = boto.connect_s3(PAPER_PLATE['peanutbutter'], PAPER_PLATE['jelly'])
    bucket = s3_connection.get_bucket(PAPER_PLATE['bread'])

    k = Key(bucket)
    k.key = filename
    k.set_contents_from_filename(filename, policy='public-read')
    k.make_public()


