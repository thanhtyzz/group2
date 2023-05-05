from tkinter import *
from tkinter import messagebox
import Modules.Admin.Component.Products.Admin_Products_create as apc
import Modules.Admin.Component.Inventory.Admin_Inventory_create as aic
import Modules.Admin.Component.Sales.Admin_Sales_create as asc
import Modules.Admin.Component.Users.Admin_User_create as auc
import Modules.Login.Login_View as lgv


class Admin_Main_View:

    def __init__(self):

        self.window = Tk()

        # get screen width and height
        self.screen_width = self.window.winfo_screenwidth()
        self.screen_height = self.window.winfo_screenheight()

        # set window width and height
        self.window_width = 1080
        self.window_height = 720
        # set window position
        self.window.geometry("%dx%d+%d+%d" % (self.window_width, self.window_height,
                                              (self.screen_width - self.window_width) / 2,
                                              (self.screen_height - self.window_height) / 2))

        self.window.configure(bg="#ffffff")
        self.window.title('Admin')
        self.window.iconphoto(False, PhotoImage(
            file=f"./Images/User/MainPage/UserIcon.png"))

        self.allframes = []

        self.canvas = Canvas(self.window, bg="#ffffff", height=720, width=1080,
                             bd=0, highlightthickness=0, relief="ridge")
        self.canvas.place(x=0, y=0)

        # -----background-----
        self.img_background = PhotoImage(file=f"./Images/Admin/MainPage/background.png")
        self.background = self.canvas.create_image(540, 65, image=self.img_background)

        # -----button-products-----
        self.img_products = PhotoImage(file=f"./Images/Admin/MainPage/img_products.png")
        self.button_products = Button(image=self.img_products, borderwidth=0,
                                      highlightthickness=0, relief="flat", bg="#ffffff", activebackground="#ffffff",
                                      command=lambda: self.click_button("products"))

        self.button_products.place(x=30, y=160, width=155, height=60)

        # -----button-inventory-----
        self.img_inventory = PhotoImage(file=f"./Images/Admin/MainPage/img_inventory.png")
        self.button_inventory = Button(image=self.img_inventory, borderwidth=0,
                                       highlightthickness=0, relief="flat", bg="#ffffff", activebackground="#ffffff",
                                       command=lambda: self.click_button("inventory"))

        self.button_inventory.place(x=200, y=160, width=155, height=60)

        # -----button-sales-----
        self.img_sales = PhotoImage(file=f"./Images/Admin/MainPage/img_sales.png")
        self.button_sales = Button(image=self.img_sales, borderwidth=0,
                                   highlightthickness=0, relief="flat", bg="#ffffff", activebackground="#ffffff",
                                   command=lambda: self.click_button("sales"))

        self.button_sales.place(x=380, y=160, width=155, height=60)

        # -----button-users-----
        self.img_users = PhotoImage(file=f"./Images/Admin/MainPage/img_users.png")
        self.button_users = Button(image=self.img_users, borderwidth=0,
                                   highlightthickness=0, relief="flat", bg="#ffffff", activebackground="#ffffff",
                                   command=lambda: self.click_button("users"))

        self.button_users.place(x=550, y=160, width=155, height=60)

        # -----button-switch-account-----
        self.img_switch = PhotoImage(file=f"./Images/Admin/MainPage/img_switch.png")
        self.button_switch = Button(image=self.img_switch, borderwidth=0,
                                    highlightthickness=0, relief="flat", bg="#ffffff", activebackground="#ffffff",
                                    command=lambda: self.switch_account())

        self.button_switch.place(x=730, y=160, width=155, height=60)

        # -----button-exit-----
        self.img_exit = PhotoImage(file=f"./Images/Admin/MainPage/img_exit.png")
        self.button_exit = Button(image=self.img_exit, borderwidth=0,
                                  highlightthickness=0, relief="flat", bg="#ffffff", activebackground="#ffffff",
                                  command=lambda: self.exit_button())

        self.button_exit.place(x=900, y=160, width=155, height=60)
        self.window.resizable(False, False)

    def click_button(self, button):
        if button == "products":
            apc.Admin_Products_create.generate_products(self)
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