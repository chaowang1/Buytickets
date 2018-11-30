# -*- coding:utf-8 -*-

from models import ticket as t

from init import session_scope


def add_user(**kwargs):
    with session_scope() as session:
        user = t.User(**kwargs)
        session.add(user)


def delete_user(user_uid):
    with session_scope() as session:
        session.query(t.User).filter_by(user_uid=user_uid).update({'status': 0})


def update_user(**kwargs):
    with session_scope() as session:
        uid = kwargs.pop('user_uid')
        session.query(t.User).filter_by(user_uid=uid).update(kwargs)


def get_user(**kwargs):
    with session_scope() as session:
        q = session.query(t.User).filter_by(**kwargs).filter_by(status=True)
        return [u.to_dict() for u in q]


def add_customer(**kwargs):
    with session_scope() as session:
        customer = t.Customer(**kwargs)
        session.add(customer)
        session.flush()
        return customer.customer_uid


def delete_customer(customer_uid):
    with session_scope() as session:
        session.query(t.Customer).filter_by(customer_uid=customer_uid).update({'status': False})


def update_customer_info(**kwargs):
    with session_scope() as session:
        uid = kwargs.pop('customer_uid')
        session.query(t.Customer).filter_by(customer_uid=uid).update(kwargs)


def get_customer_info(**kwargs):
    with session_scope() as session:
        q = session.query(t.Customer).filter_by(**kwargs).filter_by(status=True)
        return [c.to_dict() for c in q]




