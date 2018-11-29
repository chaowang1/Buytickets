# -*- coding:utf-8 -*-

import os

webroot = os.path.abspath(os.path.join(__file__, os.pardir, os.pardir))

DEBUG = True
HOST = '0.0.0.0'
PORT = '8008'
__version__ = '1.0.0'

DB_ECHO = False

DB_URI = 'sqlite3://{}'.format(webroot)





