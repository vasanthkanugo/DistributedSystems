import services
from util import Util, string_util
from server import run_server


def handle_connection(payload, connection):
    if payload is None or 'Header' not in payload:  # if header is missing
        string_util.error['error_message'] = string_util.missing_header_error
        response_message = Util.dict_to_json(string_util.error)
        connection.sendall(Util.dict_to_bytes(response_message))
    else:  # if header is present
        if payload['Header'] == 'GET':
            items_list = services.get()
            connection.sendall(Util.dict_to_bytes({'items': items_list}))
        elif payload['Header'] == 'POST':
            response = services.post(data=payload)
            if response is not None:
                string_util.error['error_message'] = response
                response_message = Util.dict_to_json(string_util.error)
                connection.sendall(Util.dict_to_bytes(response_message))
            else:
                connection.sendall(Util.dict_to_bytes(string_util.ok))
        elif payload['Header'] == 'PUT' or payload['Header'] == 'UPDATE':
            response = services.put_or_update(data=payload)
            if response is not None:
                string_util.error['error_message'] = response
                response_message = Util.dict_to_json(string_util.error)
                connection.sendall(Util.dict_to_bytes(response_message))
            else:
                connection.sendall(Util.dict_to_bytes(string_util.ok))
        elif payload['Header'] == 'DELETE':
            response = services.delete(payload)
            if response is not None:
                string_util.error['error_message'] = response
                response_message = Util.dict_to_json(string_util.error)
                connection.sendall(Util.dict_to_bytes(response_message))
            else:
                connection.sendall(Util.dict_to_bytes(string_util.ok))
        else:
            string_util.error['error_message'] = string_util.missing_header_error
            response_message = Util.dict_to_json(string_util.error)
            connection.sendall(Util.dict_to_bytes(response_message))
    return True


if __name__ == '__main__':
    host = '127.0.0.1'
    port = 65345
    run_server.start_server(host, port, handle_connection)  # starting server
