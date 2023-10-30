# -*- coding: utf-8 -*-

import os
#codecs模块-编码格式的处理

import codecs
import configparser

#获取配置文件路径
proDir = os.path.split(os.path.realpath(__file__))[0] + '/config.ini'

class ReadConfig:
    def __init__(self):
        self.cfg = configparser.ConfigParser()
        self.cfg.read(proDir)

    #获取对应config.ini配置信息
    def get_online_release(self,name):
        value = self.cfg.get('buswash_dev',name)
        return value

if __name__ == '__main__':
    #验证
    # cc = ReadConfig()
    # aa = cc.get_online_release('tester')
    # print(aa)
    None