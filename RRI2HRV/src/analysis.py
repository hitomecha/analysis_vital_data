# -*- Coding: utf-8 -*-
import pandas as pd
import numpy as np
from logging import StreamHandler, DEBUG, Formatter, FileHandler, getLogger

logger = getLogger(__name__)

DIR = 'result_tmp/'
PATH = '../data/raw/'


def read_csv(file, header=0):
    logger.debug('enter')
    df = pd.read_csv(file, header=header)
    logger.debug('exit')
    return df


if __name__ == '__main__':
    log_fmt = Formatter('%(asctime)s %(name)s %(lineno)d [%(levelname)s][%(funcName)s] %(message)s ')
    handler = StreamHandler()
    handler.setLevel('INFO')
    handler.setFormatter(log_fmt)
    logger.addHandler(handler)

    handler = FileHandler(DIR + 'train.py.log', 'a')
    handler.setLevel(DEBUG)
    handler.setFormatter(log_fmt)
    logger.setLevel(DEBUG)
    logger.addHandler(handler)

    logger.info('start')
    logger.info('data load end')
