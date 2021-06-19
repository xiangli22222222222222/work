import json
import socket

sock=socket.socket()
sock.bind(('127.0.0.1',8800))
sock.listen(5)


while 1:
    print("sever is working!!")
    conn,adr=sock.accept()
    while 1:
           data=conn.recv(1024).decode("utf8")
           file_info=json.loads(data)
           print("file_info",file_info)

           action=file_info.get('action')
           filename=file_info.get('filename')
           filesize=file_info.get('filesize')
           conn.send(b"200")
           with open("put/"+filename,"wb") as f:
               recv_data_length=0
               while recv_data_length<filesize:
                   data=conn.recv(1024)
                   recv_data_length+=len(data)
                   f.write(data)
                   print("文件总大小，%s,已成功接收%s"%(filesize,recv_data_length))
           print("接收成功")