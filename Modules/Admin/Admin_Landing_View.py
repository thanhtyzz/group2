from tkinter import *
from pathlib import Path
import Modules.Admin.Admin_Landing_Process as ap


class Admin_View:
    def __init__(self):
        self.window = Tk()
        # get screen width and height
        self.screen_width = self.window.winfo_screenwidth()
        self.screen_height = self.window.winfo_screenheight()

        # set window width and height
        self.window_width = 685
        self.window_height = 492
        # set window position
        self.window.geometry("%dx%d+%d+%d" % (self.window_width, self.window_height,
                             (self.screen_width - self.window_width) / 2, (self.screen_height - self.window_height) / 2))
        self.window.configure(bg="#FFFFFF")
        self.window.title("Admin")

        self.canvas = Canvas(self.window, bg="#FFFFFF", height=492, width=685, bd=0, highlightthickness=0, relief="ridge")
        self.canvas.place(x=0, y=0)

        assets_path = Path(r"D:\do-an-cuoi-ki-nhom-2\Images\Admin\LandingPage")

        self.background_img = PhotoImage(file=assets_path / "Background.png")
        self.logout_image = PhotoImage(file=assets_path / "Button_Logout.png")
        self.films_image = PhotoImage(file=assets_path / "Button_Films.png")
        self.inventory_image = PhotoImage(file=assets_path / "Button_Inventory.png")
        self.sales_image = PhotoImage(file=assets_path / "Button_Sales.png")
        self.users_image = PhotoImage(file=assets_path / "Button_Users.png")

        self.background = self.canvas.create_image(342.0, 246.0, image=self.background_img)

        self.logout_button = Button(image=self.logout_image, borderwidth=0, highlightthickness=0,
                               command=lambda: ap.Admin_Process.log_out_button_handle(self))
        self.logout_button.place(x=564.0, y=19.0, width=101.0, height=36.0)

        self.films_button = Button(image=self.films_image, borderwidth=0, highlightthickness=0,
                               command=lambda: ap.Admin_Process.films_button_handle(self))
        self.films_button.place(x=51.0, y=343.0, width=101.0, height=36.0)

        self.inventory_button = Button(image=self.inventory_image, borderwidth=0, highlightthickness=0,
                               command=lambda: ap.Admin_Process.inventory_button_handle(self))
        self.inventory_button.place(x=208.0, y=341.0, width=101.0, height=36.0)

        self.sales_button = Button(image=self.sales_image, borderwidth=0, highlightthickness=0,
                               command=lambda: ap.Admin_Process.sales_button_handle(self))
        self.sales_button.place(x=51.0, y=400.0, width=101.0, height=36.0)

        self.users_button = Button(image=self.users_image, borderwidth=0, highlightthickness=0,
                               command=lambda: ap.Admin_Process.users_button_handle(self))
        self.users_button.place(x=208.0, y=402.0, width=101.0, height=36.0)
        self.window.resizable(0, 0)
