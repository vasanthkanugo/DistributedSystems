import requests

# response = requests.post("http://127.0.0.1:9001/api/v1/seller/account/create",json={
#     'name': 'vasanth',
#     'user_name': 'vasanth.kanugo',
#     'password': 'password'
# })
# print(response.status_code, response.json())

# response = requests.post("http://127.0.0.1:9001/api/v1/seller/account/login",json={
#     'name': 'vasanth',
#     'user_name': 'vasanth.kanugo',
#     'password': 'password'
# })
# print(response.status_code, response.json())
# seller_id = response.json()['seller_id']
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
#
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
# response = requests.get(f"http://127.0.0.1:9001/api/v1/seller/items?seller_id={seller_id}")
# items = response.json()
# print("GET QUANTITY UPDATE",response.status_code, items)

# response = requests.delete(f"http://127.0.0.1:9001/api/v1/seller/items?seller_id={seller_id}&item_id={items['items'][0]['item_id']}")
# print("DELETE ITEM", response.status_code)
#
# response = requests.get(f"http://127.0.0.1:9001/api/v1/seller/items?seller_id={seller_id}")
# items = response.json()
# print("GET AFTER DELETE", response.status_code, response.json())
#
# response = requests.put("http://127.0.0.1:9001/api/v1/seller/items", json={
#     'item_id': items['items'][0]['item_id'],
#     'sale_price': items['items'][0]['sale_price'] + 1000,
#     'seller_id': items['items'][0]['seller_id']
# })
# print("UPDATE SALE PRICE",response.status_code)
#
# response = requests.get(f"http://127.0.0.1:9001/api/v1/seller/items?seller_id={seller_id}")
# items = response.json()
# print("GET AFTER UPDATE SALE PRICE", response.status_code, response.json())
#
# response = requests.get(f"http://127.0.0.1:9001/api/v1/seller/items/ratings?seller_id={seller_id}")
# items = response.json()
# print("GET SELLER RATINGS", response.status_code, items)

# response = requests.post(f"http://127.0.0.1:65534/api/v1/buyer/account/create", json={
#     'name': 'vasanth',
#     'user_name': 'vasanth.kanugo',
#     'password': 'password'
# })
# print("CREATE ACCOUNT", response.status_code, response.json())

response = requests.post("http://127.0.0.1:65534/api/v1/buyer/account/login",json={
    'name': 'vasanth',
    'user_name': 'vasanth.kanugo',
    'password': 'password'
})
print("LOGIN STATUS",response.status_code, response.json())
buyer_id = response.json()['buyer_id']
print(f"buyer_id: {buyer_id} ")


# response = requests.post("http://127.0.0.1:65534/api/v1/buyer/items/search", json={
#     'item_category': 'Book',
#     'keywords':['Books', 'Novel']
# })
# print("ITEM SEARCH STATUS",response.status_code, response.json())

# response = requests.get("http://127.0.0.1:65534/api/v1/buyer/cart?buyer_id=2")
# print("GET STATUS",response.status_code, response.json())
#
# response = requests.post("http://127.0.0.1:65534/api/v1/buyer/cart/items",json={
#     'buyer_id': 2,
#     'items':[{
#         'item_id': 4,
#         'quantity': 5
#         },
#         {
#         'item_id': 6,
#         'quantity': 5
#         }
#     ]
# })
#
# print("ADD ITEMS TO CART STATUS",response.status_code)

# response = requests.get("http://127.0.0.1:65534/api/v1/buyer/cart?buyer_id=2")
# print("GET CART ITEMS",response.status_code, response.json())
#
# response = requests.put("http://127.0.0.1:65534/api/v1/buyer/cart/item",json={
#     'item_id': 6,
#     'quantity': 0,
#     'buyer_id': 2
# })
# print("UPDATE CART ITEMS",response.status_code)
#
# response = requests.get("http://127.0.0.1:65534/api/v1/buyer/cart?buyer_id=2")
# print("GET CART ITEMS",response.status_code, response.json())
#
# response = requests.put("http://127.0.0.1:65534/api/v1/buyer/cart/item",json={
#     'item_id': 4,
#     'quantity': 2,
#     'buyer_id': 2
# })
# print("UPDATE CART ITEMS",response.status_code)
# response = requests.get("http://127.0.0.1:65534/api/v1/buyer/cart?buyer_id=2")
# print("GET CART ITEMS",response.status_code, response.json())
#
# response = requests.delete("http://127.0.0.1:65534/api/v1/buyer/cart?buyer_id=2")
# print("DELETE CART ITEMS", response.status_code)

# response = requests.get("http://127.0.0.1:65534/api/v1/buyer/cart?buyer_id=2")
# print("GET CART ITEMS",response.status_code, response.json())
#
# response = requests.get("http://127.0.0.1:65534/api/v1/buyer/history?buyer_id=2")
# print("GET BUYER HISTORY ITEMS",response.status_code, response.json())
#
# response = requests.get("http://127.0.0.1:65534/api/v1/seller/rating?buyer_id=2")
# print("GET SELLER RATINGS ITEMS",response.status_code)
#
# response = requests.post("http://127.0.0.1:65534/api/v1/buyer/feedback", json={
#     'buyer_id': 2,
#     'sold': True,
#     'feedbacks': [{
#         'item_id': 6,
#         'thumbs_up': True
#     },{
#             'item_id': 4,
#             'thumbs_up': False
#     }
#     ]
# })
# print("POST FEEDBACK ",response.status_code)
#
# response = requests.get("http://127.0.0.1:65534/api/v1/buyer/history?buyer_id=2")
# print("GET BUYER HISTORY ITEMS",response.status_code, response.json())

# response = requests.get("http://127.0.0.1:65534/api/v1/seller/ratings?buyer_id=2")
# print("GET SELLER RATINGS ITEMS",response.status_code, response.json())


#Look into feedback and search functionalities