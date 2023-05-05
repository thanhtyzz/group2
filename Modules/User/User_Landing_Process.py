from tkinter import *
from tkinter import messagebox
import Modules.Login.Login_View as lgv
import Modules.User.Component.User_Main_View as usmv
import Modules.Login.Login_View as lgv


class User_Landing_process:

    @staticmethod
    def log_out_button_handle(obj):
        obj.window.destroy()
        app = lgv.Login_View()
        app.window.mainloop()

    @staticmethod
    def items_button_handle(obj):
        obj.window.destroy()
        app = usmv.User_Main_View()
        app.click_button('items')
        app.window.mainloop()

    @staticmethod
    def shop_button_handle(obj):
        obj.window.destroy()
        app = usmv.User_Main_View()
        app.click_button('shop')
        app.window.mainloop()

    @staticmethod
    def log_out_button_handle(obj):
        if messagebox.askyesno("Change Account", "Are you sure you want to change account?"):
            obj.window.destroy()
            app = lgv.Login_View()
            app.window.mainloop()
        else:
            return

