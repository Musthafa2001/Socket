import socket

Host=""
Port="4444"

server=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
server.bind((Host,Port))