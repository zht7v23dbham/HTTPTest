#-*- coding:utf-8 -*-

import smtplib
from Config import MailConf
from email.mime.text import MIMEText
from email.header import Header


if __name__ == '__main__':
        mSender = MailConf.sender
        senderName = MailConf.username
        senderPwd = MailConf.password
         # 邮件标题
        subject = u'python selenium email文本邮件发送测试'
        # 文本格式邮件 正文内容
        msg = MIMEText(u'测试邮件', 'text', 'utf-8')

        # 邮件标题
        msg['Subject'] = Header(subject, 'utf-8')

        # 初始化一个smtp对象
        smtp = smtplib.SMTP()
        # 连接至smtp服务器
        smtp.connect(MailConf.smtpserver)
        # 登录smtp服务
        smtp.login(senderName,senderPwd)
        #发送邮件
        smtp.sendmail(mSender, MailConf.receiverList, msg.as_string())
        # 发送完成后关闭连接
        smtp.quit()