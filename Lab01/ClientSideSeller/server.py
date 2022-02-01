import socket
import Util
import string_util

# Get list of all items in the database
def get(data):
    return []


# Add a new item to the database
def post(data):
    return 'Hello'


# Update the item list
def put_or_update(data):
    return None


# Delete an item from the item list
def delete(data):
    return None


def start_server(port, host):
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.bind((host, port))
        s.listen()
        conn, addr = s.accept()  # accept connection
        while conn:
            print('Connected by', addr)
            while True:
                data = conn.recv(1024)
                if not data:
                    break  # closing condition with empty bytes in data
                payload = Util.bytes_to_json(data)

                if payload is None or 'Header' not in payload:  # if header is missing
                    string_util.error['error_message'] = string_util.missing_header_error
                    response_message = Util.dict_to_json(string_util.error)
                    conn.sendall(Util.dict_to_bytes(response_message))
                else:  # if header is present
                    if payload('Header') == 'GET':
                        items_list = get(data=payload)
                        conn.sendall(Util.dict_to_bytes({'items': items_list}))
                    elif payload('Header') == 'POST':
                        response = post(data=payload)
                        if response is not None:
                            string_util.error['error_message'] = response
                            response_message = Util.dict_to_json(string_util.error)
                            conn.sendall(Util.dict_to_bytes(response_message))
                        else:
                            conn.sendall(Util.dict_to_bytes(string_util.ok))
                    elif payload('Header') == 'PUT' or payload('Header') == 'UPDATE':
                        response = put_or_update(data=payload)
                        if response is not None:
                            string_util.error['error_message'] = response
                            response_message = Util.dict_to_json(string_util.error)
                            conn.sendall(Util.dict_to_bytes(response_message))
                        else:
                            conn.sendall(Util.dict_to_bytes(string_util.ok))
                    elif payload('Header') == 'DELETE':
                        response = delete(data=payload)
                        if response is not None:
                            string_util.error['error_message'] = response
                            response_message = Util.dict_to_json(string_util.error)
                            conn.sendall(Util.dict_to_bytes(response_message))
                        else:
                            conn.sendall(Util.dict_to_bytes(string_util.ok))
                    else:
                        string_util.error['error_message'] = string_util.missing_header_error
                        response_message = Util.dict_to_json(string_util.error)
                        conn.sendall(Util.dict_to_bytes(response_message))
            conn, addr = s.accept()  # open connection for new set of data


if __name__ == '__main__':
    host = '127.0.0.1'
    port = 65345
    start_server(port, host)  # starting server
