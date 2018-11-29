# -*- coding:utf-8 -*-

from flask_script import Manager

from init import app
from webapp import register_blueprints

register_blueprints(app)
manager = Manager(app)

if __name__ == '__main__':
    manager.run()
