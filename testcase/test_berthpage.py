# -*- coding: utf-8 -*-
# 泊位模块
import json

import allure
import pytest
from common import public
from common import Assert


localexcel = public.get_xls('PatrolExcel.xlsx', 'berth')

from common import publicrequest

setrq = publicrequest.Config()


class TestBerthPage:
    @pytest.mark.parametrize('excelist', localexcel)
    @allure.feature('test_berthpage')
    @allure.title('泊位模块')
    @allure.story('100%')
    def test_berth(self, excelist):
        #设置url
        setrq.set_url(excelist[4])
        # 请求头 header
        setrq.set_headers(excelist[5])
        #加入入参


        # 请求对应封装
        if excelist[3] == 'post':
            setrq.set_data(excelist[6])
            reqs = setrq.postreq()
        elif excelist[3] == 'get':
            setrq.set_params(excelist[6])
            reqs = setrq.getreq()
        else:
            setrq.set_data(excelist[6])
            reqs = setrq.putreq()


        #断言
        # assert getreq.status_code == 200
        Assert.Assertions.assert_code(self, reqs.status_code,200)

        #预取‘name’：‘123’包含再返回字符串中 #assert excellist[8] in getreq.text
        Assert.Assertions.assert_expect(self, excelist[9], reqs.text)

        # #断言两个值是否相等
        # excel_data= "{" + excelist[9] + "}"
        # Assert.Assertions.assert_body(self, json.loads(excel_data), 'ill_count', getreq.json()['data']['ill_count'])


