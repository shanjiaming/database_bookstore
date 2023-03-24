import uuid
import json
import logging
from be.model import error
from be.model import db_conn
from pymongo import MongoClient
import pymongo

class Buyer(db_conn.DBConn):
    def __init__(self):
        super().__init__()

    def new_order(self, user_id: str, store_id: str, id_and_count: [(str, int)]) -> (int, str, str):
        order_id = ""
        try:
            if not self.user_id_exist(user_id):
                return error.error_non_exist_user_id(user_id) + (order_id,)
            if not self.store_id_exist(store_id):
                return error.error_non_exist_store_id(store_id) + (order_id,)
            uid = "{}_{}_{}".format(user_id, store_id, str(uuid.uuid1()))

            for book_id, count in id_and_count:
                book = self.store_col.find_one({"store_id": store_id, "book_id": book_id})
                if book is None:
                    return error.error_non_exist_book_id(book_id) + (order_id,)
                stock_level = book["stock_level"]
                book_info = json.loads(book["book_info"])
                price = book_info["price"]

                if stock_level < count:
                    return error.error_stock_level_low(book_id) + (order_id,)

                result = self.store_col.update_one(
                    {"store_id": store_id, "book_id": book_id, "stock_level": {"$gte": count}},
                    {"$inc": {"stock_level": -count}})
                if result.modified_count == 0:
                    return error.error_stock_level_low(book_id) + (order_id,)

                self.new_order_detail_col.insert_one({
                    "order_id": uid,
                    "book_id": book_id,
                    "count": count,
                    "price": price
                })

            self.new_order_col.insert_one({
                "order_id": uid,
                "store_id": store_id,
                "user_id": user_id
            })
            order_id = uid
        except Exception as e:
            logging.info("{}".format(str(e)))
            return 530, "{}".format(str(e)), ""

        return 200, "ok", order_id

    def payment(self, user_id: str, password: str, order_id: str) -> (int, str):
        try:
            # Find the order and extract the necessary information
            order = self.db.new_order.find_one({'order_id': order_id},
                                               {'_id': 0, 'order_id': 1, 'user_id': 1, 'store_id': 1})
            if order is None:
                return error.error_invalid_order_id(order_id)

            order_id = order['order_id']
            buyer_id = order['user_id']
            store_id = order['store_id']

            if buyer_id != user_id:
                return error.error_authorization_fail()

            # Check if the user exists and has enough balance to make the payment
            user = self.db.user.find_one({'user_id': buyer_id}, {'_id': 0, 'balance': 1, 'password': 1})
            if user is None:
                return error.error_non_exist_user_id(buyer_id)

            balance = user['balance']
            if password != user['password']:
                return error.error_authorization_fail()

            # Check if the store exists
            store = self.db.user_store.find_one({'store_id': store_id}, {'_id': 0, 'user_id': 1})
            if store is None:
                return error.error_non_exist_store_id(store_id)

            seller_id = store['user_id']

            if not self.user_id_exist(seller_id):
                return error.error_non_exist_user_id(seller_id)

            # Calculate the total price of the order
            total_price = 0
            order_details = self.db.new_order_detail.find({'order_id': order_id}, {'_id': 0, 'count': 1, 'price': 1})
            for detail in order_details:
                count = detail['count']
                price = detail['price']
                total_price += price * count

            # Check if the buyer has enough balance to make the payment
            if balance < total_price:
                return error.error_not_sufficient_funds(order_id)

            # Update the buyer's balance
            result = self.db.user.update_one({'user_id': buyer_id, 'balance': {'$gte': total_price}},
                                             {'$inc': {'balance': -total_price}})
            if result.modified_count == 0:
                return error.error_not_sufficient_funds(order_id)

            # Update the seller's balance
            result = self.db.user.update_one({'user_id': seller_id}, {'$inc': {'balance': total_price}})
            if result.modified_count == 0:
                return error.error_non_exist_user_id(seller_id)

            # Delete the order and its details
            result = self.db.new_order.delete_one({'order_id': order_id})
            if result.deleted_count == 0:
                return error.error_invalid_order_id(order_id)

            result = self.db.new_order_detail.delete_many({'order_id': order_id})
            if result.deleted_count == 0:
                return error.error_invalid_order_id(order_id)

        except pymongo.errors.PyMongoError as e:
            return 528, "{}".format(str(e))

        except BaseException as e:
            return 530, "{}".format(str(e))

        return 200, "ok"

    def add_funds(self, user_id, password, add_value) -> (int, str):
        try:
            user = self.db.user.find_one({"user_id": user_id})
            if user is None:
                return error.error_authorization_fail()

            if user["password"] != password:
                return error.error_authorization_fail()

            result = self.db.user.update_one({"user_id": user_id}, {"$inc": {"balance": add_value}})
            if result.modified_count == 0:
                return error.error_non_exist_user_id(user_id)

        except pymongo.errors.PyMongoError as e:
            return 528, str(e)
        except BaseException as e:
            return 530, str(e)

        return 200, "ok"

