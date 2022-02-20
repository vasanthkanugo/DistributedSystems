from util import Util, string_util
import services
from flask import Flask, request

host, port, app = '127.0.0.1', 65534, Flask(__name__)


@app.route('/api/v1/buyer/cart', methods=['GET'])
def display_cart():
    buyer_id = request.args.get('buyer_id')
    if not buyer_id:
        string_util.error['error_message'] = string_util.missing_request_parameters.format(request_parameters='buyer id')
        return Util.get_response_object(string_util.error, 401)
    items_list = services.display(buyer_id=buyer_id)
    return Util.get_response_object(items_list, 200)


@app.route('/api/v1/buyer/items/search', methods=['POST'])
def search_items():
    items_list = services.search(request.get_json(force=True))
    return Util.get_response_object(items_list, 200)


@app.route('/api/v1/buyer/cart/items', methods=['POST'])
def add_items_to_cart():
    payload = request.get_json(force=True)
    response = services.add_item_to_cart(data=payload)
    if response is not None:
        string_util.error['error_message'] = response
        return Util.get_response_object(string_util.error, 401)
    else:
        return Util.get_response_object(response=None, status_code=200)


@app.route('/api/v1/buyer/cart/item', methods=['PUT', 'UPDATE'])
def remove_item_from_cart():
    payload = request.get_json(force=True)
    response = services.remove_item_from_cart(data=payload)
    if response is not None:
        string_util.error['error_message'] = response
        return Util.get_response_object(string_util.error, 401)
    else:
        return Util.get_response_object(response=None, status_code=200)


@app.route('/api/v1/buyer/cart', methods=['DELETE'])
def clear_cart():
    buyer_id = request.args.get('buyer_id')
    if not buyer_id:
        string_util.error['error_message'] = string_util.missing_request_parameters.format(request_parameters='buyer id')
        return Util.get_response_object(string_util.error, 401)
    response = services.delete()
    if response is not None:
        string_util.error['error_message'] = response
        return Util.get_response_object(string_util.error, 401)
    else:
        return Util.get_response_object(response=None, status_code=200)


@app.route('/api/v1/buyer/account/create', methods=['POST'])
def create_account():
    payload = request.get_json(force=True)
    response = services.create_buyer_account(data=payload)
    if response is not None:
        string_util.error['error_message'] = response
        return Util.get_response_object(string_util.error, 401)
    else:
        return Util.get_response_object(response=None, status_code=200)


@app.route('/api/v1/buyer/account/login', methods=['POST'])
def login():
    payload = request.get_json(force=True)
    response = services.login_buyer_account(data=payload)
    if 'Error' in response:
        string_util.error['error_message'] = response
        return Util.get_response_object(string_util.error, 401)
    else:
        return Util.get_response_object(response=response, status_code=200)


@app.route('/api/v1/buyer/account/logout', methods=['GET'])
def logout():
    return Util.get_response_object(response=None, status_code=200)


@app.route('/api/v1/buyer/purchase', methods=['POST'])
def make_purchase():
    payload = request.get_json(force=True)
    response = services.make_purchase(data=payload)
    if response is not None:
        string_util.error['error_message'] = response
        return Util.get_response_object(string_util.error, 401)
    else:
        return Util.get_response_object(response=None, status_code=200)


@app.route('/api/v1/buyer/feedback', methods=['POST'])
def feedback():
    payload = request.get_json(force=True)
    response = services.submit_feedback(data=payload)
    if response is not None:
        string_util.error['error_message'] = response
        return Util.get_response_object(string_util.error, 401)
    else:
        return Util.get_response_object(response=None, status_code=200)


app.run(host, port)
