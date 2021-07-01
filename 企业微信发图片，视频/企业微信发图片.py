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
           "description" : "Description"
       },
      "safe": 0,
      "enable_duplicate_check": 0,
      "duplicate_check_interval": 1800
      }

    response=requests.request("POST",url,data=json.dumps(send_json))

    print (response.text)

if __name__=='__main__':
    image_1=os.listdir('E:/work/123')
    for image_path in image_1:
        image_path='E:/work/123/'+image_path
        token_2=get_token()
        media_id1=upload_photo(image_path,token_2)
        send_photo(token_2,media_id1)
        os.remove(image_path)