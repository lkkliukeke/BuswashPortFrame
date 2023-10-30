# -*- coding: utf-8 -*-

import requests
import os
from xlrd import open_workbook
import json

#获取json返回的某个值    暂时没什么用
# def get_value_from_return_json(json, name1, name2):
#     info = json['info']
#     group = info[name1]
#     #匹配正则表达式整体结果
#     value = group[name2]
#     return value



#打印报告返回值  ---unittest生成报告展示返回值
def show_return_msg(response):
    #返回response返回信息
    url = response.url
    #返回json返回值
    msg = response.text
    print('\n请求地址：' + url)
    #可以显示中文   展示为json格式
    print('\n请求返回值：' + '\n' + json.dumps(json.dumps(msg), ensure_ascii=False, sort_keys=True, indent=4))


#从excel文件中读取测试用例
def get_xls(xls_name, sheet_name):
    #获取当前文件上层目录
    proDir = os.path.abspath(os.path.dirname(os.path.dirname(__file__)))

    cls = []
    #获取xls文件的路径（把目录和文件合成一个路径）
    xlsPath = os.path.join(proDir, 'testFile', 'case', xls_name)
    #打开文件
    file = open_workbook(xlsPath)
    #按照名称获取工作列表
    sheet = file.sheet_by_name(sheet_name)

    # 读取列表有多少行便于循环
    nrows = sheet.nrows

    # 循环行的值
    for i in range(nrows):
        # 判断如果第0行不等于下面的内容，则都追加到列表中
        if sheet.row_values(i)[0] != u'测试用例编号':
            # 追加到cls列表中
            cls.append(sheet.row_values(i))
    return cls
    # print(cls)


if __name__ == '__main__':
    # get_xls('illandaccExcel.xlsx', 'illaccget')
    pass