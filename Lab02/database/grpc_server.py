import grpc
from concurrent import futures
import time
from PIL import Image
import io
import base64
import lab6_pb2
import lab6_pb2_grpc


class addServicer(lab6_pb2_grpc.addServicer):
    def add(self, request, context):
        response = lab6_pb2.addMsg()
        response.a = request.a + request.b
        return response


class imageServicer(lab6_pb2_grpc.rawimageServicer):
    def rawimage(self, request, context):
        response = lab6_pb2.addMsg()
        ioBuffer = io.BytesIO(request.img)
        i = Image.open(ioBuffer)
        response.a = i.size[0]
        response.b = i.size[1]
        return response


class vectorProductServicer(lab6_pb2_grpc.vectorProductServicer):
    def vecproduct(self, request, context):
        response = lab6_pb2.vectorMsgResp()
        sum = 0
        length = len(request.a)
        for i in range(length):
            sum += request.a[i] * request.b[i]

        response.result = sum
        print(sum)
        return response


class jsonImageServicer(lab6_pb2_grpc.jsonImageServicer):
    def jsonimage(self, request, context):
        image_data = base64.b64decode(request.image)
        response = lab6_pb2.addMsg()
        ioBuffer = io.BytesIO(image_data)
        i = Image.open(ioBuffer)
        response.a = i.size[0]
        response.b = i.size[1]

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