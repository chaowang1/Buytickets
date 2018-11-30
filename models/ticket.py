# -*- coding:utf-8 -*-
from datetime import datetime

from sqlalchemy import Column, Integer, String, Boolean, DateTime
from sqlalchemy.ext.declarative import declarative_base

from init import engine

Base = declarative_base(engine)


class User(Base):
    """
    用户管理表
    """
    __tablename__ = 'user'

    id = Column(Integer, primary_key=True)
    user_uid = Column(String(64), nullable=False)
    user_name = Column(String(128), nullable=False)
    password = Column(String(256), nullable=False)
    email = Column(String(64), nullable=False, default="")
    telephone = Column(String(64), nullable=False)
    status = Column(Boolean, nullable=False, default=True)
    create_time = Column(DateTime, nullable=False, default=datetime.now)
    update_time = Column(DateTime, nullable=False, default=datetime.now)

    def to_dict(self):
        return {
            'id': self.id,
            'user_uid': self.user_uid,
            'user_name': self.user_name,
            'password': self.password,
            'email': self.email
        }


class Customer(Base):
    """
    购票者信息
    """
    __tablename__ = 'customer'

    id = Column(Integer, primary_key=True)
    customer_uid = Column(String(64), nullable=False)
    name = Column(String(256), nullable=False)
    card_id = Column(String(64), nullable=False, doc="身份证号码")
    status = Column(Boolean, nullable=False, default=True)
    create_time = Column(DateTime, nullable=False, default=datetime.now)
    update_time = Column(DateTime, nullable=False, default=datetime.now)

    def to_dict(self):
        return {
            'id': self.id,
            'customer_uid': self.customer_uid,
            'name': self.name,
            'card_id': self.card_id
        }


Base.metadata.create_all(engine)
