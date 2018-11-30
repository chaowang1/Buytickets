# -*- coding:utf-8 -*-

from flask import Blueprint, request

from init import app
from middles import ticket
from webapp import route
from util import generate_uuid

bp = Blueprint(app, __name__, url_prefix='/buy_ticket')


@route(bp, '/add_user', methods=['POST'])
def add_user():
    """
    添加用户
    :return:
    """
    user_uid = generate_uuid('user')
    print(111111111111111)
    kv = request.get_json(force=True)
    print(kv)
    kv['user_uid'] = user_uid
    ticket.add_user(**kv)
