# -*- coding: utf-8 -*-

# from configparser import ConfigParser
import os
import requests

from conf import readConfig


#读取配置信息
localRead = readConfig.ReadConfig()

class Config():
    #定义报告文件路径path
    path_dir = str(os.path.abspath(os.path.join(os.path.dirname(__file__), os.pardir)))
    print(path_dir)

    def __init__(self):
        #初始化获取config.ini值
        #global 全局变量
        global agreement, baseurl, environment, timeout, tester, version, port
        tester = localRead.get_online_release('tester')
        environment = localRead.get_online_release('environment')
        version = localRead.get_online_release('version')
        baseurl = localRead.get_online_release('host')
        port = localRead.get_online_release('port')
        timeout = localRead.get_online_release('timeout')
        agreement = localRead.get_online_release('agreement')

        #定义空的字典
        self.headers = {}
        self.params = {}
        self.data = {}
        self.url = None
        self.files = {}




        #定义报告路径
        self.xml_report_path = Config.path_dir + '\\report'
        self.html_report_path = Config.path_dir + '\\report\\html'


    #设置参数值
    def set_url(self, url):
        self.url = agreement + '://' + baseurl + url


    def set_headers(self, header):
        self.headers = header

    def set_params(self, param):
        self.params = param

    def set_data(self, data):
        self.data = data
        self.data = data.encode("utf-8")





    #上传图片所用
    # def set_files(self, filename):
    #     if self.filename != '':
    #         file_path = '/xx/testFile/img' + filename
    #         self.files = {'file':open(file_path, 'rb', encoding='utf-8')}
    #
    #     if filename == '' or filename is None:
    #         pass


    #定义get方法
    def getreq(self):
        try:
            response = requests.get(self.url, headers=eval(self.headers), params=self.params, timeout=float(timeout))
            return response
        except TimeoutError:
            return '出错了1'

    #定义post方法
    def postreq(self):
        try:

            response = requests.post(url=self.url, headers=eval(self.headers), data=self.data, timeout=float(timeout))
            return response
        except TimeoutError:
            return '出错了'

    # 定义post方法
    def putreq(self):
        try:

            response = requests.put(url=self.url, headers=eval(self.headers), data=self.data, timeout=float(timeout))
            return response
        except TimeoutError:
            return '出错了'


    #定义上传方式
    def postWithmultipart(self):
        try:
            response = requests.post(self.url, files=self.files, timeout=float(timeout))
            return response
        except TimeoutError:
            return '出错了1'

    #定义json格式方法
    def postJsonreq(self):
        try:
            response = requests.post(self.url, headers=self.headers, data=self.data, timeout=float(timeout))
            return response
        except TimeoutError:
            return '出错了1'

if __name__ == '__main__':
    # cc = Config()
    # print(cc.xml_report_path)
    pass