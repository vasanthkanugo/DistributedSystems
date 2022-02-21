from util import Util, string_util
import services
from flask import Flask, request

host, port, app = '127.0.0.1', 9001, Flask(__name__)


@app.route('/api/v1/seller/items', methods=['GET'])
def enlist():
    seller_id = request.args.get('seller_id')
    if not seller_id:
        string_util.error['error_message'] = string_util.missing_request_parameters.format(request_parameters='seller_id')
        return Util.get_response_object(string_util.error, 401)
    items_list = services.get_items(seller_id=seller_id)
    return Util.get_response_object(items_list, 200)

@app.route('/api/v1/seller/items/ratings', methods=['GET'])
def enlist_seller_ratings():
    seller_id = request.args.get('seller_id')
    if not seller_id:
        string_util.error['error_message'] = string_util.missing_request_parameters.format(request_parameters='seller_id')
        return Util.get_response_object(string_util.error, 401)
    items_list = services.get_seller_rating(seller_id=seller_id)
    return Util.get_response_object(items_list, 200)

@app.route('/api/v1/seller/items', methods=['POST'])
def add():
    payload = request.get_json(force=True)
    response = services.add_item_for_sale(data=payload)
    if response is not None:
        string_util.error['error_message'] = response
        return Util.get_response_object(string_util.error, 401)
    else:
        return Util.get_response_object(response=None, status_code=200)

@app.route('/api/v1/seller/items', methods=['PUT', 'UPDATE'])
def update():
    payload = request.get_json(force=True)
    response = services.remove_item(data=payload)
    if response is not None:
        string_util.error['error_message'] = response
        return Util.get_response_object(string_util.error, 401)
    else:
        return Util.get_response_object(response=None, status_code=200)

@app.route('/api/v1/seller/items', methods=['DELETE'])
def delete():
    item_id = request.args.get('item_id')
    seller_id = request.args.get('seller_id')
    if not (item_id or seller_id):
        string_util.error['error_message'] = string_util.missing_request_parameters.format(request_parameters='item_id or seller_id')
        return Util.get_response_object(string_util.error, 401)
    response = services.delete_item(item_id, seller_id, db_name=None)
    if response is not None:
        string_util.error['error_message'] = response
        return Util.get_response_object(string_util.error, 401)
    else:
        return Util.get_response_object(response=None, status_code=200)


@app.route('/api/v1/seller/account/create', methods=['POST'])
def create_account():
    payload = request.get_json(force=True)
    response = services.create_seller_account(data=payload)
    if response is not None:
        string_util.error['error_message'] = response
        return Util.get_response_object(string_util.error, 401)
    else:
        return Util.get_response_object(response=None, status_code=200)


@app.route('/api/v1/seller/account/login', methods=['POST'])
def login():
    payload = request.get_json(force=True)
    response = services.login_seller_account(data=payload)
    if 'Error' in response:
        string_util.error['error_message'] = response
        return Util.get_response_object(string_util.error, 401)
    else:
        return Util.get_response_object(response=response, status_code=200)


@app.route('/api/v1/seller/account/logout', methods=['GET'])
def logout():
    return Util.get_response_object(response=None, status_code=200)


app.run(host, port)
