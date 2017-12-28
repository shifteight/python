import logging

# add filemode='w' to overwrite
logging.basicConfig(filename='sample.log', level=logging.INFO)

logging.debug('This is a debug message')
logging.info('Informational message')
logging.error('An error has occurred!')

log = logging.getLogger('ex')

try:
    raise RuntimeError
except RuntimeError:
    log.exception('Error!')
