import Api.Login_Api as Login_Api
import Api.Signup_Api as Signup_Api
import Modules.Login.Login_View as loginview
from tkinter import END, messagebox as mbox


class Sign_up_Process:

    @staticmethod
    def login_button_handle(obj):
        obj.window.destroy()
        app = loginview.Login_View()
        app.window.mainloop()

    @staticmethod
    def signup_button_handle(obj):
        username = obj.username_entry.get()
        password = obj.password_entry.get()
        reenterpassword = obj.reenterpass_entry.get()
        api = Signup_Api.Signup_Api()
        error = api.check_user_signup(username, password, reenterpassword)

        if error == -1:
            mbox.showerror('Warning', 'Invalid User Input')
            obj.username_entry.delete(0, END)
            obj.password_entry.delete(0, END)
            obj.reenterpass_entry.delete(0, END)

        elif error == -2:
            mbox.showerror('Warning', 'Password is not the same')
            obj.username_entry.delete(0, END)
            obj.password_entry.delete(0, END)
            obj.reenterpass_entry.delete(0, END)

        elif error == -3:
            mbox.showerror('Warning', 'Existed user')
            obj.username_entry.delete(0, END)
            obj.password_entry.delete(0, END)
            obj.reenterpass_entry.delete(0, END)

        else:
            mbox.showinfo('Success', 'Account created successfully')
            obj.username_entry.delete(0, END)
            obj.password_entry.delete(0, END)
            obj.reenterpass_entry.delete(0, END)