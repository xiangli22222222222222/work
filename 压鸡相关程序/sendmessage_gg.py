import json
import requests
import get_token2



def send_message(appsecret,content2,ad_id):

	# 获取token
	token_2 = get_token2.get_token(appsecret)

	print(token_2)

	url="https://qyapi.weixin.qq.com/cgi-bin/message/send?access_token="+token_2

	send_json={	"touser": "@all",
	"toparty": "@all",
	"totag": "@all",
	"msgtype": "text",
	"agentid": ad_id,
	"text": {
		"content":content2
			},
	"safe": 0,
	"enable_id_trans": 0,
	"enable_duplicate_check": 0,
	"duplicate_check_interval": 1800
    }

	response=requests.request("POST",url,data=json.dumps(send_json))

	print (response.text)


if __name__=='__main__':
	send_message()

