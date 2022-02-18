from suds.client import Client
from util import Util
client = Client('http://localhost:8000/?wsdl', cache=None)
json = {
    'client_id': 123,
    'credit_card': {
        'name': 'Vasanth Kanugo',
        'number': '10987654321',
        'expiration_date': '12-2023'
    }
}
print(client.service.buy(Util.dict_to_json(json)))