import socket
from _thread import *
from util import Util


def threaded_client(connection, function_call):
    while True:
        data = connection.recv(2048)
        if not data:
            break
        payload = Util.bytes_to_json(data)
        if function_call(payload, connection):
            break
    connection.close()


def start_server(host, port, function):
    ThreadCount = 0
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.bind((host, port))
        s.listen()
        while True:
            Client, address = s.accept()
            print('Connected to: ' + address[0] + ':' + str(address[1]))
            start_new_thread(threaded_client, (Client, function, ))
            ThreadCount += 1
            print('Thread Number: ' + str(ThreadCount))
        s.close()
    print("Socked Closed")
