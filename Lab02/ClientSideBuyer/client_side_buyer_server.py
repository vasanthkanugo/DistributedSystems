from util import Util, string_util
import services
from flask import Flask, request

host, port, app = '127.0.0.1', 65534, Flask(__name__)


@app.route('/api/v1/buyer/items', methods=['GET'])
def enlist():
    items_list = services.get()
    return Util.get_response_object(items_list, 200)


@app.route('/api/v1/buyer/items/search', methods=['POST'])
def search():
    items_list = services.search(request.get_json(force=True))
    return Util.get_response_object(items_list, 200)


@app.route('/api/v1/buyer/items', methods=['POST'])
def add():
    payload = request.get_json(force=True)
    response = services.post(data=payload)
    if response is not None:
        string_util.error['error_message'] = response
        return Util.get_response_object(string_util.error, 401)
    else:
        return Util.get_response_object(response=None, status_code=200)


@app.route('/api/v1/buyer/items', methods=['PUT', 'UPDATE'])
def update():
    payload = request.get_json(force=True)
    response = services.put_or_update(data=payload)
    if response is not None:
        string_util.error['error_message'] = response
        return Util.get_response_object(string_util.error, 401)
    else:
        return Util.get_response_object(response=None, status_code=200)


@app.route('/api/v1/buyer/items', methods=['DELETE'])
def delete():
    response = services.delete()
    if response is not None:
        string_util.error['error_message'] = response
        return Util.get_response_object(string_util.error, 401)
    else:
        return Util.get_response_object(response=None, status_code=200)


@app.route('/api/v1/buyer/account/create', methods=['POST'])
def create_account():
    return None


@app.route('/api/v1/buyer/account/login', methods=['POST'])
def login():
    return None


@app.route('/api/v1/buyer/account/logout', methods=['GET'])
def logout():
    return None


@app.route('/api/v1/buyer/purchase', methods=['POST'])
def make_purchase():
    payload = request.get_json(force=True)
    response = services.make_purchase(data=payload)
    if response is not None:
        string_util.error['error_message'] = response
        return Util.get_response_object(string_util.error, 401)
    else:
        return Util.get_response_object(response=None, status_code=200)

app.run(host, port)
