"""
@Author:Misty rain(ZhangHao)
@E-mail:676817831@qq.com
@FileName:getlog.py
@Software:PyCharm
@Desc:打印工程日志
"""
import threading
import logging
import commont.getfileposition as file
import colorlog
import commont.gettime as timer


# 定义全局变量
log_colors_config = {
    'DEBUG': 'white',
    'INFO': 'green',
    'WARNING': 'yellow',
    'ERROR': 'red',
    'CRITICAL': 'bold_red'
}

logger = logging.getLogger('PROJECT')
logger.setLevel(logging.DEBUG)

# 创建一个handler写入日志
fh = logging.FileHandler(
    filename=file.getrootpath()+'/log/{project}.log'.format(project=timer.get_system_time_date()), encoding='utf-8')
fh.setLevel(logging.DEBUG)

# 创建一个handler输出控制台
# ch = logging.StreamHandler()
# ch.setLevel(logging.DEBUG)
# 定义日志输入格式
formatter = logging.Formatter(
    fmt='[%(asctime)s.%(msecs)03d] %(filename)s -> %(funcName)s line:%(lineno)d [%(levelname)s] : %(message)s',
    datefmt='%Y-%m-%d  %H:%M:%S'
)
# 控制台输出有颜色的日志
# console_formatter = colorlog.ColoredFormatter(
#     fmt='%(log_color)s[%(asctime)s.%(msecs)03d] %(filename)s -> %(funcName)s line:%(lineno)d [%(levelname)s] '
#         ': %(message)s',
#     datefmt='%Y-%m-%d  %H:%M:%S',
#     log_colors=log_colors_config
# )

# 定义日志输入格式
# formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s','%Y/%m/%d %H:%M:%S')
fh.setFormatter(formatter)
# ch.setFormatter(console_formatter)

logger.addHandler(fh)
# logger.addHandler(ch)


if __name__ == '__main__':

    logger.error('error message')
    logger.debug('debug message')
    logger.info('info message')
    logger.warning('war message')
    logger.critical('cri message')