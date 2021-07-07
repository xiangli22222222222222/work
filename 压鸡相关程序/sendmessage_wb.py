import get_token2
import requests
import json
import get_zaoyan

def send_message2(token_2,content2,ad_id):
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


def send_message(zaoyan,press_time,dotime):

	#新应用需要配置
	appsecret="https://qyapi.weixin.qq.com/cgi-bin/gettoken?corpid=ww17c795da4df0c791&corpsecret=2zhTvCQivYovR3oPOZF6S-y62rodvC7OMDFF6bKneTY"
	ad_id=1000003

	#获取token
	token_2=get_token2.get_token(appsecret)
	print(token_2)

	#把灶眼信息拿回来
	zaoyan1, zaoyan2 = get_zaoyan.duiying(zaoyan)


	#拼接发送内容
	content2="第"+str(zaoyan1)+"排 "+"第"+str(zaoyan2)+"个灶眼"+"   压鸡时间:"+str(dotime)+"  时长："+str(press_time)+"分钟"

	send_message2(token_2,content2,ad_id)

def send_message_about2(sum0,zaoyan,time_jian):

	#新应用需要配置
	appsecret="https://qyapi.weixin.qq.com/cgi-bin/gettoken?corpid=ww17c795da4df0c791&corpsecret=2zhTvCQivYovR3oPOZF6S-y62rodvC7OMDFF6bKneTY"
	ad_id=1000003

	#获取token
	token_2=get_token2.get_token(appsecret)
	print(token_2)

	#把灶眼信息拿回来
	zaoyan1, zaoyan2 = get_zaoyan.duiying(zaoyan)

	if sum0>55:
		good_or="   恭喜上汽了!"
	else:
		good_or="   还没有上汽！"

	#拼接发送内容
	content2="第"+str(zaoyan1)+"排 "+"第"+str(zaoyan2)+"个灶眼"+"  已经压鸡："+str(time_jian)+good_or

	send_message2(token_2,content2,ad_id)


if __name__=='__main__':
	send_message()