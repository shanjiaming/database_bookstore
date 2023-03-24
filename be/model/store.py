import logging
import os
from pymongo import MongoClient


class Store:
    def __init__(self):
        db_path = 'mongodb://localhost:27017/'
        self.client = MongoClient(db_path)
        self.db = self.client["bookstore"]
        self.init_tables()

    def init_tables(self):
        try:
            user_col = self.db["user"]
            user_col.create_index("user_id", unique=True)
            user_col.create_index("token")

            user_store_col = self.db["user_store"]
            user_store_col.create_index([("user_id", 1), ("store_id", 1)], unique=True)

            store_col = self.db["store"]
            store_col.create_index([("store_id", 1), ("book_id", 1)], unique=True)

            new_order_col = self.db["new_order"]
            new_order_col.create_index("order_id", unique=True)

            new_order_detail_col = self.db["new_order_detail"]
            new_order_detail_col.create_index([("order_id", 1), ("book_id", 1)], unique=True)

        except Exception as e:
            logging.error(e)

    def get_db_conn(self):
        return self.client

database_instance: Store = None

def init_database():
    global database_instance
    database_instance = Store()

def get_db_conn():
    global database_instance
    return database_instance.get_db_conn()
