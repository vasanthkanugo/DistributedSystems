import jsonpickle

from util import string_util, Util, db_util
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
                                                        category=item['category'],
                                                        keywords=jsonpickle.dumps(item['keywords']),
                                                        condition=item['condition'],
                                                        sale_price=item['sale_price'],
                                                        quantity=item['quantity'],
                                                        seller_id=item['seller_id'])
        error = db_util.write_db(query, db_name=db_name)
        if error:
            print("Error writing to db: "+error)
    if error:
        return string_util.error_add_item_sale
    return None

# Delete an item from the item list
def delete_item(item_id, seller_id, db_name=None):
    query = seller_db_util.delete_item_from_sale.format(item_id=item_id, seller_id=seller_id)
    error = db_util.write_db(query, db_name=db_name)
    if error:
        return string_util.error_add_item_cart
    return None

# Update an item's quantity from the item list
def remove_item(data, db_name=None):
    if not ('item_id' or 'quantity' or 'seller_id' in data):
        return string_util.missing_request_parameters.format(request_parameters='item_id or quantity or seller_id')
    if 'quantity' in data.keys():
        if data['quantity'] == 0:
            query = seller_db_util.delete_item_from_sale.format(item_id=data['item_id'], seller_id=data['seller_id'])
        else:
            query = seller_db_util.remove_item_from_sale.format(quantity=data['quantity'], item_id=data['item_id'], seller_id=data['seller_id'])
        error = db_util.write_db(query, db_name=db_name)
    else:
        if 'sale_price' not in data:
            return string_util.missing_request_parameters.format(request_parameters='sale price')
        query = seller_db_util.update_sale_price_of_item.format(item_id=data['item_id'], sale_price=data['sale_price'],
                                                                seller_id=data['seller_id'])
        error = db_util.write_db(query, db_name=db_name)
        if error:
            return string_util.error_add_item_cart
        return None

    if error:
        return string_util.error_add_item_cart
    return None

# Update sale price for an item
def update_sale_price(data, db_name=None):
    if not ('item_id' or 'sale_price' or 'seller_id' in data):
        return string_util.missing_request_parameters.format(request_parameters='item_id or quantity or seller_id')
    query = seller_db_util.update_sale_price_of_item.format(item_id=data['item_id'], sale_price=data['sale_price'], seller_id=data['seller_id'])
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
                                                password=data['password'])
    error = db_util.write_db(query, db_name=db_name)
    if error:
        return "Error creating Seller"
    return None

# Login to Seller Account
def login_seller_account(data, db_name=None):
    if not ('user_name' or 'password' in data):
        return string_util.missing_request_parameters.format(request_parameters='user_name or password or name')
    query = seller_db_util.login_account.format(user_name=data['user_name'],
                                                password=data['password'])
    login_details = db_util.read_db(query, db_name=db_name)
    if 'Error' in login_details:
        return login_details
    login_details = login_details['items'][0]
    return login_details
