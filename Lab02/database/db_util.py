import pickle
import os
__location__ = os.path.realpath(
    os.path.join(os.getcwd(), os.path.dirname(__file__)))

cart_db = os.path.join(__location__, 'cart.db')
item_db = os.path.join(__location__, 'item.db')

def read_db(db_name):
    try:
        db_file = open(db_name, 'rb')
        print(db_file.name)
        db_entries = pickle.load(db_file)
        if db_file is not None:
            db_file.close()
    except:
        print("E: error loading from db")
        return "E: error loading from db"
    return db_entries


def write_db(db_name, entries):
    db_entries = dict(read_db(db_name=db_name))
    if db_entries is None:
        db_entries = dict()
    if len(entries) != 0:
        db_entries.update(entries)
    else:
        db_entries = dict()
    del_key = None
    for key, value in db_entries.items():
        if value is None:
            del_key = key
    if not del_key is None:
        del db_entries[del_key]
    try:
        db_file = open(db_name, 'wb')
        pickle.dump(db_entries, db_file)
        db_file.close()
    except:
        print('E: error writing to db')
        return 'E: error writing to db'
    return None


