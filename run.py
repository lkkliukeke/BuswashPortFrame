#coding: utf-8
import warnings
import urllib3
import builtins

import pytest
import os

from common import Shell
from common import publicrequest

redcon = publicrequest.Config()


if __name__ == '__main__':
    shell = Shell.Shell()
    xml_report_path = redcon.xml_report_path
    html_report_path = redcon.html_report_path
    print(xml_report_path)
    print(html_report_path)


    # 清空之前的执行结果         -后续自己添加的功能
    #os.path.exists()就是判断括号里的文件是否存在的意思，括号内的可以是文件路径。
    if os.path.exists(xml_report_path):
        #os.listdir() 方法用于返回指定的文件夹包含的文件或文件夹的名字的列表
        for file_name in os.listdir(xml_report_path):
            if file_name != 'environment.properties':
                file_path = os.path.join(xml_report_path, file_name)
            #os.path.isfile()：判断某一对象(需提供绝对路径)是否为文件
            if os.path.isfile(file_path):
                os.remove(file_path)

    # 定义测试集
    arg = ['-s', '-q', '--alluredir', xml_report_path]
    pytest.main(arg)

    # 未生成html文件时 首次运行使用
    # cmd = ['allure', 'generate', xml_report_path, '-o', html_report_path]
    # 生成html文件后，加上--clean 清楚之前数据进行更新
    cmd = ['allure', 'generate', '--clean', xml_report_path, '-o', html_report_path]

    # 如果返回值遇到警告可去除warning
    urllib3.disable_warnings()
    warnings.simplefilter('ignore', ResourceWarning)

    try:
        shell.invoke(cmd)
    except Exception:
        raise


