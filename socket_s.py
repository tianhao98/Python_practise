import  socket
import threading
from multiprocessing import Process
import os





def ThreadConn(conn):
    while True:
        try:
            print(os.getpid())
            data = conn.recv(1024)
        except ConnectionResetError as e:
            print(e)
            return
        print(data)
        # conn.send(data)

if __name__ =='__main__':
    server = socket.socket()
    server.bind(('127.0.0.1', 9999))
    server.listen()
    while True:
        conn, addr = server.accept()
        print(addr)
        p1 = Process(target=ThreadConn, args=(conn,))
        p1.start()

