"""
@Author:Misty rain(ZhangHao)
@E-mail:676817831@qq.com
@FileName:gettime.py
@Software:PyCharm
@Desc:时间日期处理类
"""
import time
import datetime


def get_system_time():
    """
    获取当前时间
    :return:
    """
    new_time = time.strftime('%Y-%m-%d %H:%M:%S', time.localtime())
    return str(new_time)


def get_system_time_date():
    """
    获取当前日期
    :return:
    """
    new_time = time.strftime('%Y-%m-%d', time.localtime())
    return str(new_time)


def get_system_time_division():
    """
    获取当前时间 具体到时分
    :return:
    """
    new_time = time.strftime('%Y-%m-%d %H:%M', time.localtime())
    return str(new_time)


def get_system_time_afterday(days):
    """
    获取当前时间的后n天
    :return:
    """
    now_time = datetime.datetime.now()
    new_time = (now_time + datetime.timedelta(days=+days)).strftime("%Y-%m-%d %M:%S")
    return str(new_time)


def get_logdata():
    """
    获取当前日期
    :return:
    """
    new_time = time.strftime('%Y%m%d%H%M%S', time.localtime())
    return str(new_time)


def get_system_time_afterhours(hours):
    """
    获取当前时间的后n小时
    :return:
    """
    now_time = datetime.datetime.now()
    new_time = (now_time + datetime.timedelta(hours=+hours)).strftime("%Y-%m-%d %H:%M")
    return str(new_time)


if __name__ == '__main__':
    print(get_system_time() + '\n' + get_system_time_date() + '\n' + get_system_time_afterday(
        2) + '\n' + get_system_time_afterhours(3))
