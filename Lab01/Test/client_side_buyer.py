post_request = {
    'Header': 'POST',
    'Body': {
        'items': [
            {
                'item_id': 'item_1',
                'quantity': 3
            },
            {
                'item_id': 'item_2',
                'quantity': 2
            },
            {
                'item_id': 'item_3',
                'quantity': 4
            },
            {
                'item_id': 'item_5',
                'quantity': 10
            }
        ]
    }
}

get_request = {
    'Header': 'GET'
}

put_request = {
    'Header': 'PUT',
    'Body':
        {
            'item_id': 'item_1',
            'quantity': 4
        }
}

delete_request = {
    'Header': 'DELETE'
}

search_request = {
    'Header': 'GET',
    'Body': 'item'
}


operations = [post_request, get_request, put_request, get_request,  delete_request, get_request,  search_request]