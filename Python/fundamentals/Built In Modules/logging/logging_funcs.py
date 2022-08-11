import logging

logging.debug('This is a debug message')
logging.info('This is an info message')
logging.warning('This is a warning message')  # By default messages of level warning and above are logged
logging.error('This is an error message')
logging.critical('This is a critical message')

# https://docs.python.org/3/library/logging.html#logrecord-attributes

#  Example:
logging.basicConfig(filename='test.log', level=logging.DEBUG,
                    format='%(asctime)s:%(levelname)s:%(message)s')  # Log result will show human readable time, severity level and the message