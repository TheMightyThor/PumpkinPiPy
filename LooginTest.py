import logging
import time

index = 0

while index < 20:
    logging.basicConfig(filename='example.log',level=logging.DEBUG, format='%(asctime)s %(message)s')
    logging.debug('This message should go to the log file')
    logging.info('So should this')
    logging.warning('And this, too')
    time.sleep(10)
    index += 1
