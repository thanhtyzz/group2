from tkinter import *
import sys
sys.path.append("C:\\Users\\User\\PycharmProjects\\FinalTerm\\Modules\\Admin\\Admin_Landing_Process")
import Admin_Landing_Process as ap


class Admin_View:

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

        self.canvas = Canvas(self.window, bg="#ffffff", height=720, width=1080,
                             bd=0, highlightthickness=0, relief="ridge")

        self.canvas.place(x=0, y=0)

        # -----background-----
        self.background_img = PhotoImage(file=f"./Images/Admin/LandingPage/Background.png")
        self.background = self.canvas.create_image(565, 375, image=self.background_img)

        # -----button-log-out-----
        self.img_log_out = PhotoImage(file=f"./Images/Admin/LandingPage/Button_Logout.png")
        self.button_log_out = Button(image=self.img_log_out, borderwidth=0,
                                     highlightthickness=0, relief="flat", bg="#ffffff", activebackground="#ffffff",
                                     command=lambda: ap.Admin_Process.log_out_button_handle(self))

        self.button_log_out.place(x=800, y=60, width=210, height=60)

        # -----button-products-----
        self.img_products = PhotoImage(file=f"./Images/Admin/LandingPage/Button_Products.png")
        self.button_products = Button(image=self.img_products, borderwidth=0,
                                      highlightthickness=0, relief="flat", bg="#ffffff", activebackground="#ffffff",
                                      command=lambda: ap.Admin_Process.products_button_handle(self))

        self.button_products.place(x=49, y=582, width=170, height=55)

        # -----button-inventory-----
        self.img_inventory = PhotoImage(file=f"./Images/Admin/LandingPage/Button_Inventory.png")

        self.button_inventory = Button(image=self.img_inventory, borderwidth=0,
                                       highlightthickness=0, relief="flat", bg="#ffffff", activebackground="#ffffff",
                                       command=lambda: ap.Admin_Process.inventory_button_handle(self))

        self.button_inventory.place(x=219, y=582, width=170, height=55)

        # -----button-sales-----
        self.img_sales = PhotoImage(file=f"./Images/Admin/LandingPage/Button_Sales.png")
        self.button_sales = Button(image=self.img_sales, borderwidth=0, highlightthickness=0,
                                   relief="flat", bg="#ffffff", activebackground="#ffffff",
                                   command=lambda: ap.Admin_Process.sales_button_handle(self))

        self.button_sales.place(x=389, y=582, width=170, height=55)

        # -----button-users-----
        self.img_users = PhotoImage(file=f"./Images/Admin/LandingPage/Button_Users.png")
        self.button_users = Button(image=self.img_users, borderwidth=0, highlightthickness=0,
                                   relief="flat", bg="#ffffff", activebackground="#ffffff",
                                   command=lambda: ap.Admin_Process.users_button_handle(self))

        self.button_users.place(x=559, y=582, width=170, height=55)

        self.window.resizable(False, False)