import requests
import get_token2
import json

def get_userid(token_2):
    url='https://qyapi.weixin.qq.com/cgi-bin/appchat/create?access_token='+token_2

    send_json = {
    "name" : "NAME",
    "owner" : "LiXiang01",
    "userlist" : ["LiXiang01", "hbscherliguokunhse1987", "ash"],
    "chatid" : "1234567890"
                 }

    response = requests.request("POST", url, data=json.dumps(send_json))

    print(response.text)


def qun_liao(token_2):
    url = "https://qyapi.weixin.qq.com/cgi-bin/message/send?access_token=" + token_2

    send_json = {
    "touser": "@all",
    "toparty": "@all",
    "totag": "@all",
    "chatid": "1234567890",
    "msgtype":"text",
    "agentid": "1000002",
    "text":{
        "content" : "群聊测试消息"
    },
    "safe":0
                 }

    response = requests.request("POST", url, data=json.dumps(send_json))

    print(response.text)

if __name__=='__main__':
    secret="https://qyapi.weixin.qq.com/cgi-bin/gettoken?corpid=ww17c795da4df0c791&corpsecret=jX2J51cbXQKGl67kKHiqaiWPYv_J9hUIjlnifkSrtqQ"
    token2=get_token2.get_token(secret)
    get_userid(token2)

    qun_liao(token2)