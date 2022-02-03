from database import db_util
from util import string_util


# Search in the items database
def search(keyword):
    response = db_util.read_db(db_name=db_util.item_db)
    list_items = [item for item in response.values() if keyword in item['item_category']]
    return list_items


# Get all the elements in the cart
def get():
    response = db_util.read_db(db_name=db_util.cart_db)
    return response


# Add a new item to the cart database
def post(data):
    body = data['Body']
    if 'items' not in body:
        return string_util.missing_request_parameters.format(request_parameters='items')
    items = body['items']
    entries = db_util.read_db(db_name=db_util.cart_db)
    for item in items:
        if not ('item_id' or 'quantity' in body):
            return string_util.missing_request_parameters.format(request_parameters='item_id or quantity')
        entries.update(
            {item['item_id']: item['quantity']}
        )
    error = db_util.write_db(db_name=db_util.cart_db, entries=entries)
    if error:
        return string_util.error_add_item_cart
    return None


# Update the cart
def put_or_update(data):
    body = data['Body']
    if not ('item_id' or 'quantity' in body):
        return string_util.missing_request_parameters.format(request_parameters='item_id or quantity')
    error = db_util.write_db(db_name=db_util.cart_db, entries={body['item_id']: body['quantity']})
    if error:
        return string_util.error_add_item_cart
    return None


# Clear the cart
def delete():
    error = db_util.write_db(db_name=db_util.cart_db, entries=dict())
    if error:
        return string_util.error_add_item_cart
    return None
