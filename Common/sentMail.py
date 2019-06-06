#!/usr/bin/python3
import os
import time
import smtplib
from email.mime.text import MIMEText
from email.utils import formataddr
from email.mime.multipart import MIMEMultipart

import getcwd
from Common.config import Config
from Common.log import log1


config = Config()

rq = time.strftime('%Y%m%d', time.localtime(time.time()))  # 获取本地时间 转换成日期
email = config.config_read('sender', 'email')  # 发件人邮箱账号
password = config.config_read('sender', 'password')  # 发件人邮箱密码
usernmae = config.config_read('sender', 'username')  # 发件人姓名
users = config.config_options('addressed')  # 收件人
addressed_eamils = config.get_addkey(users)  # 收件人邮箱

path = getcwd.get_cwd()
file = os.path.join(path, 'report/xxxUI自动化测试报告.html')


def sent_mail():
    try:
        # 创建一个带附件的实例
        message = MIMEMultipart()
        message['From'] = formataddr([usernmae, email])  # 括号里的对应发件人邮箱昵称、发件人邮箱账号
        log1.info('发件人姓名：%s' % usernmae)
        log1.info('发件人邮箱：%s' % email)
        message['To'] = ';'.join(addressed_eamils)  # 括号里的对应收件人邮箱昵称、收件人邮箱账号
        log1.info('收件人邮箱：' + ';'.join(addressed_eamils))
        message['Subject'] = rq + "xxxUI自动化测试报告.html"  # 邮件的主题，也可以说是标题

        # 邮件正文内容
        message.attach(MIMEText('附件为xxxUI自动化测试报告.html', 'plain', 'utf-8'))

        # 读取要发送的附件
        att1 = MIMEText(open(file, 'rb').read(), 'base64', 'utf-8')
        log1.info('读取附件')
        # 设置附件对应的content-type
        att1["Content-Type"] = 'application/octet-stream'
        # 这里的filename可以任意写，写什么名字，邮件中显示什么名字
        att1.add_header("Content-Disposition", "attachment", filename=("gbk", "", "xxxUI自动化测试报告.html"))
        # 附件名称非中文时的写法
        # att["Content-Disposition"] = 'attachment; filename="test.html")'
        message.attach(att1)
        log1.info('添加附件')

        server = smtplib.SMTP_SSL("smtp.qq.com", 465)  # 发件人邮箱中的SMTP服务器，端口是25
        log1.info('连接QQ邮箱smtp服务')
        server.login(email, password)  # 括号中对应的是发件人邮箱账号、邮箱密码
        log1.info('连接成功')
        server.sendmail(email, addressed_eamils, message.as_string())  # 括号中对应的是发件人邮箱账号、收件人邮箱账号、发送邮件
        server.quit()  # 关闭连接
        log1.info("邮件发送成功")
    except Exception:
        log1.error("邮件发送失败", exc_info=1)
