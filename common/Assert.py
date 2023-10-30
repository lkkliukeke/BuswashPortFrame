# -*- coding: utf-8 -*-

#封装断言Assert公共方法

import json
from common import Log

logg = Log.myLog()

#封装了一个断言方法
class Assertions:
    #状态码code
    def assert_code(self, code, expected_code):
        try:
            assert int(code) == int(expected_code)
            return True
        except:
            logg.get_logger('返回状态码有误 %s, %d' % (expected_code, code))
            #raise 引发异常使用，加上它之后后面的语句不会被执行
            raise

    #返回值是否包含值
    def assert_expect(self, expect_msg, actual_msg):
        try:
            assert expect_msg in actual_msg
            return True
        except:
            # logg.get_logger('返回内容错误 %S' % (expect_msg))
            logg.get_logger('返回内容错误：' + expect_msg)
            raise


    #返回值效验    返回值json值某一个值断言
    def assert_body(self, body, body_msg, expected_msg):
        try:
            msg = body[body_msg]
            assert msg == expected_msg
            return True
        except:
            logg.get_logger('返回的值不等于预期的值, %s, %d' % (expected_msg, body_msg))
            #显示引发异常
            raise