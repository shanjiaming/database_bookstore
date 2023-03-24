from pymongo import MongoClient
from bson.objectid import ObjectId
from be.model import store


class DBConn:
    def __init__(self):
        self.client = store.get_db_conn()
        self.db = self.client["bookstore"]
        self.user_col = self.db['user']
        self.store_col = self.db['store']
        self.user_store_col = self.db['user_store']
        self.new_order_col = self.db["new_order"]
        self.new_order_detail_col = self.db["new_order_detail"]

    def user_id_exist(self, user_id):
        cursor = self.user_col.find_one({"user_id": user_id})
        if cursor is None:
            return False
        else:
            return True

    def book_id_exist(self, store_id, book_id):
        cursor = self.store_col.find_one({"store_id": store_id, "book_id": book_id})
        if cursor is None:
            return False
        else:
            return True

    def store_id_exist(self, store_id):
        cursor = self.user_store_col.find_one({"store_id": store_id})
        if cursor is None:
            return False
        else:
            return True
