from pymongo import MongoClient
import os
from dotenv import load_dotenv, find_dotenv


class Api:
    def __init__(self):
        self.connector()

    # connect to mongodb
    def connector(self):
        load_dotenv(find_dotenv())
        host = os.getenv("171.226.105.157/32")
        username = os.getenv("tranvuduyenan714")
        password = os.getenv("qazwsxedc")
        database = os.getenv("Group2")
        self.client = MongoClient(host, username=username, password=password)
        self.db = self.client.get_database(database)
        self.users_collection = self.db['user']
        self.warehouse_collection = self.db['warehouse']
        self.invoices_collection = self.db['invoices']

    def get_all_warehouse_data(self):
        warehouse = self.warehouse_collection.find()
        warehouse_data = []
        for item in warehouse:
            warehouse_data.append(item)
        return warehouse_data

    def get_all_invoices_data(self):
        invoices = self.invoices_collection.find()
        invoices_data = []
        for invoice in invoices:
            for item in invoice['Cart']:
                sub_invoice_data = {}
                sub_invoice_data["Invoice_ID"] = invoice["Invoice_ID"]
                sub_invoice_data["Invoice_Date"] = invoice["Invoice_Date"]
                sub_invoice_data["Total"] = invoice["Total"]
                # append item to sub_invoice_data
                sub_invoice_data["Film_ID"] = item["Film_ID"]
                sub_invoice_data["Film"] = item["Film"]
                sub_invoice_data["Quantity"] = item["Quantity"]
                sub_invoice_data["Price"] = item["Price"]
                sub_invoice_data["Genre"] = item["Genre"]
                invoices_data.append(sub_invoice_data)
        return invoices_data

    # get all description data in warehouse
    def get_all_description_data(self):
        warehouse = self.warehouse_collection.find()
        description_data = []
        for item in warehouse:
            description_data.append(item["Genre"])
        return description_data

    def get_all_users_data(self):
        users = self.users_collection.find()
        users_data = []
        for user in users:
            users_data.append(user)
        return users_data

    def get_last_prod_id(self):
        warehouse = self.warehouse_collection.find()
        # get last product id in warehouse
        last_prod_id = 0
        for item in warehouse:
            if int(item["Film_ID"][1:]) > last_prod_id:
                last_prod_id = int(item["Film_ID"][1:])
        return str(1000 + last_prod_id + 1).replace("1", "P", 1)
