post_request ={
    'items':[{
            'item_name': 'Books',
            'item_id': '6675578',
            'quantity': '23',
            'item_category': 'Educational',
            'keywords': ['Education', 'Read', 'Study', 'Learn'],
            'condition': 'new',
            'sale_price': 1000

        },
        {
            'item_name': 'Laptops',
            'item_id': '5578',
            'quantity': '50',
            'item_category': 'Electronics',
            'keywords': ['Electronic', 'Apple', 'Dell', 'Android'],
            'condition': 'used',
            'sale_price': 100000
        },
        {
            'item_name': 'Apples',
            'item_id': '68',
            'quantity': '80',
            'item_category': 'Food',
            'keywords': ['Fruit', 'Red', 'Juice', 'Pie'],
            'condition': 'new',
            'sale_price': 10
        }]
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
    'Header': 'DELETE',
    'Body': {
        'item_id': '5578',
        'quantity': 0
    }
}

operations = [post_request, get_request, put_request, get_request, delete_request, get_request]
