from util import string_util, Util, db_util
from datetime import datetime as dt
from suds.client import Client
import seller_db_util

# Get list of all items in the database
def get_items(seller_id, db_name=None):
    query = seller_db_util.display_items.format(seller_id=seller_id)
    response = db_util.read_db(query, db_name=db_name)
    return response

# Add a new item for sale
def add_item_for_sale(data, db_name=None):
    if 'items' not in data:
        return string_util.missing_request_parameters.format(request_parameters='items')
    items = data['items']
    # should we have a batch write to db thing.
    # eliminate batch write for now
    for item in items:
        query = seller_db_util.add_items_for_sale.format(name=item['name'],
                                                       category=data['category'],
                                                        keywords=data['keywords'],
                                                        condition=data['condition'],
                                                        sale_price=data['sale_price'],
                                                       quantity=data['quantity'])
        error = db_util.write_db(query, db_name=db_name)
        if error:
            print("Error writing to db: "+error)
    if error:
        return string_util.error_add_item_sale
    return None

# Delete an item from the item list
def delete_item(item_id, db_name=None):
    query = seller_db_util.delete_item_from_sale.format(item_id=item_id)
    error = db_util.write_db(query, db_name=db_name)
    if error:
        return string_util.error_add_item_cart
    return None

# Update an item's quantity from the item list
def remove_item(data, db_name=None):
    if not ('item_id' or 'quantity' in data):
        return string_util.missing_request_parameters.format(request_parameters='item_id or quantity')
    if data['quantity'] == 0:
        query = seller_db_util.delete_item_from_sale.format(item_id=data['item_id'])
    else:
        query = seller_db_util.remove_item_from_sale.format(quantity=data['quantity'], item_id=data['item_id'])
    error = db_util.write_db(query, db_name=db_name)
    if error:
        return string_util.error_add_item_cart
    return None

# Update sale price for an item
def update_sale_price(data, db_name=None):
    if not ('item_id' or 'sale_price' in data):
        return string_util.missing_request_parameters.format(request_parameters='item_id or quantity')
    query = seller_db_util.update_sale_price_of_item.format(item_id=data['item_id'], sale_price=data['sale_price'])
    error = db_util.write_db(query, db_name=db_name)
    if error:
        return string_util.error_add_item_cart
    return None

# Get Seller rating - for the given seller
def get_seller_rating(seller_id, db_name=None):
    query = seller_db_util.get_seller_ratings.format(seller_ids=seller_id)
    seller_ratings = db_util.read_db(query, db_name=db_name)
    return seller_ratings


# Create Seller Account
def create_seller_account(data, db_name=None):
    if not ('user_name' or 'password' or 'name' in data):
        return string_util.missing_request_parameters.format(request_parameters='user_name or password or name')
    query = seller_db_util.create_account.format(name=data['name'],
                                                user_name=data['user_name'],
                                                passwowrd=data['password'])
    error = db_util.write_db(query, db_name=db_name)
    if error:
        return "Error creating buyer"
    return None

# Login to Seller Account
def login_seller_account(data, db_name=None):
    if not ('user_name' or 'password' in data):
        return string_util.missing_request_parameters.format(request_parameters='user_name or password or name')
    query = seller_db_util.login_account.format(user_name=data['user_name'],
                                                passwowrd=data['password'])
    login_details = db_util.read_db(query, db_name=db_name)
    if 'Error' in login_details:
        return login_details
    login_details = login_details['items'][0]
    return login_details





# Update the item list
# def put_or_update(data):
#     updated_list = db_util.read_db(db_name=db_util.item_db)
#     print(updated_list)
#     if 'item_id' not in data['Body'] or 'quantity' not in data['Body']:
#         return string_util.missing_request_parameters.format(request_parameters='item_id or quantity')
#     body = data['Body']
#     if body['item_id'] not in updated_list:
#         return string_util.item_missing.format(item_id=body['item_id'])
#     item = updated_list[body['item_id']]
#     item['quantity'] = body['quantity']
#     if item['quantity'] == 0:
#         item = None
#     response_message = db_util.write_db(db_name=db_util.item_db, entries={body['item_id']: item})
#     print(response_message)
#     print("put/update db")
#     return None
