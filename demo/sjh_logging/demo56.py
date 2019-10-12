# -*- encoding: utf-8 -*-
import logging

'''
CRITICAL = 50
ERROR = 40
WARNING = 30
INFO = 20
DEBUG = 10
NOTSET = 0
'''
print(logging.CRITICAL)
logging.critical("message")
print(logging.ERROR)
logging.error("message")
print(logging.WARNING)
logging.warning("message")
print(logging.INFO)
logging.info("message")
print(logging.DEBUG)
logging.debug("message")
print(logging.NOTSET)
