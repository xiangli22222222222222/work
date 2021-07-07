import smtplib
import time
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
import os
import datetime


def send_email(file_name):
    while 1:
        exitor=os.path.exists(file_name)
        if exitor:

            txt_size1=os.path.getsize(file_name)
            if txt_size1>5000:
                #设置服务器所需信息
                #163邮箱服务器地址
                mail_host = 'smtp.qq.com'
                #163用户名
                mail_user = 'buaalx'
                #密码(部分邮箱为授权码)
                mail_pass = 'txovsqhcbtpabjfe'
                #邮件发送方邮箱地址
                sender = 'buaalx@qq.com'
                #邮件接受方邮箱地址，注意需要[]包裹，这意味着你可以写多个邮件地址群发
                receivers = ['997625@qq.com']

                #设置email信息
                #邮件内容设置
                message = MIMEMultipart()
                #邮件主题
                now_time=datetime.datetime.now().strftime('%H:%M:%S')
                print(now_time)
                message['Subject'] = '收到新的日志信息,时间为：    '+str(now_time)
                #发送方信息
                message['From'] = sender
                #接受方信息
                message['To'] = receivers[0]

                with open(file_name, 'r')as h:
                    content2 = h.read()
                # 设置txt参数
                part2 = MIMEText(content2,'plain','utf-8')
                # 附件设置内容类型，方便起见，设置为二进制流
                part2['Content-Type'] = 'application/octet-stream'
                # 设置附件头，添加文件名
                part2['Content-Disposition'] = 'attachment;filename="rizhi.txt"'

                message.attach(part2)
                #登录并发送邮件
                try:
                    smtpObj = smtplib.SMTP()
                    #连接到服务器
                    smtpObj.connect(mail_host,25)
                    #登录到服务器
                    smtpObj.login(mail_user,mail_pass)
                    #发送
                    smtpObj.sendmail(
                        sender,receivers,message.as_string())
                    #退出
                    smtpObj.quit()
                    print('success')
                except smtplib.SMTPException as e:
                    print('error',e) #打印错误
                os.remove(file_name)
        else:
            print("文件不存在！")
        time.sleep(10)
        print("等待10秒")

if __name__=='__main__':
    file_name='12194548.txt'
    send_email(file_name)