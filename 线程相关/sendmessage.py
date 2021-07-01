import time

import requests
import json
import os

def get_token():
#从获取token
    url="https://qyapi.weixin.qq.com/cgi-bin/gettoken?corpid=ww17c795da4df0c791&corpsecret=4h6Z4cGDV_efSsalIeZxYkJS_tvuMKNr855w7vfqWbQ"

    response=requests.request("GET",url)

    token_1=response.text
    token_1=json.loads(token_1)
    token_2=token_1.get('access_token')

    return (token_2)

def send_message(token_2,zaoyan5,zaoyan6):
    url="https://qyapi.weixin.qq.com/cgi-bin/message/send?access_token="+token_2

    send_json={	"touser": "@all",
	"toparty": "@all",
	"totag": "@all",
	"msgtype": "text",
	"agentid": 1000004,
	"text": {
		"content":"第"+str(zaoyan5)+"排"+"第"+str(zaoyan6)+"个灶眼"
	        },
	"safe": 0,
	"enable_id_trans": 0,
	"enable_duplicate_check": 0,
	"duplicate_check_interval": 1800
    }

    response=requests.request("POST",url,data=json.dumps(send_json))

    print (response.text)
def duiying(zaoyan):
        zaoyan1=0
        zaoyan2=0
        if zaoyan==0:
            zaoyan1=1
            zaoyan2=1
        elif zaoyan==1:
            zaoyan1 = 2
            zaoyan2 = 1
        elif zaoyan==2:
            zaoyan1=1
            zaoyan2=2
        elif zaoyan==3:
            zaoyan1=2
            zaoyan2=2
        elif zaoyan==4:
            zaoyan1=1
            zaoyan2=3
        elif zaoyan==5:
            zaoyan1=3
            zaoyan2=3
        return (zaoyan1,zaoyan2)

def dothis(zaoyan):
        zaoyan3,zaoyan4=duiying(zaoyan)
        token_2=get_token()
        send_message(token_2,zaoyan3,zaoyan4)

if __name__=='__main__':
    dothis()