from cgitb import reset
from tkinter import *
import Api.Admin_Api as AdminApi
import Modules.Admin.Component.Inventory.Admin_Inventory_create as aic
import Api.Main_Api as MainApi
import tkinter.messagebox as mbox


class Admin_Inventory_Process:

    @staticmethod
    def get_json_data(obj):
        film = obj.film_entry.get()
        genre = obj.genre_entry.get()
        price = obj.price_entry.get()
        showtime = obj.showtime_entry.get()
        stock = obj.stock_entry.get()
        add_stock = obj.add_stock_entry.get()
        if film == '' or genre == '' or showtime == '' or price == '' or stock == '' or add_stock == '':
            return 0
        else:
            json_data = {
                'Film': f'{film}',
                'Genre': f'{genre}',
                'Price': f'{price}',
                'Showtime': f'{showtime}',
                'Stock': f'{int(stock) + int(add_stock)}',}
            return json_data

    @staticmethod
    def update_button_handle(obj):
        data = Admin_Inventory_Process.get_json_data(obj)
        if data == 0:
            mbox.showerror('Error', 'Missing input data')
        else:
            # Get the ID of the selected film in the treeview
            film_id = obj.tree.item(obj.tree.selection())['values'][0]
            api = AdminApi.Admin_Api()
            check = api.update_items(data, film_id)
            if check == -2:
                mbox.showerror('Error', 'Film ID already exists in the collection')
            elif check == -3:
                mbox.showerror('Error', 'Incorrect Showtime format')
            elif check == -1:
                mbox.showinfo('Info', 'No new information was provided for update')
            else:
                obj.tree.delete(*obj.tree.get_children())
                table_data = api.get_all_warehouse_data()
                for row in table_data:
                    obj.tree.insert('', 'end', values=(
                    row['Film_ID'], row['Film'], row['Genre'], row['Showtime'], row['Price'], row['Stock']))
                mbox.showinfo('Success', 'Update process completed')
                obj.current_stock_entry.config(state=NORMAL)
                obj.film_entry.delete(0, END)
                obj.genre_entry.delete(0, END)
                obj.showtime_entry.delete(0, END)
                obj.price_entry.delete(0, END)
                obj.current_stock_entry.delete(0, END)
                obj.add_stock_entry.delete(0, END)
                obj.current_stock_entry.config(state=DISABLED)

    @staticmethod
    def remove_button_handle(obj):
        api = AdminApi.Admin_Api()
        # Get the ID of the selected film in the treeview
        film_id = obj.tree.item(obj.tree.selection())['values'][1]
        check = api.remove_items(film_id)
        mbox.showinfo('Success', 'Update process completed')
        for item in obj.tree.get_children():
            obj.tree.delete(item)
        table_data = api.get_all_warehouse_data()
        for row in table_data:
            obj.tree.insert('', 'end', values=(row['Film_ID'], row['Film'], row['Genre'], row['Showtime'], row['Price'], row['Stock']))
        obj.film_entry.delete(0, END)
        obj.genre_entry.delete(0, END)
        obj.showtime_entry.delete(0, END)
        obj.price_entry.delete(0, END)
        obj.current_stock_entry.delete(0, END)
        obj.add_stock_entry.delete(0, END)

    @staticmethod
    def reset(obj):
        obj.film_name_entry.delete(0, END)
        obj.genre_entry.delete(0, END)
        obj.showtime_entry.delete(0, END)
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
            data  = api.warehouse_collection.find({'Film': {'$regex': f'{search_term}', '$options': 'i'}})
            for row in data: 
                obj.tree.insert('', 'end', values = (row['Film_id'], row['Film'], row['Genre'], row['Showtime'], row['Price'], row['Stock']))

    @staticmethod 
    def reset_button_handle(obj): 
        api = AdminApi.Admin_Api()
        for item in obj.tree.get_children(): 
            obj.tree.delete(item) 
        table_data = api.get_all_warehouse_data()
        for row in table_data: 
            obj.tree.insert('', 'end', values = (row['Film_id'], row['Film'], row['Genre'], row['Showtime'], row['Price'], row['Stock']))
        obj.current_stock_entry.config(state = NORMAL)
        obj.search_entry.delete(0, END)
        obj.film_entry.delete(0, END) 
        obj.genre_entry.delete(0, END) 
        obj.showtime_entry.delete(0, END)
        obj.price_entry.delete(0, END)
        obj.current_stock_entry.delete(0, END)
        obj.add_stock_entry.delete(0, END)
        obj.current_stock_entry.config(state = DISABLED)
        
