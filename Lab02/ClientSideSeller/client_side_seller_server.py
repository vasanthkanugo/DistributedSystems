from util import Util, string_util
import services
from flask import Flask, request

host, port, app = '127.0.0.1', 655346, Flask(__name__)


@app.route('/api/v1/seller/items', methods=['GET'])
def enlist():
    items_list = services.get()
    return Util.get_response_object(items_list, 200)

@app.route('/api/v1/seller/items/add', methods=['POST'])
def add():
    payload = request.get_json(force=True)
    response = services.post(data=payload)
    if response is not None:
        string_util.error['error_message'] = response
        return Util.get_response_object(string_util.error, 401)
    else:
        return Util.get_response_object(response=None, status_code=200)

@app.route('/api/v1/seller/items/update', methods=['PUT', 'UPDATE'])
def update():
    payload = request.get_json(force=True)
    response = services.put_or_update(data=payload)
    if response is not None:
        string_util.error['error_message'] = response
        return Util.get_response_object(string_util.error, 401)
    else:
        return Util.get_response_object(response=None, status_code=200)


@app.route('/api/v1/seller/items/delete', methods=['DELETE'])
def delete():
    response = services.delete()
    if response is not None:
        string_util.error['error_message'] = response
        return Util.get_response_object(string_util.error, 401)
    else:
        return Util.get_response_object(response=None, status_code=200)


@app.route('/api/v1/seller/account/create', methods=['POST'])
def create_account():
    return None


@app.route('/api/v1/seller/account/login', methods=['POST'])
def login():
    return None


@app.route('/api/v1/seller/account/logout', methods=['GET'])
def logout():
    return None


app.run(host, port)
