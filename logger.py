# coding: utf-8
'''
Logger Module
'''

import logging
import logging.handlers
import os

LOG_MAX = 1024 * 1024 * 10
BACKUP_COUNT = 5
LOG_FORMAT = logging.Formatter(
    '%(asctime)s %(filename)s[line:%(lineno)d] %(levelname)s %(message)s', '%Y-%m-%d %H:%M:%S')

def _get_filehandler(name):
    base_path = os.path.dirname(os.path.realpath(__file__))
    logs_dir = os.path.join(base_path, 'logs')
    if not os.path.exists(logs_dir):
        os.makedirs(logs_dir)
    filename = '%s.log' % name
    logger_file = os.path.join(logs_dir, filename)
    file_handler = logging.handlers.RotatingFileHandler(
        logger_file, maxBytes=LOG_MAX, backupCount=BACKUP_COUNT)
    file_handler.setFormatter(LOG_FORMAT)
    return file_handler


def get_logger(name, level=logging.INFO):
    '''
    return logger
    '''
    logger = logging.getLogger(name)
    logger.setLevel(level)
    file_handler = _get_filehandler(name)
    logger.addHandler(file_handler)
    return logger

if __name__ == '__main__':
    my_logger = get_logger('my_logger')
    my_logger.info('this is a info')
    my_logger.debug('this is a debug')