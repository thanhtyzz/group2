from tkinter import *
from tkinter import ttk
from tkinter import messagebox
import Api.User_Api as Api
import Service.Widget_service as ws

class User_Shop_process:

    @staticmethod
    def add_to_cart(obj):

        #add to cart
        obj.quantity.set(obj.quantity_entry.get())
        obj.price.set(obj.price_entry.get())
        api = Api.User_Api()
        check = api.add_item_to_cart(
            obj.search_entry.get(), obj.quantity_entry_bframe.get())
        if check == -1:
            messagebox.showinfo("Error", "Cannot find this movie")
        elif check == -2:
            messagebox.showinfo("Error", "Not enough tickets available")
            obj.search_entry.delete(0, END)
            obj.quantity_entry_bframe.delete(0, END)
        elif check == -3:
            messagebox.showinfo("Error", "Error quantity")
        elif check == -4:

            User_Shop_process.refresh_treeview(obj)
            User_Shop_process.get_total_ammount(obj)
            obj.price.set(api.temp)
            messagebox.showinfo("Success", "Item updated")
        else:
            # add check to treeview
            obj.tree.insert("", "end", values=(check['Film_id'], check['Film'], check['Quantity'], check['Price']))
            obj.film_id.set(check["Film_id"])
            obj.film.set(check["Film"])
            obj.quantity.set(check["Quantity"])
            obj.price.set(check["Price"])
            messagebox.showinfo("Success", "Successfully added ticket to cart")
            User_Shop_process.get_total_ammount(obj)

    @staticmethod
    def remove_from_cart(obj):
        try:
            # get choosen data of obj.tree
            data = obj.tree.item(obj.tree.selection())['values']
            # removing ticket data from cart
            api = Api.User_Api()
            api.remove_item_from_cart(data[1])
            # remove data from treeview
            obj.tree.delete(obj.tree.selection())
            # update total amount
            User_Shop_process.get_total_ammount(obj)
            obj.film_id.set("")
            obj.film.set("")
            obj.quantity.set("")
            obj.price.set("")
            obj.search_entry.delete(0, END)
            obj.quantity_entry.delete(0, END)
            messagebox.showinfo("Success", "Successfully removed ticket from cart")
        except:
            messagebox.showinfo("Error", "No ticket selected")

    @staticmethod
    def get_total_ammount(obj):
        # get total amount
        api = Api.User_Api()
        data = api.total_cart
        total = 0
        for item in data:
            total += int(item['Price'])
        obj.total.set(total)

    @staticmethod
    def process_cart_handle(obj):
        api = Api.User_Api()
        check = api.process_cart()
        if check == 0:
            messagebox.showinfo("Success", "Cart processed")
            # update treeview
            for item in obj.tree.get_children():
                obj.tree.delete(item)

            # remove all data in form frame
            obj.film_id.set("")
            obj.film.set("")
            obj.quantity.set("")
            obj.price.set("")
            obj.total.set("")
            # remove data in button frame
            for item in obj.buttonframe.winfo_children():
                # check item is entry
                if isinstance(item, Entry):
                    item.delete(0, END)
        else:
            messagebox.showinfo("Error", "Empty cart")
            obj.film_id.set("")
            obj.film.set("")
            obj.quantity.set("")
            obj.price.set("")
            obj.total.set("")

    @staticmethod
    def refresh_treeview(obj):
        # update treeview
        api = Api.User_Api()
        for item in obj.tree.get_children():
            obj.tree.delete(item)
        data = api.total_cart
        for item in data:
            obj.tree.insert("", END, values=(item["Film_id"], item["Film"], item["Quantity"], item["Price"]))
