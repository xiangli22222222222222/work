import datetime
import os
import requests
import json
import get_zaoyan
import get_token


#往服务器上传素材
def upload_photo(image_path,token_2):

    url = "https://qyapi.weixin.qq.com/cgi-bin/media/upload?access_token="+token_2+"&type=video"

    payload={}
    files=[
      ('media',(image_path,open(image_path,'rb'),'video'))
    ]
    headers = {}

    response = requests.request("POST", url, headers=headers, data=payload, files=files)

    print(response.text)

    response_2=json.loads(response.text)

    media_id1=response_2.get('media_id')

    print(media_id1)
    return(media_id1)

#企业微信发送视频
def send_photo(token_2,media_id1,zaoyan1,zaoyan2,datetime1,get_photo_time):

    #转换需要展示的时间格式
    datetime1=datetime.datetime.strftime(datetime1,'%H:%M:%S')
    get_photo_time=datetime.datetime.strftime(get_photo_time,'%H:%M:%S')

    #访问路径和json数据
    url="https://qyapi.weixin.qq.com/cgi-bin/message/send?access_token="+token_2

    send_json={"touser" : "@all",
      "toparty" : "@all",
      "totag" : "@all",
      "msgtype" : "video",
      "agentid" : 1000004,
      "video" : {
            "media_id" : media_id1,
            "title" : "第"+str(zaoyan1)+"排"+"第"+str(zaoyan2)+"个灶眼",
           "description" : "压鸡时间为:"+str(datetime1)+"录制时间为:"+str(get_photo_time)
       },
      "safe": 0,
      "enable_duplicate_check": 0,
      "duplicate_check_interval": 1800
      }

    response=requests.request("POST",url,data=json.dumps(send_json))

    print (response.text)

def take_video(zaoyan,datetime1,get_phototime,image_path):

    #获取token
    token_2=get_token.get_token()

    #上传视频文件
    media_id1=upload_photo(image_path,token_2)

    #获取灶眼对应信息
    zaoyan1,zaoyan2=get_zaoyan.duiying(zaoyan)

    #发送视频到企业微信
    send_photo(token_2,media_id1,zaoyan1,zaoyan2,datetime1,get_phototime)

    #删除视频文件
    os.remove(image_path)

if __name__=='__main__':
    take_video()