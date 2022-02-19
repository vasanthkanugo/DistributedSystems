import grpc
from database import db_pb2, db_pb2_grpc
import struct
import sys
from time import perf_counter
import base64
import random

addr = "545"
endpoint = 'add'
num_tests = int()


channel = grpc.insecure_channel(addr)

if endpoint == 'add':
    stub = db_pb2_grpc.execute_dbStub(channel)
    query = None
    stub.execute_db(query)

    timer_start = perf_counter()
    for i in range(num_tests):
        number = route_guide_pb2_grpc.read_db_msg()
        resp = stub.add(number)
        print(resp.a)
    timer_stop = perf_counter()
