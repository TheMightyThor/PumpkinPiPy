import requests
import logging
from pumpkinpiconfig import PAPER_PLATE


def post_image_to_server(filename, numba):
    logging.info('posting to website')
    # r = requests.post('http://localhost:5000/api/imageData?name={}&numba={}'.format(filename, numba),headers={'xyz': PAPER_PLATE['noggin']})

    r = requests.post(PAPER_PLATE['commandcenter'] + '/imageData?name={}&numba={}'.format(filename, numba),
                      headers={'xyz': PAPER_PLATE['noggin']})

    logging.info('posted file to site response = %s' % r.text)
