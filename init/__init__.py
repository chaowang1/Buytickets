import os
from flask_docs import ApiDoc
from contextlib import contextmanager

from flask import Flask
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from config import webconfig as config

app = Flask(__name__,
            static_folder=os.path.abspath(os.path.join(config.webroot, 'static')),
            static_url_path="",
            template_folder=os.path.abspath(os.path.join(config.webroot, 'templates'))
            )

app.config.from_object(config)

app.secret_key = '9pf0glVwIwsvGsgmheQRRBoumt1TbSq6fmfhjztL'

app.config['API_DOC_MEMBER'] = ['ticket']
app.config['RESTFUL_API_DOC_EXCLUDE'] = []
ApiDoc(app)

engine = create_engine(app.config['DB_URI'],
                       encoding='utf-8',
                       convert_unicode=True,
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
