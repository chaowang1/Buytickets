# -*- coding:utf-8 -*-
import time
import uuid

from flask import jsonify as flask_jsonify

from config.webconfig import __version__
from myException import webappException as Err


def generate_uuid(prefix=''):
    if not prefix:
        return str(uuid.uuid1())[:-13]
    return '-'.join([prefix, uuid.uuid1().hex[:-13]])


def jsonify(interface, has_error=False, data=None):
    out = {
        '_head': {
            '_version': __version__,
            '_msgType': 'response',
            '_interface': interface,
            '_remark': '',
            '_timestamps': int(time.time())
        },
        '_data': {
            '_errCode': None,
            '_errStr': None,
            '_ret': None
        }
    }

    if has_error:
        out['_data']['_errCode'] = data.code
        out['_data']['_errStr'] = data.message
        out['_data']['_ret'] = -1
    else:
        out['_data']['_errCode'] = 0
        out['_data']['_errStr'] = 'ok'
        out['_data']['_ret'] = 0
        if data is not None:
            out['_data']['retData'] = data
    return flask_jsonify(out)


def validate_args(in_data):

    if in_data is None:
        return dict()

    if not isinstance(in_data, dict):
        raise Err.ErrArgs

    if in_data.get('_head') is None:
        raise Err.ErrArgs

    if in_data['_head'].get('_version') is None:
        raise Err.ErrArgs

    if __version__ != in_data['_head']['_version']:
        raise Err.ErrArgs

    if in_data.get('_param') is None or \
            not isinstance(in_data['_param'], dict):
        raise Err.ErrArgs

    return in_data['_param']


if __name__ == '__main__':
    print(generate_uuid('server'))
