import pymongo
from bson import ObjectId
from be.model import error
from be.model import db_conn

class Seller(db_conn.DBConn):

    def __init__(self):
        super().__init__()

    def add_book(self, user_id: str, store_id: str, book_id: str, book_json_str: str, stock_level: int):
        try:
            if not self.user_id_exist(user_id):
                return error.error_non_exist_user_id(user_id)
            if not self.store_id_exist(store_id):
                return error.error_non_exist_store_id(store_id)
            if self.book_id_exist(store_id, book_id):
                return error.error_exist_book_id(book_id)

            self.store_col.insert_one({
                'store_id': store_id,
                'book_id': book_id,
                'book_info': book_json_str,
                'stock_level': stock_level
            })
        except pymongo.errors.PyMongoError as e:
            return 528, "{}".format(str(e))
        except BaseException as e:
            return 530, "{}".format(str(e))
        return 200, "ok"

    def add_stock_level(self, user_id: str, store_id: str, book_id: str, add_stock_level: int):
        try:
            if not self.user_id_exist(user_id):
                return error.error_non_exist_user_id(user_id)
            if not self.store_id_exist(store_id):
                return error.error_non_exist_store_id(store_id)
            if not self.book_id_exist(store_id, book_id):
                return error.error_non_exist_book_id(book_id)

            # Bug: no ObjectID
            # self.store_col.update_one(
            #     {'store_id': store_id, 'book_id': book_id},
            #     {'$inc': {'stock_level': add_stock_level}}
            # )
            objectID = self.store_col.find_one({'store_id': store_id, 'book_id': book_id})['_id']
            self.store_col.update_one(
                {'_id': ObjectId(objectID)},
                {'$inc': {'stock_level': add_stock_level}}
            )

        except BaseException as e:
            return 530, "{}".format(str(e))
        return 200, "ok"

    def create_store(self, user_id: str, store_id: str) -> (int, str):
        try:
            if not self.user_id_exist(user_id):
                return error.error_non_exist_user_id(user_id)
            if self.store_id_exist(store_id):
                return error.error_exist_store_id(store_id)
            store = {
                'store_id': store_id,
                'user_id': user_id
            }
            self.user_store_col.insert_one(store)
        except BaseException as e:
            return 530, "{}".format(str(e))
        return 200, "ok"

