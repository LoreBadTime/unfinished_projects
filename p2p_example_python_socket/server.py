import socket
from typing import final

ADDRESS = ""
PORT = 11000
try:
    sock = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
    sock.setblocking(True)
    
    sock.bind((ADDRESS,PORT))
    print("server in ascolto")
    sock.listen()
    client, address = sock.accept()
    sock.settimeout(20)
    print("connesso al client" + client.recv(1024).decode('utf-8'))
    client.sendall("server".encode('utf-8'))

    if client.recv(1024).decode("utf-8") == "DISCONNECT":
        client.sendall("ok".encode('utf-8'))
        if client.recv(1024).decode("utf-8") == "ok":
            print("received shutdown")
           
finally:
    sock.shutdown(socket.SHUT_RDWR)
    sock.close()