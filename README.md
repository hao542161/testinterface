# 安装依赖包
    pip install -r requirements.txt
# 项目描述：
   该项目主要作用于项目接口自动化的测试，通过该框架可以轻松实现自动验证项目接口错误和流程错误。
   本项目主要有俩个实现方向：
   1、python+pytest+yaml+allure 通过yaml来管理接口测试数据
   2、python+pytest+execl+allure 通过execl来管理接口测试数据
   项目开发完成后使用Jenkins来完成最终的集成，从而实现自动化。

# 项目框架：
    commont：项目公共类文件夹
        getlog.py：日志类
        connectmysql：连接数据库类
        getfileposition：获取文件位置类
        gettime：获取时间日期类
        configemail：邮箱配置
        confighttp：http请求配置
        readconfig: 读取config.ini文件
        readyaml: 读取yaml文件
    file：execl文件保存位置
    config：配置文件夹
        config.ini：项目的所有全局配置路径，包括mysql、接口地址、邮箱地址等
    log：日志保存文件夹，按天保存日志
    report：保存生成的报告
        report.html pytest自带的报告
        report.xml xml报告
    testcase：用例文件，使用pytest框架
        conftest.py 程序总调用函数
        test_ 具体的用例
    yaml：接口请求信息管理
# 运行方式：
   通过run方法来运行整个工程，也可以通过调整要执行的模块运行固定模块的接口。

# 报告：
   在线生成HTML报告。可以在report中查看运行报告。