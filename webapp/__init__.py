# -*- coding:utf-8 -*-

import os
import string
import random
from flask import Flask
from flask_docs import ApiDoc
from contextlib import contextmanager
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from config import webconfig as config


app = Flask(__name__,
            static_folder=os.path.abspath(os.path.join(config.webroot, 'static')),
            static_url_path="",
            template_folder=os.path.abspath(os.path.join(config.webroot, 'templates'))
            )

app.config.from_object(config)

app.secret_key = ''.join(random.choice(string.ascii_uppercase + string.digits + string.ascii_lowercase, k=40))

app.config['API_DOC_MEMBER'] = ['ticket']
app.config['RESTFUL_API_DOC_EXCLUDE'] = []
ApiDoc(app)

engine = create_engine(app.config['DB_URI'] + '?charset=utf8',
                       encoding='utf-8',
                       convert_unicode=True,
                       echo=app.config['DB_ECHO'],
                       pool_pre_ping=True,
                       )

session_factory = sessionmaker(bind=engine)


@contextmanager
def session_scope():
    session = session_factory()
    try:
        yield session
        session.commit()
    except:
        session.rollback()
        raise
    finally:
        session.close()





