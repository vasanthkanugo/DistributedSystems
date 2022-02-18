import grpc
# import the generated classes
import route_guide_pb2
import route_guide_pb2_grpc
import struct
import sys
from time import perf_counter
import base64
import random

addr = sys.argv[1]
endpoint = sys.argv[2]
num_tests = int(sys.argv[3])


channel = grpc.insecure_channel(addr)

if endpoint == 'add':
    stub = route_guide_pb2_grpc.addStub(channel)

    timer_start = perf_counter()
    for i in range(num_tests):
        number = route_guide_pb2.read_db_msg()
        resp = stub.add(number)
        print(resp.a)
    timer_stop = perf_counter()

    total = timer_stop - timer_start
    avg = (total / num_tests) * 1000
    print("Took", avg, "ms per operation")


elif endpoint == 'vectorProduct':
    stub = lab6_pb2_grpc.vectorProductStub(channel)
    timer_start = perf_counter()

    list1 = []
    list2 = []

    for i in range(101):
        list1.append(random.random())
        list2.append(random.random())

    for i in range(num_tests):
        number = lab6_pb2.vectorMsg(a=list1, b=list2)
        resp = stub.vecproduct(number)
        print(resp.result)
    timer_stop = perf_counter()

    total = timer_stop - timer_start
    avg = (total / num_tests) * 1000
    print("Took", avg, "ms per operation")

elif endpoint == 'jsonImage':
    stub = lab6_pb2_grpc.jsonImageStub(channel)
    timer_start = perf_counter()
    for i in range(num_tests):
        string = base64.b64encode(img).decode('utf-8')
        number = lab6_pb2.jsonImageMsg(image=string)
        resp = stub.jsonimage(number)
        print(resp.a, resp.b)
    timer_stop = perf_counter()

    total = timer_stop - timer_start
    avg = (total / num_tests) * 1000
    print("Took", avg, "ms per operation")