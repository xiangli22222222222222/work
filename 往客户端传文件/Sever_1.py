import socket
import json

server_1=socket.socket()

server_1.bind(('127.0.0.1',8801))

server_1.listen(3)
number=0
if number<10:
    conn,addr=server_1.accept()

    file_size= conn.recv(1024)

    file_size=file_size.decode('utf8')

    file_size=json.loads(file_size)

    file_size1=file_size.get("data_size1")

    file_name=file_size.get("data_name1")


    print(file_size1)


    file_size1=int(file_size1)

    print(file_size1)

    f=open("e:/work/123/"+file_name,'wb')
    recv_size = 0
    while recv_size < file_size1:
        data=conn.recv(1024)
        print("这个长度有%s"%len(data))
        recv_size += len(data)
        f.write(data)
        print("已经接受文件大小%s,总文件大小%s"%(recv_size,file_size1))
    f.close()
    number+=1
    print(number)
print("接受成功")


