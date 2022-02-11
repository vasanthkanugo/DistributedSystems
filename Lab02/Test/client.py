import socket
import time

import client_side_buyer
import client_side_seller
from util import Util


HOST = '127.0.0.1'  # The server's hostname or IP address
PORT = 65345      # The port used by the server

for operation in client_side_seller.operations:
    start_time = time.time()
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.connect((HOST, PORT))
        print('Operation: '+str(operation['Header']))
        print('Operation: '+str(operation))

        s.sendall(Util.dict_to_bytes(operation))
        data = s.recv(1024)
        print('Received', repr(data))
        print('----------------------------------------------')
        s.close()
    print('Time Taken: ' + str(time.time() - start_time))
    print('----------------------------------------------')

PORT = 65346        # The port used by the server


for operation in client_side_buyer.operations:
    start_time = time.time()
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.connect((HOST, PORT))
        print('Operation: '+str(operation['Header']))
        print('Operation: '+str(operation))

        s.sendall(Util.dict_to_bytes(operation))
        data = s.recv(1024)
        print('Received', repr(data))
        print('----------------------------------------------')
        s.close()
    print('Time Taken: ' + str(time.time() - start_time))
    print('----------------------------------------------')