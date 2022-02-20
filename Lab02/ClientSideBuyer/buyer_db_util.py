# Login Account Functionality
create_account = "INSERT INTO buyers(name, user_name, password) VALUES({name}, {user_name}, {password})"
login_account = "SELECT buyer_id FROM buyers WHERE user_name={user_name} AND password={password}"

# Cart Functionality
search_items = "SELECT * FROM items WHERE category={category} AND keyword in ({keywords}) AND buyer_id={buyer_id}"
add_items_to_cart = "INSERT INTO cart(item_id, buyer_id, quantity) VALUES({item_id}, {buyer_id}, {quantity})"
remove_item_from_cart = "UPDATE cart SET quantity={quantity} WHERE item_id={item_id} AND buyer_id={buyer_id}"
delete_item_from_cart = "DELETE FROM cart WHERE item_id={item_id} AND buyer_id={buyer_id}"
delete_cart = "DELETE FROM cart where buyer_id={buyer_id}"
display_cart = "SELECT * FROM cart where buyer_id={buyer_id}"

# Get Seller Rating
search_seller_ids = "SELECT DISTINCT(sellers.seller_id) FROM history JOIN items ON history.item_id=items.item_id " \
               "JOIN sellers ON items.seller_id=sellers.seller_id " \
               "WHERE history.sold=1 and history.buyer_id={buyer_id}"
get_seller_ratings = "SELECT name, up_votes, down_votes, item_sold FROM seller WHERE seller_id IN ({seller_ids})"

# Get Buyer History
get_buyer_history = "SELECT * FROM history where buyer_id={buyer_id}"

# Submit Feedback
add_history = "INSERT INTO history(buyer_id, item_id, up_vote, down_vote, sold) VALUES({buyer_id}," \
                 " {item_id}, {up_vote}, {down_vote}, {sold})"
update_up_votes = "UPDATE sellers SET up_votes = up_votes + 1, sold = sold + 1 where seller_id = (" \
                  "SELECT seller_id FROM items WHERE item_id = {item_id})"
update_down_votes = "UPDATE sellers SET down_votes = down_votes + 1, sold = sold + 1 where seller_id = (" \
                  "SELECT seller_id FROM items WHERE item_id = {item_id})"
