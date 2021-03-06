import grpc
import os
from util import Util
from database import db_pb2, db_pb2_grpc

__location__ = os.path.realpath(
    os.path.join(os.getcwd(), os.path.dirname(__file__)))
db = os.path.join(__location__, '../database/database.db')


def dict_factory(cursor, row):
    d = {}
    for idx, col in enumerate(cursor.description):
        d[col[0]] = row[idx]
    return d

'''
returns: 
case_1: Error statement - if error encountered
case_2: {
    'items':[
        {'col_1':val_1},
        {'col_2':val_2}
    ]
}
should return a json object. 
if error:
{
    'Error' : error_reponse
}
'''
host = "127.0.0.1"
addr = f"{host}:50051"

def read_db(query, db_name=db):
    channel = grpc.insecure_channel(addr)
    stub = db_pb2_grpc.read_dbStub(channel)
    message = db_pb2.read_db_msg(query=query)
    response = stub.read_db(message)
    response = response.response
    json = Util.json_to_dic(response)
    return json


def write_db(query, db_name=db):
    channel = grpc.insecure_channel(addr)
    stub = db_pb2_grpc.write_dbStub(channel)
    message = db_pb2.write_db_msg(query=query)
    response = stub.write_db(message)
    response = response.response
    json = Util.json_to_dic(response)
    return json
