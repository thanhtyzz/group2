from tkinter import *
import tkinter as tk
from pathlib import Path
import Modules.Login.Login_Process as lgp


class LoginView:
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
        self.window.title("Login")

        self.canvas = Canvas(self.window, bg="#FFFFFF", height=492, width=685, bd=0, highlightthickness=0, relief="ridge")
        self.canvas.place(x=0, y=0)

        assets_path = Path(r"D:\Study\HK2\KY THUAT LAP TRINH\Do_an-cuoi_ki_Nhom2\File\Images\Login")

        self.background_img = PhotoImage(file=assets_path / "Background.png")
        self.login_image_1 = PhotoImage(file=assets_path / "Button_Login_1.png")
        self.signup_image = PhotoImage(file=assets_path / "Button_Signup.png")
        self.entry_image = PhotoImage(file=assets_path / "Textbox.png")
        self.trendingnow_image = PhotoImage(file=assets_path / "Button_Trendingnow.png")
        self.login_image_2 = PhotoImage(file=assets_path / "Button_Login_2.png")

        self.background = self.canvas.create_image(342.0, 246.0, image=self.background_img)

        self.login_button_1 = Button(image=self.login_image_1, borderwidth=0, highlightthickness=0,
                               command=lambda: print("button_1 clicked"), relief="flat")
        self.login_button_1.place(x=610.0, y=12.0, width=64.0, height=33.0)

        self.signup_button = Button(image=self.signup_image, borderwidth=0, highlightthickness=0,
                               command=lambda: lgp.Login_Process.signup_button_handle(self))
        self.signup_button.place(x=532.0, y=12.0, width=69.0, height=33.0)

        self.entry_bg_1 = self.canvas.create_image(354.0, 246.5, image=self.entry_image)
        self.entry_1 = Entry(bd=0, bg="#F8EBD1", fg="#000716", highlightthickness=0)
        self.entry_1.place(x=262.5, y=229.0, width=183.0, height=33.0)

        self.entry_bg_2 = self.canvas.create_image(351.0, 326.5, image=self.entry_image)
        self.entry_2 = Entry(bd=0, bg="#F8EBD1", fg="#000716", highlightthickness=0)
        self.entry_2.place(x=259.5, y=309.0, width=183.0, height=33.0)

        self.canvas.create_rectangle(342.5, 384.5, 435.0, 385.0, fill="#FFFFFF", outline="")
        self.canvas.create_text(343.0, 368.0, anchor="nw", text="forgot password", fill="#FFFFFF",
                                 font=("Poppins Regular", 13 * -1))

        self.trendingnow_button = Button(image=self.trendingnow_image, borderwidth=0, highlightthickness=0,
                               command=lambda: print("button_3 clicked"), relief="flat")
        self.trendingnow_button.place(x=465.0, y=427.0, width=203.0, height=54.0)
        # Nút trending now hiện những bộ phim đang trend

        self.login_button_2 = Button(image=self.login_image_2, borderwidth=0, highlightthickness=0,
                               command=lambda: lgp.Login_Process.confirm_button_handle(self))
        self.login_button_2.place(x=258.0, y=361.0, width=69.0, height=33.0)
        self.window.resizable(0, 0)
