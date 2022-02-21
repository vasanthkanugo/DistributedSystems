# Login Account Functionality
create_account = "INSERT INTO sellers(name, user_name, password) VALUES(\'{name}\', \'{user_name}\', \'{password}\')"
login_account = "SELECT seller_id FROM sellers WHERE user_name=\'{user_name}\' AND password=\'{password}\' "

# Seller Functionality
add_items_for_sale = "INSERT INTO items(name, category, keywords, condition, sale_price, quantity, seller_id)" \
                     " VALUES(\'{name}\', \'{category}\', \'{keywords}\', \'{condition}\', \'{sale_price}\', \'{quantity}\', \'{seller_id}\')"
remove_item_from_sale = "UPDATE items SET quantity={quantity} WHERE item_id={item_id} AND seller_id={seller_id} "
delete_item_from_sale = "DELETE FROM items WHERE item_id={item_id} AND seller_id={seller_id} "
update_sale_price_of_item ="UPDATE items SET sale_price={sale_price} WHERE item_id={item_id} AND seller_id={seller_id}"
display_items = "SELECT * FROM items where seller_id={seller_id} "

# Get Seller Rating
get_seller_ratings = "SELECT name, up_votes, down_votes, items_sold FROM sellers WHERE seller_id={seller_id} "

