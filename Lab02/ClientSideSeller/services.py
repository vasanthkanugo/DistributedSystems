from database import db_util
from util import string_util


# Get list of all items in the database
def get():
    response_message = db_util.read_db(db_name=db_util.item_db)
    print(response_message)
    print("read db")
    return response_message


# Add a new item to the database
def post(data):
    for element in data['Body']:
        response_message = db_util.write_db(db_name=db_util.item_db, entries={element['item_id']: element})
    print(response_message)
    print("post db")
    return None


# Update the item list
def put_or_update(data):
    updated_list = db_util.read_db(db_name=db_util.item_db)
    print(updated_list)
    if 'item_id' not in data['Body'] or 'quantity' not in data['Body']:
        return string_util.missing_request_parameters.format(request_parameters='item_id or quantity')
    body = data['Body']
    if body['item_id'] not in updated_list:
        return string_util.item_missing.format(item_id=body['item_id'])
    item = updated_list[body['item_id']]
    item['quantity'] = body['quantity']
    if item['quantity'] == 0:
        item = None
    response_message = db_util.write_db(db_name=db_util.item_db, entries={body['item_id']: item})
    print(response_message)
    print("put/update db")
    return None


# Delete an item from the item list
def delete(data):
    return put_or_update(data)
