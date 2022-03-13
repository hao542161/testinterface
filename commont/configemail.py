"""
@Author:Misty rain(ZhangHao)
@E-mail:676817831@qq.com
@FileName:configemail.py
@Software:PyCharm
@Desc:邮件配置
"""
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.header import Header
from email.utils import formatdate

from commont import readconfig as rc
from commont import getfileposition as gf
from commont.getlog import logger
# 读取config邮箱配置
host = rc.get_email('host')
port = rc.get_email('port')
Sender = rc.get_email('Sender')
password = rc.get_email('password')
Receiver = rc.get_email('Receiver')


class SendEMail:
    """
    初始化，连接邮箱服务器并登录
    """

    def __init__(self):
        self.smtps = smtplib.SMTP_SSL(host=host, port=port)
        self.smtps.login(user=Sender, password=password)

    """
    发送普通邮件
    """

    def sendemail_text(self):
        # 构建邮件内容
        main_msg = MIMEMultipart()
        text_msg = MIMEText("xx自动化测试报告！")
        main_msg.attach(text_msg)
        main_msg['From'] = Sender
        main_msg['To'] = Receiver
        main_msg['Subject'] = Header("接口自动化测试报告", "utf-8")
        main_msg['Date'] = formatdate()
        fullText = main_msg.as_string()
        # 用smtp发送邮件
        self.smtps.sendmail(Sender, Receiver.split(','), fullText)

    """
    发送附件邮件
    """

    def sendemail_file(self):
        # 构建邮件内容
        main_msg = MIMEMultipart()
        text_msg = MIMEText("自动化测试报告！")
        main_msg.attach(text_msg)
        # 构建附件
        file_msg = MIMEText(open(gf.getrootpath() + '\\report\\' + 'test.html', 'rb').read(), 'base64', 'utf-8')
        file_msg["Content-Type"] = 'application/octet-stream'
        file_msg["Content-Disposition"] = 'attachment; filename="report_test.html"'
        main_msg.attach(file_msg)
        main_msg['From'] = Sender
        main_msg['To'] = Receiver
        main_msg['Subject'] = Header("接口自动化测试报告", "utf-8")
        main_msg['Date'] = formatdate()
        fullText = main_msg.as_string()
        # 用smtp发送邮件
        self.smtps.sendmail(Sender, Receiver.split(','), fullText)
        logger.critical('发送邮件成功！收件人分别为：{Receiver}'.format(Receiver=Receiver))


if __name__ == '__main__':
    sendemail = SendEMail()
    sendemail.sendemail_file()
