
import requests
import logging
from pumpkinpiconfig import PAPER_PLATE

xyz = PAPER_PLATE['noggin']
def post_image_to_server(fileName):
    logging.info('posting to website')

    r = requests.post(PAPER_PLATE['commandcenter'] + '/imageData?name=%s' % fileName, headers={ 'xyz' : xyz})

    logging.info('posted file to site response = %s' % r.text)