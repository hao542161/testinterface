"""
@Author:Misty rain(ZhangHao)
@E-mail:676817831@qq.com
@FileName:configHttp.py
@Software:PyCharm
@Desc:http请求配置
"""
import requests
from commont import readconfig as rc
from commont.getlog import logger
import json


class HttpClient:
    """
    parameter:url,port,timout,headers
    请求地址、端口、超时时间、请求头
    这里封装最常见的几种公共，像file、cookie这些在方法中
    """

    def __init__(self):
        self.url = rc.get_interface('url')
        self.timeout = int(rc.get_interface('timeout'))
        self.headers = json.loads(rc.get_interface('headers'))

    """
    name：接口名
    data：参数
    """

    def send_post(self, name, data):
        response = requests.post(url=self.url + name, json=data, headers=self.headers, timeout=self.timeout)
        # 获取返回内容
        # 转码 utf-8、gbk、unicode-escape
        response.encoding = 'unicode-escape'
        text = response.text
        # 获取返回code值
        code = response.status_code
        try:
            # 将字符串转换为字典
            dict_text = json.loads(text)
            # 定义字典来保存数据
            result = {"text": dict_text, "code": code}
            # 打印日志
            logger.info(
                '{name} / post请求：\n请求值：{request}\n返回值：\n{text}状态码：{code}'.format(name=name, request=data, text=text,
                                                                                 code=code))
        except:
            logger.info(
                '{name} / post请求：\n请求值：{request}\n返回值：\n{text}状态码：{code}'.format(name=name, request=data, text=text,
                                                                                 code=code))
            raise Exception('请求错误')

        return result

    def send_get(self, name, data):
        response = requests.get(url=self.url + name, json=data, headers=self.headers, timeout=self.timeout)
        # 获取返回内容
        response.encoding = 'unicode-escape'
        text = response.text
        # 获取返回code值
        code = response.status_code
        # 将字符串转换为字典
        dict_text = json.loads(text)
        # 定义字典来保存数据
        result = {"text": dict_text, "code": code}
        # 打印日志
        logger.info('{name} / get请求：\n请求值：{request}\n返回值：\n{text}状态码：{code}'.format(name=name, request=data, text=text,
                                                                                    code=code))
        # dict_result = json.load(result)
        return result

    def send_http(self, method, name, data):
        method = method.lower()
        if method not in ('get', 'post'):
            raise Exception('Invalid request method [%s], should be "get" or "post"' % method)

        if method == 'post':
            result = self.send_post(name, data)
        else:
            result = self.send_get(name, data)

        return result


# 调试
if __name__ == '__main__':
    http = HttpClient()
    params = {'username': '天才儿子', 'password': '123456'}
    result = http.send_http('post', 'login', params)
    # hh = json.loads()
    print(result['text']['code'])
