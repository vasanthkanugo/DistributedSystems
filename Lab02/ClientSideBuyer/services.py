from database import db_util
from util import string_util, Util
from datetime import datetime as dt
from suds.client import Client


# Search in the items database
def search(data):
    response = db_util.read_db(db_name=db_util.item_db)
    if 'item_category' not in data['Body'] or 'keywords' not in data['Body']:
        return string_util.missing_request_parameters.format(request_parameters='item_category or keywords')
    category_items = [item for item in response.values() if
                      ('item_category' in item and data['Body']['item_category'] in item['item_category'])]
    keyword_items = list()
    for item in response.values():
        if 'keywords' in item:
            for keyword in data['Body']['keywords']:
                if keyword in item['keywords']:
                    keyword_items.append(item)
    list_items = [value for value in category_items if value in keyword_items]
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


# purchase the full cart or items
'''
{
    'client_id': client_id, 
    'credit_card':{
        'name' : 'name on credit card',
        'number': 'number on the credit card',
        'expiration_date' :'expiration_date with expected format '%M-%Y''
    },
    'price': price
}
'''


def make_purchase(data):
    json_body = data['Body']
    if 'client_id' not in json_body:
        return string_util.missing_request_parameters.format(request_parameters='client_id')
    elif 'credit_card' not in json_body:
        return string_util.missing_request_parameters.format(request_parameters='credit_card')
    elif 'name' not in json_body['credit_card'] or 'number' not in json_body['credit_card'] or 'expiration_date' not in \
            json_body['credit_card']:
        return string_util.missing_request_parameters.format(request_parameters='credit card details are missing')
    elif 'price' not in json_body:
        return string_util.missing_request_parameters.format(request_parameters='Invalid price for transaction')
    else:
        date = None
        try:
            date = dt.strptime(json_body['credit_card']['expiration_date'], '%M-%Y')
        except ValueError:
            return string_util.missing_request_parameters.format(request_parameters='Incorrect date format')
        if date < dt.now():
            return string_util.missing_request_parameters.format(request_parameters='Credit Card Expired')
    client = Client('http://localhost:8000/?wsdl', cache=None)
    # response = client.service.buy(Util.dict_to_json(json_body))
    response_json = Util.bytes_to_json(bytes(str(client.service.buy(Util.dict_to_json(json_body))), encoding='utf-8'))
    if response_json == string_util.ok:
        return None
    return response_json['error_message']
