from tkinter import *
import tkinter as tk
from pathlib import Path
import Modules.Signup.Signup_Process as signup_process
import matplotlib.pyplot as plt
import matplotlib.image as mpimg


class Signup_View:
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
        self.window.title("Signup")

        self.canvas = Canvas(self.window, bg="#FFFFFF", height=492, width=685, bd=0, highlightthickness=0, relief="ridge")
        self.canvas.place(x=0, y=0)

        assets_path = Path(r"D:\do-an-cuoi-ki-nhom-2\Images\Signup")

        self.background_img = PhotoImage(file=assets_path / "Background.png")
        self.login_image = PhotoImage(file=assets_path / "Button_Login.png")
        self.signup_image_1 = PhotoImage(file=assets_path / "Button_Signup_1.png")
        self.entry_image = PhotoImage(file=assets_path / "Textbox.png")
        self.trendingnow_image = PhotoImage(file=assets_path / "Button_Trendingnow.png")
        self.signup_image_2 = PhotoImage(file=assets_path / "Button_Signup_2.png")

        self.background = self.canvas.create_image(342.0, 246.0, image=self.background_img)

        self.login_button = Button(image=self.login_image, borderwidth=0, highlightthickness=0,
                               command=lambda: signup_process.Signup_Process.login_button_handle(self))
        self.login_button.place(x=532.0, y=12.0, width=69.0, height=33.0)

        self.signup_button_1 = Button(image=self.signup_image_1, borderwidth=0, highlightthickness=0,
                               command=lambda: print("signup_button_1 clicked"), relief="flat")
        self.signup_button_1.place(x=607.0, y=12.0, width=70.0, height=33.0)

        self.entry_bg_1 = self.canvas.create_image(354.0, 230.0, image=self.entry_image)
        self.entry_1 = Entry(bd=0, bg="#F8EBD1", fg="#000716", highlightthickness=0)
        self.entry_1.place(x=268.0, y=214.0, width=172.0, height=30.0)

        self.entry_bg_2 = self.canvas.create_image(354.0, 293.0, image=self.entry_image)
        self.entry_2 = Entry(bd=0, bg="#F8EBD1", fg="#000716", highlightthickness=0)
        self.entry_2.place(x=268.0, y=277.0, width=172.0, height=30.0)

        self.entry_bg_3 = self.canvas.create_image(354.0, 355.0, image=self.entry_image)
        self.entry_3 = Entry(bd=0, bg="#F8EBD1", fg="#000716", highlightthickness=0)
        self.entry_3.place(x=268.0, y=339.0, width=172.0, height=30.0)

        self.trendingnow_button = Button(image=self.trendingnow_image, borderwidth=0, highlightthickness=0,
                               command=lambda: signup_process.Trendingnow_process.trendingnow(self), relief="flat")
        self.trendingnow_button.place(x=465.0, y=427.0, width=203.0, height=55.0)
        # The 'Trending Now' button displays the movies that are currently trending
       
        self.signup_button_2 = Button(image=self.signup_image_2, borderwidth=0, highlightthickness=0,
                               command=lambda: signup_process.Signup_Process.signup_button_handle(self))
        self.signup_button_2.place(x=315.0, y=391.0, width=78.0, height=31.0)
        self.window.resizable(0, 0)

class Tredingnow_View:
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
                             (self.screen_width - self.window_width) / 2, (self.screen_height - self.window_height) / 2))
        self.window.configure(bg="#FFFFFF")
        self.window.title("TredingNow")
        self.canvas = Canvas(self.window, bg="#FFFFFF", height=492, width=685, bd=0, highlightthickness=0, relief="ridge")
        self.canvas.place(x=0, y=0)

        assets_path = Path(r"D:\do-an-cuoi-ki-nhom-2\Images\Trendingnow")

        self.phim1 = PhotoImage(file=assets_path / "D:\do-an-cuoi-ki-nhom-2\Images\SignUp\Button_Login.png")
        self.phim2 = PhotoImage(file=assets_path / "D:\do-an-cuoi-ki-nhom-2\Images\SignUp\Button_Login.png")
        # self.phim3 = PhotoImage(file=assets_path / "phim3.jpg")
        # self.phim4 = PhotoImage(file=assets_path / "phim4.jpg")
        # self.phim5 = PhotoImage(file=assets_path / "phim5.jpg")
        # self.phim6 = PhotoImage(file=assets_path / "phim6.jpg")

        self.vitri1 = self.canvas.create_image(342.0, 246.0, image=self.phim1)
        self.vitri2 = self.canvas.create_image(500, 500.0, image=self.phim2)

        # self.phim11 = Button(image=self.phim1, borderwidth=0, highlightthickness=0,
        #                        command=lambda: signup_process.Signup_Process.Trendingnow_process(self))
        # self.phim11(x=10.0, y=124.0, width=97.0, height=37.0)
        # self.phim2 = Button(image=self.login_image, borderwidth=0, highlightthickness=0,
        #                        command=lambda: signup_process.Signup_Process.Trendingnow_process(self))
        # self.login_button.place(x=532.0, y=12.0, width=69.0, height=33.0)

        # self.signup_button_1 = Button(image=self.signup_image_1, borderwidth=0, highlightthickness=0,
        #                        command=lambda: print("signup_button_1 clicked"), relief="flat")
        # self.signup_button_1.place(x=607.0, y=12.0, width=70.0, height=33.0)

        # self.entry_bg_1 = self.canvas.create_image(354.0, 230.0, image=self.entry_image)
        # self.entry_1 = Entry(bd=0, bg="#F8EBD1", fg="#000716", highlightthickness=0)
        # self.entry_1.place(x=268.0, y=214.0, width=172.0, height=30.0)

        # self.entry_bg_2 = self.canvas.create_image(354.0, 293.0, image=self.entry_image)
        # self.entry_2 = Entry(bd=0, bg="#F8EBD1", fg="#000716", highlightthickness=0)
        # self.entry_2.place(x=268.0, y=277.0, width=172.0, height=30.0)

        # self.entry_bg_3 = self.canvas.create_image(354.0, 355.0, image=self.entry_image)
        # self.entry_3 = Entry(bd=0, bg="#F8EBD1", fg="#000716", highlightthickness=0)
        # self.entry_3.place(x=268.0, y=339.0, width=172.0, height=30.0)

        # self.trendingnow_button = Button(image=self.trendingnow_image, borderwidth=0, highlightthickness=0,
        #                        command=lambda: signup_process.Trendingnow_process.trendingnow(self), relief="flat")
        # self.trendingnow_button.place(x=465.0, y=427.0, width=203.0, height=55.0)
        # # The 'Trending Now' button displays the movies that are currently trending
       
        # self.signup_button_2 = Button(image=self.signup_image_2, borderwidth=0, highlightthickness=0,
        #                        command=lambda: signup_process.Signup_Process.signup_button_handle(self))
        # self.signup_button_2.place(x=315.0, y=391.0, width=78.0, height=31.0)
        # self.window.resizable(0, 0)