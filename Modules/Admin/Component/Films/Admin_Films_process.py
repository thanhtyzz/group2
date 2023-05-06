from tkinter import *
from tkinter import messagebox
import json
import Api.Admin_Api as admin_api


class Admin_Films_Process:

    @staticmethod
    def addfilm_button_handle(obj):
        api = admin_api.Admin_Api()
        # Get all data from films form
        film_id = obj.film_id_entry.get()
        film = obj.film_entry.get()
        genre = obj.genre_entry.get()
        showtime = obj.showtime_entry.get()
        price = obj.price_entry.get()
        stock = obj.stock_entry.get()
        if film_id == "" or film == "" or genre == "" or showtime == "" or price == "" or stock == "":
            messagebox.showerror("Error", "Invalid Input")
        else:
            json_data = {"Film_ID": f"{film_id}", "Film": f"{film}",
                         "Genre": f"{genre}", "Showtime": f"{showtime}",
                         "Price": float(f"{price}"), "Stock": int(f"{stock}")}
            check = api.add_new_item(json_data)
            if check == -1:
                messagebox.showinfo("Error", "Film ID is not in collection but all information is in collection")
            elif check == 0:
                messagebox.showinfo("Success", "Inserted Succesfully")
            else:
                messagebox.showinfo("Error", "Film already existed")

    @staticmethod
    def reset_button_handle(obj):
        api = admin_api.Admin_Api()
        new_prod_id = api.get_last_prod_id()
        obj.film_id.set(new_prod_id)
        obj.film_entry.delete(0, END)
        obj.genre_entry.delete(0, END)
        obj.showtime_entry.delete(0, END)
        obj.price_entry.delete(0, END)
        obj.stock_entry.delete(0, END)
    
    @staticmethod
    def click_button(self,button):
        if button == "films": 
            apc.Admin_Films_create.generate_films(self) 
        elif button == "inventory":
            aic.Admin_Inventory_create.generate_inventory(self)
        elif button == "sales": 
            asc.Admin_Sales_create.generate_sales(self) 
        elif button == "users":
            auc.Admin_User_create.generate_users(self) 

    def exit_button(self): 
            if messagebox.askyesno("Quit", "Are you sure you want to quit?"): 
                self.window.destroy() 
                exit() 
            else: 
                return
        
    def switch_account(self): 
        if messagebox.askyesno("Change Account", "Are you sure you want to change account?"): 
            self.window.destroy() 
            app = lgv.Login_View()
            app.window.mainloop() 
        else:
            return
