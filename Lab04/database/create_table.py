import os
import sqlite3
from sqlite3 import Error

create_seller_table = "CREATE TABLE IF NOT EXISTS " \
                      "sellers(seller_id INTEGER PRIMARY KEY AUTOINCREMENT, " \
                      "name TEXT NOT NULL, " \
                      "up_votes INTEGER DEFAULT 0, " \
                      "down_votes INTEGER DEFAULT 0, " \
                      "items_sold INTEGER DEFAULT 0, " \
                      "user_name TEXT NOT NULL, " \
                      "password TEXT NOT NULL) "

create_buyer_table = "CREATE TABLE IF NOT EXISTS " \
                     "buyers(buyer_id INTEGER PRIMARY KEY AUTOINCREMENT," \
                     "name TEXT NOT NULL, " \
                     "items_purchased INTEGER DEFAULT 0," \
                     "user_name TEXT NOT NULL, " \
                     "password TEXT NOT NULL)"

create_item_table = "CREATE TABLE IF NOT EXISTS " \
                    "items(item_id INTEGER PRIMARY KEY AUTOINCREMENT," \
                    "name TEXT NOT NULL, " \
                    "category TEXT NOT NULL, " \
                    "keywords TEXT NOT NULL, " \
                    "condition TEXT NOT NULL, " \
                    "sale_price INTEGER NOT NULL, " \
                    "quantity INTEGER DEFAULT 0," \
                    "seller_id INTEGER, " \
                    "FOREIGN KEY(seller_id) REFERENCES sellers(seller_id)" \
                    "ON DELETE CASCADE ON UPDATE NO ACTION)"

create_cart_table = "CREATE TABLE IF NOT EXISTS " \
                    "cart(cart_id INTEGER PRIMARY KEY AUTOINCREMENT," \
                    "item_id INTEGER," \
                    "buyer_id INTEGER, " \
                    "quantity INTEGER NOT NULL," \
                    "FOREIGN KEY(item_id) REFERENCES items(item_id)" \
                    "ON DELETE CASCADE ON UPDATE NO ACTION, " \
                    "FOREIGN KEY(buyer_id) REFERENCES buyers(buyer_id)" \
                    "ON DELETE CASCADE ON UPDATE NO ACTION)"

create_history_table = "CREATE TABLE IF NOT EXISTS " \
                       "history(history_id INTEGER PRIMARY KEY AUTOINCREMENT, " \
                       "buyer_id INTEGER, " \
                       "item_id INTEGER, " \
                       "up_vote BOOLEAN DEFAULT False, " \
                       "down_vote BOOLEAN DEFAULT False," \
                       "sold BOOLEAN DEFAULT False, " \
                       "FOREIGN KEY(item_id) REFERENCES items(item_id)" \
                        "ON DELETE CASCADE ON UPDATE NO ACTION," \
                       "FOREIGN KEY(buyer_id) REFERENCES buyers(buyer_id)" \
                        "ON DELETE CASCADE ON UPDATE NO ACTION)"

def create_tables(db_file):
    conn = None
    try:
        conn = sqlite3.connect(db_file)
        print(sqlite3.version)
        cursor = conn.cursor()
        tables = [create_seller_table, create_buyer_table, create_item_table, create_cart_table, create_history_table]
        for table in tables:
            try:
                cursor.execute(table)
            except Error as e:
                print(f"Error creating table:{table} - E:{e.__str__()}")
                return f"Error creating table:{table} - E:{e.__str__()}"
    except Error as e:
        print(e)
        return e
    finally:
        if conn:
            conn.commit()
            conn.close()
    return None


if __name__ == '__main__':
    __location__ = os.path.realpath(
        os.path.join(os.getcwd(), os.path.dirname(__file__)))

    database = os.path.join(__location__, 'database.db')
    create_tables(database)
