import requests
import json

# 指定ajax-get请求的url（通过抓包进行获取）
url = 'https://movie.douban.com/j/chart/top_list?'
# 封装ajax的get请求携带的参数(从抓包工具中获取) 封装到字典
param = {
    'type': '13',
    'interval_id': '100:90',
    'action': '',
    'start': '20',  # 从第20个电影开始获取详情
    'limit': '20',  # 获取多少个电影详情
    # 改变这两个参数获取的电影详情不一样
}
# 定制请求头信息，相关的头信息必须封装在字典结构中
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/66.0.3359.181 Safari/537.36',
}
# 发起ajax的get请求还是用get方法
response = requests.get(url=url, params=param, headers=headers)

# 获取响应内容：响应内容为json字符串
data = response.text
data = json.loads(data)
for data_dict in data:
    print(data_dict["rank"], data_dict["title"])