"""
@Author:Misty rain(ZhangHao)
@E-mail:676817831@qq.com
@FileName:run.py
@Software:PyCharm
@Desc:运行用例入口
"""
import os
from commont import getfileposition as gf
import pytest

if __name__ == '__main__':
    # 运行所有接口
    pytest.main()
    os.system('allure generate '+gf.getrootpath()+'/report/allure -o '+gf.getrootpath()+'/allure_report --clean')
    # 运行主要接口
    # pytest.main(['-m=main'])
    # 运行次要接口
    # pytest.main(['-m=secondary'])
