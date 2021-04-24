# coding:utf-8

import configparser
import os
# 简单邮件传输协议
import smtplib
import time
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.utils import formataddr
import base64
import urllib.request
import re
import time

import json
from pathlib import Path



class Text(object):


    # 加载配置文件
    def loading(self):
        f = open('AccountInfo.json', encoding='UTF-8')
        text = ""
        line = f.readline()  # 调用文件的 readline()方法
        while line:
            if not re.match(r'(\s*//)|(\n)', line):
                text = text + line
            line = f.readline()



        f.close()
        document = json.loads(text)


        self.flag = document['flag']
        self.from_email = document['from_email']
        self.to_email = document['to_email']
        self.key = document['key']
        self.websitelist = document['productList']
        self.biaoti = document['biaoti']
        self.msg = ""


    # 爬虫
    def getnews(self):
        news = []
        for website in self.websitelist:
            url = website["url"]

            # regex = str(base64.b64decode(website["reg"]))[3:-1].replace("\\\\","\\")
            # temp1 = regex.replace("\\\\","\\")
            # print(temp1)
            regex = str(base64.b64decode(website["reg"]))[3:-1].replace("\\\\","\\")
            head = website["header"]
            page = urllib.request.urlopen(url).read().decode('utf-8')
            p = re.compile(regex)
            items = p.findall(page)


            # 对于每一条匹配的结果，如果需要筛选在这个for里面自己写
            for item in items:
                # do something


                # 把每条结果添加进正文
                self.msg = self.msg + 'https://sast.xidian.edu.cn/'+ item[0] + '\t' + item[1]+ '\t' +item[2] + '\n'
                # self.msg += str(item)

        # print(self.msg)







    def send_email(self):

        today_time = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())

        # 设置邮箱的域名
        HOST = 'smtp.qq.com'
        # 设置邮件标题
        SUBJECT = '%s' % (self.biaoti)
        # 设置发件人邮箱
        FROM = self.from_email
        # 设置收件人邮箱
        TO = self.to_email  # 可以同时发送到多个邮箱
        message = MIMEMultipart('related')

        # 发送邮件正文到对方的邮箱中
        # with open("log.log", "r") as logfile:  # 打开文件
        #     data = logfile.read()  # 读取文件
        zhengwen = "爬取结果：\n%s" % self.msg
        # logfile.close()


        my_sender = self.from_email
        my_pass = self.key  # 发件人邮箱密码(当时申请smtp给的口令)
        my_user = self.to_email  # 可以同时发送到多个邮箱


        try:
            msg = MIMEText(zhengwen, 'plain', 'utf-8')
            msg['From'] = formataddr(["爬虫脚本", my_sender])
            # 括号里的对应发件人邮箱昵称、发件人邮箱账号
            msg['To'] = formataddr(["结果", my_user])
            # 括号里的对应收件人邮箱昵称、收件人邮箱账号
            msg['Subject'] = '%s ： %s ' % (self.biaoti, today_time)
            # 邮件的主题，也可以说是标题

            server = smtplib.SMTP_SSL("smtp.qq.com", 465)
            # 发件人邮箱中的SMTP服务器，端口是465
            server.login(my_sender, my_pass)
            # 括号中对应的是发件人邮箱账号、邮箱密码
            server.sendmail(my_sender, [my_user, ], msg.as_string())
            # 括号中对应的是发件人邮箱账号、收件人邮箱账号、发送邮件
            server.quit()  # 关闭连接
        except Exception:  # 如果 try 中的语句没有执行，则会执行下面的 ret=False
            print("邮件发送失败:%s" % Exception)

        print("邮件发送成功")



    def main(self):

        try:
            self.loading()

            self.getnews()



        except Exception as e:
            print(e)
            print("未知错误")
            self.msg = '！！！ 未知错误 ！！！' + str(e)

        finally:
            if self.flag == 1:
                self.send_email()
                print("已经执行发送邮件任务")


def main_handler(agrs1,agrs2):
    Text().main()


# Text().loading()
# Text().getnews()

# Text().main()