"""
@Author:Misty rain(ZhangHao)
@E-mail:676817831@qq.com
@FileName:conftest.py
@Software:PyCharm
@Desc:程序总调用函数，session级别的函数，所有用例中都可以调用
注意：仅在该目录或下层目录生效：testcases
"""
import pytest


@pytest.fixture(scope='session')
def login():
    cookie = 'IGUQWEHDQWHEO112'
    print('获取到{cookie}'.format(cookie=cookie))
    return cookie


# 处理使用 @pytest.mark.parametrize，ids为中文乱码问题
def pytest_collection_modifyitems(items):
    """
    测试用例收集完成时，将收集到的item的name和nodeid的中文显示在控制台上
    :return:
    """
    for item in items:
        item.name = item.name.encode("utf-8").decode("unicode_escape")
        item._nodeid = item.nodeid.encode("utf-8").decode("unicode_escape")

