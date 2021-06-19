import socket

def main():
    sock=socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.bind(('localhost', 7030))
    sock.listen(5)

    while True:
        conn,addr=sock.accept()
        data=conn.recv(1024)
        print(data)
        conn.send(b"HTTP/1.1 200 OK\r\nContent-Type:text/html; charset=utf-8\r\n\r\n")
        conn.send("电脑前的你真好看".encode("utf-8"))
        conn.close()
if __name__== "__main__":
       main()