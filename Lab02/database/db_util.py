import os
import sqlite3
from sqlite3 import Error
from util import Util

__location__ = os.path.realpath(
    os.path.join(os.getcwd(), os.path.dirname(__file__)))
db = os.path.join(__location__, 'database.db')


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

def read_db(query, db_name=db):
    conn = None
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


def write_db(query, db_name=db):
    conn = None
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
