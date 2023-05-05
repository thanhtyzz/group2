import Api.Main_Api as main_api
import datetime


class User_Api(main_api.Api):
    total_cart = []
    temp = 0

    def __init__(self):
        super().__init__()
        self.connector()

    # get last Invoice_Id from invoice collection
    def get_last_invoice_id(self):
        try:
            self.cursor = self.invoices_collection.find().sort(
                [('Invoice_Id', -1)])
            self.last_invoice_id = self.cursor[0]['Invoice_Id']
            return self.last_invoice_id
        except:
            return "INV-000"

    def create_new_invoice_id(self):
        self.last_invoice_id = self.get_last_invoice_id()
        id = self.last_invoice_id.split('-')[-1]
        new_id = float(id) + 1
        self.new_invoice_id = 'INV-' + str(100 + int(new_id)).replace("1", "0", 1)

    def add_item_to_cart(self, product_name, quantity):
        data = self.warehouse_collection.find_one(
            {'Product_name': product_name})
        if data == None:
            return -1  # error 1: product is not exist
        else:
            product_id = data['Product_id']
            product_name = data['Product_name']
            product_price = data['Price']
            left_stock = data['Stock']
        try:
            quantity = float(quantity)
        except:
            return -3  # error 3: quantity is not a number

        if float(left_stock) < float(quantity):
            return -2  # error 2: not enough stock
        else:
            left_stock = float(left_stock) - float(quantity)
        # check product_id is in User_Api.total_cart
        if len(User_Api.total_cart) != 0:
            for i in range(len(User_Api.total_cart)):
                if User_Api.total_cart[i]['Product_id'] == product_id:
                    x = float(User_Api.total_cart[i]['Quantity']) + float(quantity)
                    if float(left_stock) < x:
                        return -2  # error 2: not enough stock
                    else:
                        User_Api.total_cart[i]['Quantity'] = x
                        User_Api.total_cart[i]['Price'] = float(User_Api.total_cart[i]['Price']) + float(
                            quantity) * float(product_price)
                        left_stock = float(left_stock) - float(quantity)
                        User_Api.temp = User_Api.total_cart[i]['Price']
                        return -4  # error 4: product already in cart

            self.cart = {}
            self.cart['Product_id'] = product_id
            self.cart['Product_name'] = product_name
            self.cart['Quantity'] = quantity
            self.cart['Price'] = float(product_price) * float(quantity)
            User_Api.total_cart.append(self.cart)

            return self.cart

        else:
            self.cart = {}
            self.cart['Product_id'] = product_id
            self.cart['Product_name'] = product_name
            self.cart['Quantity'] = quantity
            self.cart['Price'] = float(product_price) * float(quantity)

            # add cart to cart.json in Data folder
            User_Api.total_cart.append(self.cart)

            return self.cart

    # process
    def process_cart(self):
        self.create_new_invoice_id()
        sum = 0
        if len(User_Api.total_cart) != 0:
            for i in range(len(User_Api.total_cart)):
                sum = sum + User_Api.total_cart[i]['Price']

            dict = {'Invoice_Id': self.new_invoice_id, 'InvoiceDate': datetime.datetime.now(
            ), 'Cart': User_Api.total_cart, 'TotalAmount': sum}
            self.invoices_collection.insert_one(dict)
            # update stock in warehouse collection
            for i in range(len(User_Api.total_cart)):
                self.cursor = self.warehouse_collection.find(
                    {'Product_name': User_Api.total_cart[i]['Product_name']})
                for data in self.cursor:
                    self.warehouse_collection.update_one({'Product_name': User_Api.total_cart[i]['Product_name']}, {
                        '$set': {'Stock': float(data['Stock']) - float(User_Api.total_cart[i]['Quantity'])}})

            User_Api.total_cart = []
            User_Api.temp = 0
            return 0  # success
        else:
            return -1

    # get all product name from warehouse collection
    def get_all_product_name(self):
        cursor = self.warehouse_collection.find()
        product_name = []
        for data in cursor:
            product_name.append(data['Product_name'])
        return product_name

    def remove_item_from_cart(self, product_name):
        for i in range(len(User_Api.total_cart)):
            if User_Api.total_cart[i]['Product_name'] == product_name:
                User_Api.total_cart.pop(i)
                return 0  # success
        return -1  # error 1: product is not exist

    # get all warehouse data by function get_all_warehouse_data
    # get all invoice data by function get_all_invoice_data