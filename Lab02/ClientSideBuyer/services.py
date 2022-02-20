from database import db_util
from util import string_util, Util
from datetime import datetime as dt
from suds.client import Client
import buyer_db_util


# Search in the items database
def search(data, db_name=None):
    if 'item_category' not in data or 'keywords' not in data:
        return string_util.missing_request_parameters.format(request_parameters='item_category or keywords')
    query = buyer_db_util.search_items.format(category=data['item_category'],
                                              keywords=','.join(data['keywords']))
    response = db_util.read_db(query, db_name=db_name)
    return response


# Get all the elements in the cart
def display(buyer_id, db_name=None):
    query = buyer_db_util.display_cart.format(buyer_id=buyer_id)
    response = db_util.read_db(query, db_name=db_name)
    return response


# Add a new item to the cart database
def add_item_to_cart(data, db_name=None):
    if 'items' not in data:
        return string_util.missing_request_parameters.format(request_parameters='items')
    items = data['items']
    # should we have a batch write to db thing.
    # eliminate batch write for now
    for item in items:
        query = buyer_db_util.add_items_to_cart.format(item_id=item['item_id'],
                                                       buyer_id=data['buyer_id'],
                                                       quantity=data['quantity'])
        error = db_util.write_db(query, db_name=db_name)
        if error:
            print("Error writing to db: "+error)
    if error:
        return string_util.error_add_item_cart
    return None


# Update the cart
def remove_item_from_cart(data, db_name=None):
    if not ('item_id' or 'quantity' in data):
        return string_util.missing_request_parameters.format(request_parameters='item_id or quantity')
    if data['quantity'] == 0:
        query = buyer_db_util.delete_item_from_cart.format(buyer_id=data['buyer_id'], item_id=data['item_id'])
    else:
        query = buyer_db_util.remove_item_from_cart.format(buyer_id=data['buyer_id'], item_id=data['item_id'], quantity=data['quantity'])
    error = db_util.write_db(query, db_name=db_name)
    if error:
        return string_util.error_add_item_cart
    return None


# Clear the cart
def clear_cart(buyer_id, db_name=None):
    query = buyer_db_util.delete_cart.format(buyer_id=buyer_id)
    error = db_util.write_db(query, db_name=db_name)
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


def make_purchase(data, db_name=None):
    if 'client_id' not in data:
        return string_util.missing_request_parameters.format(request_parameters='client_id')
    elif 'credit_card' not in data:
        return string_util.missing_request_parameters.format(request_parameters='credit_card')
    elif 'name' not in data['credit_card'] or 'number' not in data['credit_card'] or 'expiration_date' not in \
            data['credit_card']:
        return string_util.missing_request_parameters.format(request_parameters='credit card details are missing')
    elif 'price' not in data:
        return string_util.missing_request_parameters.format(request_parameters='Invalid price for transaction')
    else:
        date = None
        try:
            date = dt.strptime(data['credit_card']['expiration_date'], '%M-%Y')
        except ValueError:
            return string_util.missing_request_parameters.format(request_parameters='Incorrect date format')
        if date < dt.now():
            return string_util.missing_request_parameters.format(request_parameters='Credit Card Expired')
    client = Client('http://localhost:8000/?wsdl', cache=None)
    # response = client.service.buy(Util.dict_to_json(json_body))
    response_json = Util.bytes_to_json(bytes(str(client.service.buy(Util.dict_to_json(data))), encoding='utf-8'))
    if response_json == string_util.ok:
        return None
    return response_json['error_message']


'''
Input Structure: {
    'client_id': client_id, 
    'feedbacks' :[
        { 
            'item_id': item_id, 
            'rating': 0 or 1(thumbs up or down), 
            'feedback': 'any or none'
        }, 
        { 
            'item_id': item_id, 
            'rating': 0 or 1(thumbs up or down), 
            'feedback': 'any or none'
        }
    ]
}
'''

# Submit feedback for a set of items
def submit_feedback(data, db_name=None):
    return None


# Get Seller rating - for the given buyer_id
def get_seller_rating(buyer_id, db_name=None):
    query = buyer_db_util.search_seller_ids.format(buyer_id=buyer_id)
    seller_ids = db_util.read_db(query, db_name=db_name)
    if not seller_ids:
        return None
    query = buyer_db_util.get_seller_ratings.format(seller_ids=','.join(seller_ids))
    seller_ratings = db_util.read_db(query, db_name=db_name)
    return seller_ratings

# Get Buyer History
def get_buyer_history(buyer_id, db_name=None):
    query = buyer_db_util.get_buyer_history.format(buyer_id=buyer_id)
    history = db_util.read_db(query, db_name=db_name)
    return history


# Create Buyer Account
def create_buyer_account(data, db_name=None):
    if not ('user_name' or 'password' or 'name' in data):
        return string_util.missing_request_parameters.format(request_parameters='user_name or password or name')
    query = buyer_db_util.create_account.format(name=data['name'],
                                                user_name=data['user_name'],
                                                passwowrd=data['password'])
    error = db_util.write_db(query,db_name=db_name)
    if error:
        return "Error creating buyer"
    return None

# Login to Buyer Account
def login_buyer_account(data, db_name=None):
    if not ('user_name' or 'password' in data):
        return string_util.missing_request_parameters.format(request_parameters='user_name or password or name')
    query = buyer_db_util.login_account.format(user_name=data['user_name'],
                                                passwowrd=data['password'])
    login_details = db_util.read_db(query, db_name=db_name)
    if 'Error' in login_details:
        return login_details
    login_details = login_details['items'][0]
    return login_details


