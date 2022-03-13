"""
@Author:Misty rain(ZhangHao)
@E-mail:676817831@qq.com
@FileName:test_login.py
@Software:PyCharm
@Desc:登录用例
"""

# 集成allure
import os

import allure

import pytest
from commont.getlog import logger
from commont.configHttp import HttpClient
from commont import readyaml

http = HttpClient()

# 读取data
data = readyaml.get_api()['login']


# 公共函数-传参
@pytest.fixture(params=[data['params']])
def login_params(request):
    return request.param


class TestLogin:

    def setup_class(self):
        logger.info('=================【登录】用例执行-开始===========')

    def teardown_class(self):
        logger.info('=================【登录】用例执行-结束===========')

    @allure.feature('成功登录')
    @allure.story('正确的用户名密码进行登录')
    def test_success_login(self, login_params):
        """
        登录成功
        :return:0
        """
        # 请求
        result = http.send_http(data['method'], data['url'], login_params)
        # 校验
        assert result['text']['code'] == '0' and result['code'] == 200

    @allure.feature('异常登录')
    @allure.story('错误的密码、用户进行登录')
    @pytest.mark.parametrize('params', [(data['failpwd_params']), (data['failname_params'])], ids=['错误的密码', '错误的用户'])
    def test_fail_login(self, params):
        """
        1、错误的密码
        2、错误的用户
        :return:1
        """
        result = http.send_http(data['method'], data['url'], params)
        # 校验
        assert result['text']['code'] == '1' and result['code'] == 200, '返回状态码错误！'


if __name__ == '__main__':
    pytest.main(['test_login.py'])
    os.system('allure generate ../report/allure -o ../allure_report --clean')
