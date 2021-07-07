import requests
import json

def get_token(appsecret):
#从获取token
    url=appsecret

    response=requests.request("GET",url)

    token_1=response.text
    token_1=json.loads(token_1)
    token_2=token_1.get('access_token')
    return (token_2)

if __name__=='__main__':
    get_token(appsecret)