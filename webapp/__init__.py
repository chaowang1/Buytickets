# -*- coding:utf-8 -*-
import traceback
import pkgutil
import importlib
from functools import wraps
from flask import request, Response, Blueprint
from voluptuous import MultipleInvalid
from werkzeug import exceptions as wkerr

from util import jsonify
from config.logger import log as LOGGER
from myException import webappException as Err


def route(app, *args, **kwargs):
    def decorator(func):
        @app.route(*args, **kwargs)
        @wraps(func)
        def wrapper(*args, **kwargs):
            try:
                rv = func(*args, **kwargs)
            except (wkerr.BadRequest, MultipleInvalid) as e:
                LOGGER(str(e))
                return jsonify(request.path, has_error=True, data=Err.ErrArgs)
            except Err.ServiceError as e:
                if e.code == 1001:
                    return Response('relogin', status=599)
                return jsonify(request.path, has_error=True, data=e)
            except Exception as e:
                print(e)
                LOGGER(traceback.format_exc())
                return jsonify(request.path, has_error=True, data=Err.ErrInternal)

            return jsonify(request.path, data=rv)

        return func
    return decorator


def register_blueprints(app):
    for _, name, _ in pkgutil.iter_modules(__path__):
        m = importlib.import_module("%s.%s" % (__name__, name))
        for item in dir(m):
            item = getattr(m, item)
            if isinstance(item, Blueprint):
                app.register_blueprint(item)
    return app





