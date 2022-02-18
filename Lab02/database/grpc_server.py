import grpc
from concurrent import futures
import time
import route_guide_pb2
import route_guide_pb2_grpc


class read_dbServicer(route_guide_pb2_grpc.read_dbServicer):
    def read_db(self, request, context):
        response = route_guide_pb2.read_db_msg()
        return response

# create a gRPC server
server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))

route_guide_pb2_grpc.add_read_dbServicer_to_server(
    read_dbServicer(), server)


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