"""
@Author:Misty rain(ZhangHao)
@E-mail:676817831@qq.com
@FileName:get.py
@Software:PyCharm
@Desc:获取文件位置
"""
import configparser
import os


# 获取当前目录
def getcurrent():
    path = os.path.abspath(os.path.dirname(__file__))
    return path


# 获取项目根目录
def getrootpath():
    path = os.path.dirname(os.path.dirname(__file__))
    return path


# 获取文件目录
def getfilepath():
    path = os.path.dirname(os.path.dirname(__file__)) + '/file'
    return path


# 调试
if __name__ == '__main__':
    print(getcurrent())
    print(getrootpath())
