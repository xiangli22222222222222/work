import datetime
import requests
import json
import os
import get_token


def send_message(token_2,datetime_1,photo_time):

    #转换时间格式
    photo_time=datetime.datetime.strftime(photo_time,'%H:%M:%S')

    #发送请求
    url="https://qyapi.weixin.qq.com/cgi-bin/message/send?access_token="+token_2
    datetime_1=datetime_1+datetime.timedelta(hours=8)
    datetime_1=datetime.datetime.strftime(datetime_1,'%H:%M:%S')
    send_json={	"touser": "@all",
	"toparty": "@all",
	"totag": "@all",
	"msgtype": "text",
	"agentid": 1000004,
	"text": {
		"content":" 到点时间: "+str(datetime_1)+" 拍照时间: "+str(photo_time)
	        },
	"safe": 0,
	"enable_id_trans": 0,
	"enable_duplicate_check": 0,
	"duplicate_check_interval": 1800
    }
    response=requests.request("POST",url,data=json.dumps(send_json))

#往服务器上传素材
def upload_photo(image_path,token_2):

    url = "https://qyapi.weixin.qq.com/cgi-bin/media/upload?access_token="+token_2+"&type=image"

    payload={}
    files=[
      ('media',(image_path,open(image_path,'rb'),'image'))
    ]
    headers = {}

    response = requests.request("POST", url, headers=headers, data=payload, files=files)

    print(response.text)

    response_2=json.loads(response.text)

    media_id1=response_2.get('media_id')

    return(media_id1)

#企业微信发送文本消息


#企业微信发送视频
def send_photo(token_2,media_id1):
    url="https://qyapi.weixin.qq.com/cgi-bin/message/send?access_token="+token_2
    send_json={"touser" : "@all",
      "toparty" : "@all",
      "totag" : "@all",
      "msgtype" : "image",
      "agentid" : 1000004,
      "image" : {
            "media_id" : media_id1,
            "title" : "Title",
            "description" : "到点时间:"
       },
      "safe": 0,
      "enable_duplicate_check": 0,
      "duplicate_check_interval": 1800
      }

    response=requests.request("POST",url,data=json.dumps(send_json))

    print (response.text)
def send_pic(FILE_PATH,datetime_1,photo_time):
        #获取token
        token_2=get_token.get_token()

        #上传图片，并获取media_id
        media_id1=upload_photo(FILE_PATH,token_2)
        print(media_id1)

        #发送企业微信文本，通知拍照时间和压鸡时间
        send_message(token_2,datetime_1,photo_time)

        #把图片发送到企业微信
        send_photo(token_2,media_id1)
        os.remove(FILE_PATH)

if __name__=='__main__':
    send_pic()