import json

def dict_to_bytes(map):
    return bytes(json.dumps(map), encoding='utf8')


def bytes_to_json(payload):
    json_dump = None
    try:
        json_dump = json.loads(bytes.decode(payload))
    except:
        print("E: invalid json " + str(payload))
    return json_dump

def dict_to_json(object):
    return json.dumps(object)

def json_to_dic(payload):
    json_dump = None
    try:
        json_dump = json.loads(bytes.decode(payload))
    except:
        print("E: invalid json " + str(payload))
    return json_dump
