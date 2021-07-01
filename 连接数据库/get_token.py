import requests
import json

def get_token():
#从获取token
    url="https://qyapi.weixin.qq.com/cgi-bin/gettoken?corpid=ww17c795da4df0c791&corpsecret=4h6Z4cGDV_efSsalIeZxYkJS_tvuMKNr855w7vfqWbQ"

    response=requests.request("GET",url)

    token_1=response.text
    token_1=json.loads(token_1)
    token_2=token_1.get('access_token')
    return (token_2)

if __name__=='__main__':
    get_token()