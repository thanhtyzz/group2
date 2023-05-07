from tkinter import *
from pathlib import Path
from tkinter import messagebox
import Modules.Admin.Component.Films.Admin_Films_create as apc
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
        self.window_width = 685
        self.window_height = 492
        # set window position
        self.window.geometry("%dx%d+%d+%d" % (self.window_width, self.window_height,
                             (self.screen_width - self.window_width) / 2, (self.screen_height - self.window_height) / 2))
        self.window.configure(bg="#FFFFFF")
        self.window.title("Admin")

        self.allframes = []

        self.canvas = Canvas(self.window, bg="#FFFFFF", height=492, width=685, bd=0, highlightthickness=0, relief="ridge")
        self.canvas.place(x=0, y=0)

        assets_path = Path(r"D:\do-an-cuoi-ki-nhom-2\Images\Admin\MainPage")

        self.background_img = PhotoImage(file=assets_path / "Background.png")
        self.films_image = PhotoImage(file=assets_path / "Button_Films.png")
        self.inventory_image = PhotoImage(file=assets_path / "Button_Inventory.png")
        self.sales_image = PhotoImage(file=assets_path / "Button_Sales.png")
        self.users_image = PhotoImage(file=assets_path / "Button_Users.png")
        self.switch_image = PhotoImage(file=assets_path / "Button_Switch.png")
        self.exit_image = PhotoImage(file=assets_path / "Button_Exit.png")

        self.background = self.canvas.create_image(342.0, 246.0, image=self.background_img)

        self.films_button = Button(image=self.films_image, borderwidth=0, highlightthickness=0,
                               command=lambda: self.click_button("films"), relief="flat")
        self.films_button.place(x=10.0, y=124.0, width=97.0, height=37.0)

        self.inventory_button = Button(image=self.inventory_image, borderwidth=0, highlightthickness=0,
                               command=lambda: self.click_button("inventory"), relief="flat")
        self.inventory_button.place(x=118.0, y=125.0, width=102.0, height=35.0)

        self.sales_button = Button(image=self.sales_image, borderwidth=0, highlightthickness=0,
                               command=lambda: self.click_button("sales"), relief="flat")
        self.sales_button.place(x=233.0, y=126.0, width=97.0, height=33.0)

        self.users_button = Button(image=self.users_image, borderwidth=0, highlightthickness=0,
                               command=lambda: self.click_button("users"), relief="flat")
        self.users_button.place(x=349.0, y=126.0, width=97.0, height=33.0)

        self.switch_button = Button(image=self.switch_image, borderwidth=0, highlightthickness=0,
                               command=lambda: self.switch_account(), relief="flat")
        self.switch_button.place(x=461.0, y=126.0, width=97.0, height=33.0)

        self.exit_button = Button(image=self.exit_image, borderwidth=0, highlightthickness=0,
                               command=lambda: self.exit(), relief="flat")
        self.exit_button.place(x=576.0, y=126.0, width=97.0, height=33.0)
        self.window.resizable(0, 0)

    def click_button(self,button):
        if button == "films": 
            apc.Admin_Films_create.generate_films(self) 
        elif button == "inventory":
            aic.Admin_Inventory_create.generate_inventory(self)
        elif button == "sales": 
            asc.Admin_Sales_create.generate_sales(self) 
        elif button == "users":
            auc.Admin_User_create.generate_users(self) 

    def exit(self): 
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