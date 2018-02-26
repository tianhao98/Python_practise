import socket, os

server = socket.socket()
server.bind(('127.0.0.1', 9999))
server.listen()

while True:
    conn, addr = server.accept()
    print(addr)
    while True:
        try:
            data = conn.recv(1024)
        except ConnectionResetError as e:
            print('client colse....')
            conn.close()
            break
        if not data:
            print('client colse....')
            break
        comm = os.popen(data.decode()).read()
        if len(comm) == 0:comm = 'command output is not....'
        comm_resv_size = len(comm.encode('utf-8'))
        print(comm_resv_size)
        conn.send(str(comm_resv_size).encode())
        print('%s is command : %s' % (addr, data.decode()))
        if len(comm) == 0:
            comm = 'commmand is not put..'
        conn.send(comm.encode('utf8'))
    conn.close()

bytes