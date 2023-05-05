import Api.Login_Api as Login_Api
from tkinter import messagebox
import Modules.Signup.Signup_View as suv
from tkinter import *
import Modules.Admin.Admin_Landing_View as av
import Modules.User.User_Landing_View as uv


class Login_Process:

    @staticmethod
    def confirm_button_handle(obj):
        username = obj.entry_1.get()
        password = obj.entry_2.get()
        api = Login_Api.Login_Api()
        c = api.check_user_login(username, password)
        if c == -1:
            messagebox.showerror("Warning", "Invalid User Input")
            obj.entry_1.delete(0, END)
            obj.entry_2.delete(0, END)

        elif c == -2:
            messagebox.showerror("Warning", "User not found")
            obj.entry_1.delete(0, END)
            obj.entry_2.delete(0, END)

        elif c == -3:
            messagebox.showerror("Warning", "Wrong password")
            obj.entry_2.delete(0, END)
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
        app = suv.Signup_View()
        app.window.mainloop()
