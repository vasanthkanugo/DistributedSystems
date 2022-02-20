import grpc
from concurrent import futures
import time
import db_pb2_grpc, db_pb2
from sqlite3 import Error
import sqlite3
import os
import create_table
from util import Util

db_file = None


def dict_factory(cursor, row):
    d = {}
    for idx, col in enumerate(cursor.description):
        d[col[0]] = row[idx]
    return d


class read_dbServicer(db_pb2_grpc.read_dbServicer):
    def read_db(self, request, context):
        conn = None
        query = request.query
        response = None
        try:
            conn = sqlite3.connect(db)
            conn.row_factory = dict_factory
            cursor = conn.cursor()
            cursor.execute(query)
            rows = cursor.fetchall()
            response = dict()
            response['items'] = rows
        except Error as e:
            return f"Error while reading data base: {e}"
        finally:
            if conn:
                conn.close()
        return Util.dict_to_json(response)


class write_dbServicer(db_pb2_grpc.write_dbServicer):
    def write_db(self, request, context):
        conn = None
        query = request.query
        try:
            conn = sqlite3.connect(db)
            conn.row_factory = dict_factory
            cursor = conn.cursor()
            cursor.execute(query)
            conn.commit()
        except Error as e:
            return f"Error while reading data base: {e}"
        finally:
            if conn:
                conn.close()
        return None


if __name__ == '__main__':
    __location__ = os.path.realpath(
        os.path.join(os.getcwd(), os.path.dirname(__file__)))
    db = os.path.join(__location__, 'database.db')

    print("Creating Databases")
    error = create_table.create_tables(db)
    if error:
        print("Error: " + error)
        exit()
    # create a gRPC server
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    db_pb2_grpc.add_read_dbServicer_to_server(read_dbServicer(), server)
    db_pb2_grpc.add_write_dbServicer_to_server(write_dbServicer(), server)
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
