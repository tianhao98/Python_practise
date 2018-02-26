import socket, os

client = socket.socket()
client.connect(('127.0.0.1', 9999))

while True:
    command = input('>>:')
    if not command:
        continue
    client.send(command.encode('utf8'))
    comm_resv_size = int(client.recv(1024))
    print(comm_resv_size)
    comm_resv=''
    while comm_resv_size >= 1024:
        data = client.recv(1024).decode()
        comm_resv = comm_resv+data
        comm_resv_size -= 1024
    else:
        data = client.recv(comm_resv_size).decode()
        comm_resv = comm_resv + data
        print(comm_resv)
        del comm_resv
