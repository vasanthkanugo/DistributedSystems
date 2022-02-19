import grpc
from concurrent import futures
import time
import db_pb2_grpc, db_pb2
from sqlite3 import Error
import sqlite3
import os
import create_table

db_file = None

class execute_dbServicer(db_pb2_grpc.execute_dbServicer):
    def execute_db(self, request, context):
        response = db_pb2.response_msg()
        query = request.query
        connection_response = None
        # Code to execute the query

        conn = None
        try:
            conn = sqlite3.connect(db_file)
            print(sqlite3.version)
            cursor = conn.cursor()
            cursor.execute(query)
            cursor.fetchall()
            rows = {
                'items':[]
            }
            # if cursor:
            #     for db_r:
            #         rows['items'] +=

        except Error as e:
            print(f"Error executing query :{e}")
            connection_response = f"Error executing query :{e}"
        finally:
            if conn:
                conn.close()
        return response


if __name__ == '__main__':
    __location__ = os.path.realpath(
        os.path.join(os.getcwd(), os.path.dirname(__file__)))
    db = os.path.join(__location__, 'database.db')

    print("Creating Databases")
    error = create_table.create_tables(db)
    if not error:
        print("Error: "+error)
        exit()
    # create a gRPC server
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    db_pb2_grpc.add_execute_dbServicer_to_server(execute_dbServicer(), server)
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