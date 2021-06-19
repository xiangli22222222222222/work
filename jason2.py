import requests

url = 'xxx'

files={'file':('test2.jpg',open('test2.jpg','rb'),'image/jpeg')}

rsp=requests.post(url,files=files)

print(rsp.request.text)