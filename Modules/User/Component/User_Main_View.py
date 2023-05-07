from tkinter import *
from pathlib import Path
import Modules.User.Component.Films.User_Films_create as uic
import Modules.User.Component.Buytickets.User_Buytickets_create as ubc 
from tkinter import messagebox 
import Modules.Login.Login_View as lgv


class User_Main_View:
    
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
        self.window.title("Buytickets")

        self.allframes = []

        self.canvas = Canvas(self.window, bg="#FFFFFF", height=492, width=685, bd=0, highlightthickness=0, relief="ridge")
        self.canvas.place(x=0, y=0)

        assets_path = Path(r"D:\do-an-cuoi-ki-nhom-2\Images\User\MainPage")

        self.background_img = PhotoImage(file=assets_path / "Background.png")
        self.films_image = PhotoImage(file=assets_path / "Button_Films.png")
        self.invoice_image = PhotoImage(file=assets_path / "Button_Invoice.png")
        self.signout_image = PhotoImage(file=assets_path / "Button_Signout.png")
        self.quit_image = PhotoImage(file=assets_path / "Button_Quit.png")

        self.background = self.canvas.create_image(342.0, 246.0, image=self.background_img)

        self.films_button = Button(self.window, image=self.films_image, borderwidth=0, highlightthickness=0,
                               command=lambda: self.click_button("films"))
        self.films_button.place(x=61.0, y=128.0, width=107.0, height=38.0)

        self.invoice_button = Button(self.window, image=self.invoice_image, borderwidth=0, highlightthickness=0,
                               command=lambda: self.click_button("buytickets"))
        self.invoice_button.place(x=212.0, y=131.0, width=101.0, height=33.0)

        self.signout_button = Button(self.window, image=self.signout_image, borderwidth=0, highlightthickness=0,
                               command = self.change_account)
        self.signout_button.place(x=363.0, y=131.0, width=103.0, height=33.0)

        self.quit_button = Button(self.window, image=self.quit_image, borderwidth=0, highlightthickness=0,
                               command = self.quit_button_click)
        self.quit_button.place(x=514.0, y=131.0, width=106.0, height=34.0)
        self.window.resizable(0, 0)

    def quit_button_click(self): 
        if messagebox.askyesno("Quit", "Are you sure you want to quit?"): 
            self.window.destroy() 
            exit() 
        else: 
            return
    
    def change_account(self): 
        if messagebox.askyesno("Change Account", "Are you sure you want to change account?"): 
            self.window.destroy() 
            app = lgv.Login_View()
            app.window.mainloop() 
        else:
            return 

    def click_button(self, button): 
        if button == "films": 
            uic.User_Films_create.generate_films(self)
        elif button == "buytickets": 
            ubc.User_Buytickets_create.generate_buytickets(self)
