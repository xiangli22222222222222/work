import json
import socket
import os

sock=socket.socket()
sock.connect(('82.157.37.136',8801))

while 1:
      cmd=input("请输入命令：")
      action,filename=cmd.strip().split(" ")
      filesize=os.path.getsize(filename)

      file_info={
            "action": action,
            "filename": filename,
            "filesize": filesize,

      }
      file_info_json=json.dumps(file_info).encode("utf8")
      sock.send(file_info_json)

      code=sock.recv(1024).decode("utf8")
      if code=="200":
            with open(filename,"rb") as f:
                  for line in f:
                        sock.send(line)
      else:
            print("服务器异常")