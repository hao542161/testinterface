"""
@Author:Misty rain(ZhangHao)
@E-mail:676817831@qq.com
@FileName:readconfig.py
@Software:PyCharm
@Desc:读取config文件内容，注意：config里面不能有中文，如果有中文打开cf.read下面一行的注释
"""
from commont import getfileposition as gf
import configparser


cf = configparser.ConfigParser()
cf.read(gf.getrootpath() + '/config/config.ini')
# cf.read(gf.getrootpath() + '/config/config.ini', encoding="utf-8-sig")


# 获取数据库配置文件内容
def get_db(name):
    value = cf.get('Mysql-Database', name)
    return value


# 获取邮箱配置文件内容
def get_email(name):
    value = cf.get('E-mail-address', name)
    return value


# 获取接口配置文件内容
def get_interface(name):
    value = cf.get('Interface-Address', name)
    return value


if __name__ == '__main__':
    print(get_interface('anbo'))