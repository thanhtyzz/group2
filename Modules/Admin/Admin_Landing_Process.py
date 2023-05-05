from tkinter import *
import Modules.Login.Login_View as lgv
import Modules.Admin.Component.Admin_Main_View as amv


class Admin_Process:

    @staticmethod
    def log_out_button_handle(obj):
        obj.window.destroy()
        app = lgv.Login_View()
        app.window.mainloop()

    @staticmethod
    def films_button_handle(obj):
        obj.window.destroy()
        app = amv.Admin_Main_View()
        app.click_button('Films')
        app.window.mainloop()

    @staticmethod
    def inventory_button_handle(obj):
        obj.window.destroy()
        app = amv.Admin_Main_View()
        app.click_button('Inventory')
        app.window.mainloop()

    @staticmethod
    def sales_button_handle(obj):
        obj.window.destroy()
        app = amv.Admin_Main_View()
        app.click_button('Sales')
        app.window.mainloop()

    @staticmethod
    def users_button_handle(obj):
        obj.window.destroy()
        app = amv.Admin_Main_View()
        app.click_button('Users')
        app.window.mainloop()
