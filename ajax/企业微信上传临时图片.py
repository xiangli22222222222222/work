# -*-coding:utf-8 -*-
__author__ = 'yangxin_ryan'

import requests, json
import urllib3

urllib3.disable_warnings()
"""
Python实现企业微信推送文件
备注：支持中文名字等
"""


class WechatFile(object):

    def get_token(self, corpid, secret):
        url = "https://qyapi.weixin.qq.com/cgi-bin/gettoken"
        data = {"corpid": "ww17c795da4df0c791",
                "corpsecret": "4h6Z4cGDV_efSsalIeZxYkJS_tvuMKNr855w7vfqWbQ"}
        r = requests.get(url=url, params=data, verify=False)
        token = r.json()['access_token']
        return token

    def get_file_url(self, token, path):
        url = "https://qyapi.weixin.qq.com/cgi-bin/media/upload?access_token=%s&type=image" % token
        data = {"media": open(path, 'rb')}
        r = requests.post(url=url, files=data)
        dict_data = r.json()
        return dict_data['media_id']

    def send_news_message(self, user, path):
        corpid = "ww17c795da4df0c791"
        secret = "4h6Z4cGDV_efSsalIeZxYkJS_tvuMKNr855w7vfqWbQ"
        agentid = "1000004"
        token = self.get_token(corpid, secret)
        file_meida = self.get_file_url(token, path)
        url = "https://qyapi.weixin.qq.com/cgi-bin/message/send?access_token=%s" % token
        data = {"touser": all,
                "agentid": 1000004,
                "msgtype": "file",
                "file": {"media_id": file_meida},
                "safe": "0"}
        headers = {'content-type': 'application/json'}
        data_dict = json.dumps(data, ensure_ascii=False).encode('utf-8')
        r = requests.post(url=url, headers=headers, data=data_dict)
        status = eval(r.text)
        print(status)
        return status


if __name__ == '__main__':
    user = "yangxin03"
    path = "./1.png"
    wechat_file = WechatFile()
    wechat_file.send_news_message(user, path)