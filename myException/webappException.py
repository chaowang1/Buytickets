# -*- coding:utf-8 -*-


class ServiceError(Exception):

    def __init__(self, code, message):
        self.code = code
        self.message = message

    def __str__(self):
        return '<%d %s>' % (self.code, self.message)


ErrArgs = ServiceError(1000, '参数错误')
ErrTokenFail = ServiceError(1001, '登录令牌失效')
ErrUserUnregistered = ServiceError(1002, '用户未注册')


