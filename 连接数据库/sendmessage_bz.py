import datetime

import get_token
import requests
import json
import get_zaoyan

def send_message2(token_2,zaoyan1,zaoyan2,get_time,m,n):
	url="https://qyapi.weixin.qq.com/cgi-bin/message/send?access_token="+token_2

	send_json={	"touser": "@all",
	"toparty": "@all",
	"totag": "@all",
	"msgtype": "text",
	"agentid": 1000004,
	"text": {
		"content":"第"+str(zaoyan1)+"排"+"第"+str(zaoyan2)+"个灶眼"+" 超过3的次数："+str(m)+str(n)+"   时间为："+str(get_time)
			},
	"safe": 0,
	"enable_id_trans": 0,
	"enable_duplicate_check": 0,
	"duplicate_check_interval": 1800
	}

	response=requests.request("POST",url,data=json.dumps(send_json))

	print (response.text)


def send_message(zaoyan,get_time,m,n):
	zaoyan1,zaoyan2=get_zaoyan.duiying(zaoyan)
	token_2=get_token.get_token()
	send_message2(token_2,zaoyan1,zaoyan2,get_time,m,n)

if __name__=='__main__':
    send_message()