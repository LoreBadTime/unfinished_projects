import socket
import asyncio
from typing import final

def startclient(sock,tupl):
    sock.setblocking(True)
    print("client in connect\n")
    sock.connect(tupl)
    print("client connected\n")

def startserver(sock_server,tupl,lista):

    sock_server.setblocking(True)
    sock_server.bind(tupl)
    sock_server.listen()
    print("server in accept\n")
    client, address = sock_server.accept()
    lista.append(client)
    

async def main():
    CL_ADDRESS = "192.168.215.82" #indirizzo IP
    MY_ADDRESS = ""
    MY_PORT = 11000
    lista = []
    sock_server = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
    sock_cl = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
    
    await asyncio.gather(
            asyncio.to_thread(startserver,sock_server,(MY_ADDRESS,MY_PORT),lista),
            asyncio.to_thread(startclient,sock_cl,(CL_ADDRESS,MY_PORT)))
    server = sock_server
    client = lista[0]

    # this string must be modified from the other side
    sock_cl.sendall("Hello from there\n".encode("utf-8"))
    
    print("from other client: " + client.recv(1024).decode("utf-8"))
    
    sock_cl.close()
    sock_server.close()
    
asyncio.run(main())

