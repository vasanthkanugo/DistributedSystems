post_request = {
    'Header': 'POST',
    'Body': [
             {
                'item_name': 'Books',
                'item_id': '6675578',
                'quantity': '23',
                'item_category': 'Educational'
             },
                {
                    'item_name': 'Laptops',
                    'item_id': '5578',
                    'quantity': '50',
                    'item_category': 'Electronics'
                },
                {
                    'item_name': 'Apples',
                    'item_id': '68',
                    'quantity': '80',
                    'item_category': 'Food'
                }
    ]
}

get_request = {
    'Header': 'GET'
}

put_request = {
    'Header': 'PUT',
    'Body':
        {
            'item_id': '68',
            'quantity': 4
        }
}

delete_request = {
    'Header': 'DELETE'
}


operations = [post_request, get_request, put_request, get_request,  delete_request, get_request]