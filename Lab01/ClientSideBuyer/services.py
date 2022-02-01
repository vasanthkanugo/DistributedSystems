from database import db_util
from util import string_util


# Search in the items database
def search(data):
    response = db_util.read_db(db_name=db_util.item_db)
    return response


# Get all the elements in the cart
def get():
    response = db_util.read_db(db_name=db_util.cart_db)
    return response


# Add a new item to the cart database
def post(data):
    body = data['body']
    if not ('item_id' or 'quantity' in body):
        return string_util.missing_request_parameters.format(request_parameters='item_id or quantity')
    error = db_util.write_db(db_name=db_util.cart_db, entries=body)
    if error:
        return string_util.error_add_item_cart
    return None


# Update the cart
def put_or_update(data):
    body = data['body']
    if not ('item_id' or 'quantity' in body):
        return string_util.missing_request_parameters.format(request_parameters='item_id or quantity')
    error = db_util.write_db(db_name=db_util.cart_db, entries=body)
    if error:
        return string_util.error_add_item_cart
    return None


# Clear the cart
def delete():
    error = db_util.write_db(db_name=db_util.cart_db, entries=dict())
    if error:
        return string_util.error_add_item_cart
    return None
