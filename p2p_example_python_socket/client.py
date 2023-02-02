import socket
from typing import final

ADDRESS = "192.168.215.82"
PORT = 11000
try:
    sock = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
    sock.setblocking(True)
    sock.settimeout(20)
    sock.connect((ADDRESS,PORT))

    sock.sendall("1".encode('utf-8'))
    print("connesso al " + sock.recv(1024).decode('utf-8'))
    sock.sendall("DISCONNECT".encode('utf-8'))

    if sock.recv(1024).decode("utf-8") == "ok":
        print("received shutdown")
        sock.sendall("ok".encode('utf-8'))
       
finally:
    sock.shutdown(socket.SHUT_RDWR)
    sock.close()
