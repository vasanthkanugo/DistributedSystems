# Login Account Functionality
create_account = "INSERT INTO sellers(name, user_name, password) VALUES({name}, {user_name}, {password})"
login_account = "SELECT seller_id FROM sellers WHERE user_name={user_name} AND password={password}"

# Functionality
add_items_for_sale = "INSERT INTO items(name, category, keywords, condition, sale_price, quantity) VALUES({name}, {category}, {keywords}, {condition}, {sale_price}, {quantity}, {})"
remove_item_from_sale = "UPDATE quantity={quantity} FROM items WHERE item_id={item_id}"
update_sale_price_of_item ="UPDATE sale_price={sale_price} FROM items WHERE item_id={item_id}"
display_items = "SELECT * FROM items where seller_id={seller_id}"

# Get Seller Rating
get_seller_ratings = "SELECT name, up_votes, down_votes, item_sold FROM sellers WHERE seller_id IN ({seller_ids})"

# Get Buyer History
get_buyer_history = "SELECT * FROM history where buyer_id={buyer_id}"
