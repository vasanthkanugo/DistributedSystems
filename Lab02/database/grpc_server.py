import grpc
from concurrent import futures
import time
import io
import base64
import route_guide_pb2
import route_guide_pb2_grpc


class read_dbServicer(route_guide_pb2_grpc.read_dbServicer):
    def read_db(self, request, context):
        response = route_guide_pb2.read_db_msg()
        return response

class vectorProductServicer(route_guide_pb2_grpc.vectorProductServicer):
    def vecproduct(self, request, context):
        response = route_guide_pb2_grpc.vectorMsgResp()
        sum = 0
        length = len(request.a)
        for i in range(length):
            sum += request.a[i] * request.b[i]

        response.result = sum
        print(sum)
        return response



# create a gRPC server
server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))

lab6_pb2_grpc.add_addServicer_to_server(
    addServicer(), server)

lab6_pb2_grpc.add_rawimageServicer_to_server(
    imageServicer(), server)

lab6_pb2_grpc.add_vectorProductServicer_to_server(
    vectorProductServicer(), server)

lab6_pb2_grpc.add_jsonImageServicer_to_server(
    jsonImageServicer(), server)

print('Starting server. Listening on port 50051.')
server.add_insecure_port('[::]:50051')
server.start()

# since server.start() will not block,
# a sleep-loop is added to keep alive
try:
    while True:
        time.sleep(86400)
except KeyboardInterrupt:
    server.stop(0)