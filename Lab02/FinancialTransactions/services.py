from spyne import Application, rpc, ServiceBase, Iterable, Integer, Unicode, Byte
from spyne.protocol.soap import Soap11
from spyne.server.wsgi import WsgiApplication
from util import Util, string_util
from datetime import datetime as dt

'''
Format of the body
{
    'client_id' : client_id,
    'credit_card':{
        'name' : 'name on credit card',
        'number': 'number on the credit card',
        'expiration_date' :'expiration_date with expected format '%M-%Y''
    }, 
    'price': price
}
'''


class HelloWorldService(ServiceBase):
    @rpc(Unicode, _returns=Unicode)
    def buy(ctx, body):
        json_body = Util.json_to_dic(bytes(body, encoding='utf-8'))
        if 'client_id' not in json_body:
            string_util.error['error_message'] = string_util.missing_request_parameters.format(request_parameters='client_id')
            return Util.dict_to_bytes(string_util.error)
        elif 'credit_card' not in json_body:
            string_util.error['error_message'] = string_util.missing_request_parameters.format(
                request_parameters='credit_card')
            return Util.dict_to_bytes(string_util.error)
        elif 'name' not in json_body['credit_card'] or 'number' not in json_body['credit_card'] or 'expiration_date' not in json_body['credit_card']:
            string_util.error['error_message'] = string_util.missing_request_parameters.format(
                request_parameters='credit card details are missing')
            return Util.dict_to_bytes(string_util.error)
        elif 'price' not in json_body:
            string_util.error['error_message'] = string_util.missing_request_parameters.format(
                request_parameters='Invalid price for transaction')
            return Util.dict_to_bytes(string_util.error)
        else:
            date = None
            try:
                date = dt.strptime(json_body['credit_card']['expiration_date'], '%M-%Y')
            except:
                string_util.error['error_message'] = string_util.missing_request_parameters.format(
                    request_parameters='Incorrect date format')
                return Util.dict_to_bytes(string_util.error)
            if date < dt.now():
                string_util.error['error_message'] = string_util.missing_request_parameters.format(
                    request_parameters='Credit Card Expired')
                return Util.dict_to_bytes(string_util.error)
        return Util.dict_to_bytes(string_util.ok)


application = Application([HelloWorldService], 'spyne.examples.hello.soap',
                          in_protocol=Soap11(validator='lxml'),
                          out_protocol=Soap11())

wsgi_application = WsgiApplication(application)

if __name__ == '__main__':
    import logging

    from wsgiref.simple_server import make_server

    logging.basicConfig(level=logging.DEBUG)
    logging.getLogger('spyne.protocol.xml').setLevel(logging.DEBUG)

    logging.info("listening to http://127.0.0.1:8000")
    logging.info("wsdl is at: http://localhost:8000/?wsdl")

    server = make_server('127.0.0.1', 8000, wsgi_application)
    server.serve_forever()
