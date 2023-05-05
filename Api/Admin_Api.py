import json
import Api.Main_Api as main_api


class Admin_Api(main_api.Api):

    def __init__(self):
        super().__init__()
        self.connector()

    def add_new_item(self, json_data):
        # get product id in json_data
        product_id = json_data["Product_id"]
        # get product quantity in json_data
        product = self.warehouse_collection.find_one(
            {'Product_id': product_id})
        if product == None:
            # check Product_name of json_data is in collection
            S = 0
            for key, value in json_data.items():
                if self.warehouse_collection.find_one({key: value}) != None:
                    S += 1
                else:
                    continue
            if S == 6:
                # erorr 1 : product id is not in collection but all informations are in collection
                return -1
            # update json_data to database
            self.warehouse_collection.insert_one(json_data)
            return 0  # success
        else:
            return -2  # error 2: product is already exist

    def update_items(self, json_data, product_id):
        # get product quantity in json_data
        product = self.warehouse_collection.find_one(
            {'Product_id': product_id})
        _id = product['_id']  # get _id of product
        S = 0
        for key, value in json_data.items():
            if self.warehouse_collection.find_one({key: value}) != None:
                S += 1
            else:
                continue
        if S == 6:
            return -2  # erorr 2 : product id is not in collection but all informations are in collection
        else:
            # update json_data to _id in  database
            self.warehouse_collection.update_one(
                {'_id': _id}, {'$set': json_data})
            return 0  # success

    def remove_items(self, product_id):
        # get product quantity in json_data
        product = self.warehouse_collection.find_one(
            {'Product_id': product_id})
        _id = product['_id']  # get _id of product
        self.warehouse_collection.delete_one({'_id': _id})
        return 0  # success

    def update_user(self, json_data):
        username = json_data["username"]
        # get user in json_data
        user = self.users_collection.find_one({'username': username})
        _id = user['_id']  # get _id of user
        # update json_data to _id in  database
        self.users_collection.update_one({'_id': _id}, {'$set': json_data})
        return 0  # success

    def remove_user(self, data):
        username = data[0]
        # get user in json_data
        user = self.users_collection.find_one({'username': username})
        _id = user['_id']  # get _id of user
        self.users_collection.delete_one({'_id': _id})
        return 0  # success

    def add_new_user(self, json_data):
        # get user in json_data
        user = self.users_collection.find_one({'username': json_data["username"]})
        if user == None:
            # add to database
            self.users_collection.insert_one(json_data)
            return 0  # success
        else:
            return -1  # error 1: user is already exist

    # get all warehouse data by function get_all_warehouse_data
    # get all invoice data by function get_all_invoice_data