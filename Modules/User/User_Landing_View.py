from tkinter import *
from pathlib import Path
import Modules.User.User_Landing_Process as up


class User_Landing_View:
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
                                              (self.screen_width - self.window_width) / 2,
                                              (self.screen_height - self.window_height) / 2))
        self.window.configure(bg="#FFFFFF")
        self.window.title("User")

        self.canvas = Canvas(self.window, bg="#FFFFFF", height=492, width=685, bd=0, highlightthickness=0,
                             relief="ridge")
        self.canvas.place(x=0, y=0)

        assets_path = Path(r"r"D:\do-an-cuoi-ki-nhom2\Images\User\LandingPage")

        self.background_img = PhotoImage(file=assets_path / "Background.png")
        self.logout_image = PhotoImage(file=assets_path / "Button_Logout.png")
        self.films_image = PhotoImage(file=assets_path / "Button_Films.png")
        self.buytickets_image = PhotoImage(file=assets_path / "Button_BuyTickets.png")

        self.background = self.background_img.create_image(342.0, 246.0, image=self.background_img)

        self.logout_button = Button(image=self.logout_image, borderwidth=0, highlightthickness=0,
                                    command=lambda: up.User_Landing_process.log_out_button_handle(self))
        self.logout_button.place(x=570.0, y=13.0, width=103.0, height=35.0)

        self.films_button = Button(image=self.films_image, borderwidth=0, highlightthickness=0,
                                   command=lambda: up.User_Landing_process.films_button_handle(self))
        self.films_button.place(x=204.0, y=406.0, width=121.0, height=42.0)

        self.buytickets_button = Button(image=self.buytickets_image, borderwidth=0, highlightthickness=0,
                                        command=lambda: up.User_Landing_process.buytickets_button_handle(self))
        self.buytickets_button.place(x=362.0, y=405.0, width=123.0, height=43.0)
        self.window.resizable(0, 0)

