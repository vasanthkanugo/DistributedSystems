import requests

# response = requests.post("http://127.0.0.1:9001/api/v1/seller/account/create",json={
#     'name': 'vasanth',
#     'user_name': 'vasanth.kanugo',
#     'password': 'password'
# })
# print(response.status_code, response.json())

response = requests.post("http://127.0.0.1:9001/api/v1/seller/account/login",json={
    'name': 'vasanth',
    'user_name': 'vasanth.kanugo',
    'password': 'password'
})
print(response.status_code, response.json())
seller_id = response.json()['seller_id']
# print(f"seller id: {seller_id} ")
#
# response = requests.post("http://127.0.0.1:9001/api/v1/seller/items", json={
#     'items':[
#         {
#             'name': "harry potter Novel",
#             'category': 'Book',
#             'keywords': ['Books', 'Book', 'Novel', 'Harry Potter'],
#             'condition': 'New',
#             'sale_price': 100,
#             'quantity': 4,
#             'seller_id': seller_id
#         },
#         {
#             'name': "Fifty shaded",
#             'category': 'Book',
#             'keywords': ['Books', 'Book', 'Novel'],
#             'condition': 'New',
#             'sale_price': 1000,
#             'quantity': 1,
#             'seller_id': seller_id
#         }
#     ]
# })
# print(response.status_code)

# response = requests.get(f"http://127.0.0.1:9001/api/v1/seller/items?seller_id={seller_id}")
# items = response.json()
# print("GET", response.status_code, items)
#
# response = requests.put("http://127.0.0.1:9001/api/v1/seller/items", json={
#     'item_id': items['items'][0]['item_id'],
#     'quantity': items['items'][0]['quantity'] + 100,
#     'seller_id': items['items'][0]['seller_id']
# })
# print("UDPATE QUANTITY",response.status_code)
#
response = requests.get(f"http://127.0.0.1:9001/api/v1/seller/items?seller_id={seller_id}")
items = response.json()
print("GET QUANTITY UPDATE",response.status_code, items)

response = requests.delete(f"http://127.0.0.1:9001/api/v1/seller/items?seller_id={seller_id}&item_id={items['items'][0]['item_id']}")
print("DELETE ITEM", response.status_code)

response = requests.get(f"http://127.0.0.1:9001/api/v1/seller/items?seller_id={seller_id}")
items = response.json()
print("GET AFTER DELETE", response.status_code, response.json())

response = requests.put("http://127.0.0.1:9001/api/v1/seller/items", json={
    'item_id': items['items'][0]['item_id'],
    'sale_price': items['items'][0]['sale_price'] + 1000,
    'seller_id': items['items'][0]['seller_id']
})
print("UPDATE SALE PRICE",response.status_code)

response = requests.get(f"http://127.0.0.1:9001/api/v1/seller/items?seller_id={seller_id}")
items = response.json()
print("GET AFTER UPDATE SALE PRICE", response.status_code, response.json())

