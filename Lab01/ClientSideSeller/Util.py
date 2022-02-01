import json
import pickle


def dict_to_bytes(map):
    return bytes(json.dumps(map), encoding='utf8')


def bytes_to_json(payload):
    json_dump = None
    try:
        json_dump = json.loads(str(payload))
    except:
        print("E: invalid json " + str(payload))
    return json_dump

def dict_to_json(object):
    return json.dumps(object)


def read_db(db_name):
    try:
        db_file = open(db_name, 'rb')
        db_entries = pickle.load(db_name)
        if db_file is not None:
            db_file.close()
    except:
        print("E: error loading from db")
        return "E: error loading from db"
    return db_entries


def write_db(entries, db_name):
    db_entries = read_db(db_name=db_name)
    if db_entries is None:
        db_entries = dict()
    db_entries.update(entries)
    try:
        db_file = open(db_name, 'wb')
        pickle.dump(db_entries, db_file)
        db_file.close()
    except:
        print('E: error writing to db')
        return 'E: error writing to db'
    return None
