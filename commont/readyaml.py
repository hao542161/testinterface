"""
@Author:Misty rain(ZhangHao)
@E-mail:676817831@qq.com
@FileName:readyaml.py
@Software:PyCharm
@Desc:读取yaml文件，用于获取接口名称、参数等信息
"""
import os
import yaml
from commont import getfileposition as gf

PATH = lambda p: os.path.abspath(os.path.join(
    os.path.dirname(__file__), p
))


def get_api():
    info = YamlData(gf.getrootpath()+'\\yaml\\api.yml').data()
    return info


class YamlData:
    def __init__(self, file):
        if os.path.isfile(PATH(file)):
            self.file = PATH(file)
        else:
            raise FileNotFoundError("文件不存在")

    def data(self):
        with open(file=self.file, mode="rb") as f:
            infos = yaml.load(f, Loader=yaml.FullLoader)
        return infos