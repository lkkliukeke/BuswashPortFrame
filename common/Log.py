# -*- coding: utf-8 -*-

import logging

import Logs
from common import publicrequest

#主要获取路径
pathroute = publicrequest.Config()
print(pathroute)


import time
import os

#获取当前时间 这个函数你看看是干啥的time.strftimePython time strftime() 函数用于格式化时间，返回以可读字符串表示的当地时间，格式由参数 format 决定
#这个就是一个获取时间的
def get_current_time():
    return time.strftime(myLog.data, time.localtime(time.time()))
    # a = time.strftime(myLog.data, time.localtime(time.time()))
    # print(a)

#定义类
class myLog():
    data = '%Y-%m-%d %H:%M:%S'

    def __init__(self):
        #定义日志获取路径
        resultPath = os.path.join(pathroute.path_dir, 'Logs')
        # resultPath = os.path.abspath('D:\PycharmProjects\BuswashPortFrame\Logs')
        print(resultPath)
        #D:\PycharmProjects\BuswashPortFrame\Logs

        #os.path.exists()方法可以直接获取判断文件/文件夹是否存在
        if not os.path.exists(resultPath):
            os.mkdir(resultPath)
        else:
            pass

        #使用接口debug、info、warn、error、critical之前必须创建Logger实例
        self.logger = logging.getLogger()
        # 设置日志使用的方式  为：info
        self.logger.setLevel(logging.INFO)

        # 创建一个handler写入日志文件，且写入日志文件生成的路径，设置日志文件名   utf-8设置日志格式
        handler = logging.FileHandler(os.path.join(resultPath, 'buswash.log'), encoding='utf-8')

        # 定义handler输出格式formatter格式化器，指明了最终输出中日志记录布局
        formatter = logging.Formatter('%(asctime)s- %(name)s - %(levelname)s - %(message)s')
        # 使用formatter对象设置日志信息最后的规划、结构和内容，默认的时间格式为：%Y/%m/%d %H:%M:%S %p
        handler.setFormatter(formatter)

        # logger添加到handler里面， 为logger实例增加一个处理器
        self.logger.addHandler(handler)




    #写入日志文件信息
    def get_logger(self, log_msg):
        #获取记录
        self.logger.info('日志[info]' + get_current_time()+ ' ' + log_msg)

    #写入起始行
    def build_start_line(self, case_no):
        self.logger.info('---------' + case_no + 'ATART-----------')

    # 写入结束行
    def build_end_line(self, case_no):
        self.logger.info('---------' + case_no + 'END-----------')



    # def get_logger1(self):
    #     # 获取记录
    #     self.logger.info('日志[info]1' + get_current_time())
    #     # print('1111')

if __name__ == '__main__':
    None
    # myLog1 = myLog()
    # myLog1.get_logger1()