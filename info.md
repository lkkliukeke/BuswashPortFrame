接口自动化框架说明文档
#目录说明
    common 公共方法
        Assert 封装assert方法
        public 读取excel用例公共方法封装
        publicLogin 登录公共封装
        publicrequest  封装请求、配置信息
        Log  封装记录Log方法，分为：debug、info、warning、error、critical
             日志方法封装输出（err.log & log.log日志）
        cookie & session 公共方法封装
        shell 封装subprocess方法CASE执行结束进程操作（优化性能）

    conf 配置文件公共方法封装
        config.ini 域名/端口/超时环境配置
        readconfig 读取ini配置信息封装方法
    Log 日志输出
    
    Report  1.pytestcase执行报告生成
            2.environment.properties配置报告显示环境

    Testcase XX版本CASE实现
        1，单项目/多项目case实现
        2，jsonpath使用快捷获取节点值

    TestFile
        excel case 单接口 & 多接口组装
        img 请求图片/文件存放地址

    pytest.ini
        参考官方处理错误方法：https://docs.pytest.org/en/stable/warning.html
        处理pytest执行结果告警信息-过滤

    run
        执行所有case方法