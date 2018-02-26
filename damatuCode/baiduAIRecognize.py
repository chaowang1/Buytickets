# -*- coding:utf-8 -*-
from aip import AipImageClassify
from config.ticketConf import _get_yaml
from config.configCommon import getWorkDir
import os


class BaiduAISDK(object):

    def __init__(self, APP_ID, API_KEY, SECRET_KEY, options):
        self.APP_ID = APP_ID
        self.API_KEY = API_KEY
        self.SECRET_KEY = SECRET_KEY
        self.options = options

    def run(self):
        self.client = self.api_client()
        project_path = getWorkDir()
        filepath = os.path.join(project_path, 'tkcode')
        image = self.get_file_content(filepath)
        try:
            result = self.client.objectDetect(image, self.options)
            return result
        except:
            print "验证码验证失败"

    def api_client(self):
        print self.APP_ID,self.API_KEY,self.SECRET_KEY
        sdk_client = AipImageClassify(self.APP_ID, self.API_KEY, self.SECRET_KEY)
        return sdk_client

    def get_file_content(self, file_path):
        with open(file_path, 'rb') as fp:
            return fp.read()


if __name__ == "__main__":
    kwarg = _get_yaml()["baiduAIconf"]
    print kwarg
    AIOp = BaiduAISDK(APP_ID = kwarg["APP_ID"], SECRET_KEY = kwarg["SECRET_KEY"],
                   API_KEY=kwarg["SECRET_KEY"], options=kwarg["options"])
    print AIOp.run()


