import Api.Login_Api as Login_Api
from tkinter import messagebox
import Modules.Signup.Sign_up_View as suv
from tkinter import *
import Modules.Admin.Admin_Landing_View as av
import Modules.User.User_Landing_View as uv


class Login_Process:

    @staticmethod
    def confirm_button_handle(obj):
        username = obj.name_entry.get()
        password = obj.password_entry.get()
        api = Login_Api.Login_Api()
        c = api.check_user_login(username, password)
        if c == -1:
            messagebox.showerror("Warning", "Invalid User Input")
            obj.name_entry.delete(0, END)
            obj.password_entry.delete(0, END)

        elif c == -2:
            messagebox.showerror("Warning", "User not found")
            obj.name_entry.delete(0, END)
            obj.password_entry.delete(0, END)

        elif c == -3:
            messagebox.showerror("Warning", "Wrong password")
            obj.password_entry.delete(0, END)
        else:
            if c == "Admin":
                messagebox.showinfo("MB", "Welcome Admin")
                obj.window.destroy()
                app = av.Admin_View()
                app.window.mainloop()

            if c == "User":
                messagebox.showinfo("MB", "Welcome User")
                obj.window.destroy()
                app = uv.User_Landing_View()
                app.window.mainloop()

    @staticmethod
    def signup_button_handle(obj):
        obj.window.destroy()
        app = suv.Sign_up_View()
        app.window.mainloop()