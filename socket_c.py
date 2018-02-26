import socket

client = socket.socket()
client.connect(('127.0.0.1', 9999))
while True:
    data = input('>>:')
    client.send(data.encode())