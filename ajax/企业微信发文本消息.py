import requests
import json
url = "https://qyapi.weixin.qq.com/cgi-bin/message/send?access_token=PW6FKajRfRPx2NVXC4M4xCFITnx0o5kAzbGllX4JVd30ovoaSO2PMkQnsRa-XpXGgS6qV5JyFZnMTBgnnCPYL_OtF7v3LYuOd4B3JlSK_3hxjXSuHZWtX4JPoTZFAr3tYERMq025F6y82OjzJBTyOQ4XWjlphvPpO4Jd8jJqd7_R966mrohHiKm1yNT2rD25SArjP2v__8nypiTxb3l1Kg"
data = {
   "touser" : "@all",
   "msgtype" : "text",
   "agentid" : 1000004,
   "text" : {
       "content" : "你有问题知道嘛？"
   }
}
#字符串格式
res = requests.post(url=url,data=json.dumps(data))
print(res.text)
