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

class Trendingnow_View:
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
        self.window.title("TrendingNow")
        self.canvas = Canvas(self.window, bg="#FFFFFF", height=720, width=1080, bd=0, highlightthickness=0, relief="ridge")
        self.canvas.place(x=0, y=0)

        assets_path = Path(r"D:\do-an-cuoi-ki-nhom-2\Images\Trendingnow")

        self.phim1 = PhotoImage(file=assets_path / "image_1.png")
        self.phim2 = PhotoImage(file=assets_path / "image_2.png")
        self.phim3 = PhotoImage(file=assets_path / "image_3.png")
        self.phim4 = PhotoImage(file=assets_path / "image_4.png")
        self.phim5 = PhotoImage(file=assets_path / "image_5.png")
        self.phim6 = PhotoImage(file=assets_path / "image_6.png")
        self.phim7 = PhotoImage(file=assets_path / "image_7.png")
        self.phim8 = PhotoImage(file=assets_path / "image_8.png")
        self.phim9 = PhotoImage(file=assets_path / "image_9.png")
        self.phim10 = PhotoImage(file=assets_path / "image_10.png")
        self.phim11 = PhotoImage(file=assets_path / "image_11.png")
        self.phim12 = PhotoImage(file=assets_path / "image_12.png")

        self.vitri1 = self.canvas.create_image(85.0, 170.0, image=self.phim1)
        self.vitri2 = self.canvas.create_image(265.0, 170.0, image=self.phim2)
        self.vitri3 = self.canvas.create_image(445.0, 170.0, image=self.phim3)
        self.vitri4 = self.canvas.create_image(625.0, 170.0, image=self.phim4)
        self.vitri5 = self.canvas.create_image(805.0, 170.0, image=self.phim5)
        self.vitri6 = self.canvas.create_image(985.0, 170.0, image=self.phim6)
        self.vitri7 = self.canvas.create_image(985.0, 540.0, image=self.phim7)
        self.vitri8 = self.canvas.create_image(805.0, 540.0, image=self.phim8)
        self.vitri9 = self.canvas.create_image(625.0, 540.0, image=self.phim9)
        self.vitri10 = self.canvas.create_image(445.0, 540.0, image=self.phim10)
        self.vitri11 = self.canvas.create_image(265.0, 540.0, image=self.phim11)
        self.vitri12 = self.canvas.create_image(85.0, 540.0, image=self.phim12)

        self.button1 = Button(image=self.phim1, borderwidth=0, highlightthickness=0,
                               command=lambda: signup_process.Trendingnow_process.phim_button(self))
        self.button1.place(x=0.0, y=0.0, width=170.0, height=340.0)

class Infor_View:
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
        self.window.title("Information")
        self.canvas = Canvas(self.window, bg="#FFFFFF", height=492, width=685, bd=0, highlightthickness=0, relief="ridge")
        self.canvas.place(x=0, y=0)