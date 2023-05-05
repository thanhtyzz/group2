from tkinter import *
from tkinter import messagebox
import json
import Api.Admin_Api as admin_api


class Admin_Products_Process:

    @staticmethod
    def add_item_button_handle(obj):
        api = admin_api.Admin_Api()
        # Get all data from products form
        product_id = obj.product_id_entry.get()
        product_name = obj.product_name_entry.get()
        description = obj.description_entry.get()
        category = obj.category_entry.get()
        price = obj.price_entry.get()
        stock = obj.stock_entry.get()
        if product_id == "" or product_name == "" or category == "" or price == "" or stock == "":
            messagebox.showerror("Error", "Invalid Input")
        else:
            json_data = {"Product_id": f"{product_id}", "Product_name": f"{product_name}",
                         "Description": f"{description}", "Category": f"{category}",
                         "Price": float(f"{price}"), "Stock": int(f"{stock}")}
            check = api.add_new_item(json_data)
            if check == -1:
                messagebox.showinfo("Error", "Product id is not in collection but all information is in collection")
            elif check == 0:
                messagebox.showinfo("Success", "Inserted Succesfully")
            else:
                messagebox.showinfo("Error", "Product already existed")

    @staticmethod
    def reset_button_handle(obj):
        api = admin_api.Admin_Api()
        new_prod_id = api.get_last_prod_id()
        obj.product_id.set(new_prod_id)
        obj.product_name_entry.delete(0, END)
        obj.description_entry.delete(0, END)
        obj.category_entry.delete(0, END)
        obj.price_entry.delete(0, END)
        obj.stock_entry.delete(0, END)