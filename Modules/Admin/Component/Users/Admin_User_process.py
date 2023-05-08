from tkinter import *
from tkinter import messagebox
import tkinter.messagebox as mbox
import Api.Admin_Api as AdminApi
import Modules.Signup.Signup_View as suv

class Admin_User_Process:

    @staticmethod
    def reset_data(obj):
        obj.entry_username.config(state = NORMAL)
        obj.entry_username.delete(0,END)
        obj.entry_password.delete(0,END)
        obj.entry_role.delete(0,END)
        obj.entry_username.config(state = DISABLED)


    @staticmethod
    def get_data(obj):
        username = obj.entry_username.get()
        password = obj.entry_password.get()
        role = obj.entry_role.get()
        if username == '' or password == '' or role == '':
            mbox.showerror('Error','Invalid Input')
            return -1
        else:
            data = {
                'username': username,
                'password': password,
                "roles": role
            }
            return data

    @staticmethod
    def update_button_handle(obj):
        data = Admin_User_Process.get_data(obj)
        if data == -1:
            mbox.showerror("Error", "Invalid user input")
        else:
            api = AdminApi.Admin_Api()
            api.update_user(data)
            for item in obj.tree.get_children():
                obj.tree.delete(item)
            users = api.get_all_users_data()
            for user in users:
                obj.tree.insert('', 'end', values = (user['username'], user['password'], user['roles']))
            mbox.showinfo("Success", "Updated Successfully")

    @staticmethod
    def delete_button_handle(obj):
        # get choosen data of obj.tree
        data = obj.tree.item(obj.tree.selection())['values']
        # remove data from cart
        api = AdminApi.Admin_Api()
        api.remove_user(data)
        # remove data from treeview
        obj.tree.delete(obj.tree.selection())
        mbox.showinfo("Success", "User removed")
        Admin_User_Process.reset_data(obj)

    @staticmethod
    def create_button_handle(self): 
        if messagebox.askyesno("Warning!", "Go to signup page to create a new user account?"): 
            self.window.destroy() 
            app = suv.Signup_View()
            app.window.mainloop() 
        else:
            return