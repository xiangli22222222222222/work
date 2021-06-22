import socket
import os
import json
client_1=socket.socket()

client_1.connect(("127.0.0.1",8801))

f=os.listdir("C:/Users/admin/Desktop/m")
for f1 in f:
    (f2,f3)=os.path.splitext(f1)
    data=open('C:/Users/admin/Desktop/m/'+f1,'rb')

    data_size=os.path.getsize('C:/Users/admin/Desktop/m/'+f1)

    data_size=str(data_size)
    data_name=f1

    print(data_size)

    data_json={"data_size1":data_size,"data_name1":data_name}

    data_json_send=json.dumps(data_json)

    client_1.send (data_json_send.encode('utf8'))


    for data1 in data:
       client_1.send(data1)


client_1.close()
