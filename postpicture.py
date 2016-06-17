
import requests
import logging

def post_image_to_server(fileName):
    logging.info('posting to website')
    r = requests.post('http://desolate-brook-40903.herokuapp.com/api/imageData?name=%s' % fileName, None, None)

    print r.text

