from cgitb import reset
from tkinter import *
import Api.Admin_Api as AdminApi
import Modules.Admin.Component.Inventory.Admin_Inventory_create as aic
import Api.Main_Api as MainApi
import tkinter.messagebox as mbox


class Admin_Inventory_Process:

    @staticmethod
    def get_json_data(obj):
        product_name = obj.product_name_entry.get()
        description = obj.description_entry.get()
        category = obj.category_entry.get()
        price = obj.price_entry.get()
        current_stock = obj.current_stock_entry.get()
        add_stock = obj.add_stock_entry.get()
        if product_name == '' or description == '' or category == '' or price == '' or current_stock == '' or add_stock == '':
            return 0
        else:
            json_data = {
                'Product_name': f'{product_name}',
                'Description' : f'{description}',
                'Category': f'{category}',
                'Price': f'{price}',
                'Stock': f'{int(current_stock) + int(add_stock)}',
            }
            return json_data

    @staticmethod
    def update_button_handle(obj):
        data = Admin_Inventory_Process.get_json_data(obj)
        if data == 0:
            mbox.showerror('Error','Invalid User Input')
        else:
            #get the product id selected in treeview
            product_id = obj.tree.item(obj.tree.selection())['values'][0]
            api = AdminApi.Admin_Api()
            check = api.update_items(data, product_id)
            if check == -2:
                mbox.showerror('Error','Product id is not in collection but all information is in collection')
            else:
                for item in obj.tree.get_children():
                    obj.tree.delete(item)
                table_data = api.get_all_warehouse_data()
                for row in table_data:
                    obj.tree.insert('', 'end', values = (row['Product_id'], row['Product_name'], row['Description'], row['Category'], row['Price'], row['Stock']))
                mbox.showinfo('Success','Updated Succesfully')
                obj.current_stock_entry.config(state = NORMAL)
                obj.product_name_entry.delete(0, END)
                obj.description_entry.delete(0, END)
                obj.category_entry.delete(0, END)
                obj.price_entry.delete(0, END)
                obj.current_stock_entry.delete(0, END)
                obj.add_stock_entry.delete(0, END)
                obj.current_stock_entry.config(state = DISABLED)

    @staticmethod
    def remove_button_handle(obj):
        api = AdminApi.Admin_Api()
        #get the product id selected in treeview
        product_id = obj.tree.item(obj.tree.selection())['values'][0]
        check = api.remove_items(product_id)
        mbox.showinfo('Success','Removed successfully')
        for item in obj.tree.get_children():
            obj.tree.delete(item)
        table_data = api.get_all_warehouse_data()
        for row in table_data:
            obj.tree.insert('', 'end', values = (row['Product_id'], row['Product_name'], row['Description'], row['Category'], row['Price'], row['Stock']))
        obj.product_name_entry.delete(0, END)
        obj.description_entry.delete(0, END)
        obj.category_entry.delete(0, END)
        obj.price_entry.delete(0, END)
        obj.current_stock_entry.delete(0, END)
        obj.add_stock_entry.delete(0, END)

    @staticmethod
    def reset(obj):
        obj.product_name_entry.delete(0, END)
        obj.description_entry.delete(0, END)
        obj.category_entry.delete(0, END)
        obj.price_entry.delete(0, END)
        obj.current_stock_entry.delete(0, END)
        obj.add_stock_entry.delete(0, END)

    @staticmethod
    def search_button_handle(obj):
        api = AdminApi.Admin_Api()
        search_term = obj.search_entry.get()
        if search_term == '':
            mbox.showerror('Error','Invalid User Input')
        else:
            for item in obj.tree.get_children():
                obj.tree.delete(item)
            data  = api.warehouse_collection.find({'Product_name': {'$regex': f'{search_term}', '$options': 'i'}})
            for row in data:
                obj.tree.insert('', 'end', values = (row['Product_id'], row['Product_name'], row['Description'], row['Category'], row['Price'], row['Stock']))

    @staticmethod
    def reset_button_handle(obj):
        api = AdminApi.Admin_Api()
        for item in obj.tree.get_children():
            obj.tree.delete(item)
        table_data = api.get_all_warehouse_data()
        for row in table_data:
            obj.tree.insert('', 'end', values = (row['Product_id'], row['Product_name'], row['Description'], row['Category'], row['Price'], row['Stock']))
        obj.current_stock_entry.config(state = NORMAL)
        obj.search_entry.delete(0, END)
        obj.product_name_entry.delete(0, END)
        obj.description_entry.delete(0, END)
        obj.category_entry.delete(0, END)
        obj.price_entry.delete(0, END)
        obj.current_stock_entry.delete(0, END)
        obj.add_stock_entry.delete(0, END)
        obj.current_stock_entry.config(state = DISABLED)