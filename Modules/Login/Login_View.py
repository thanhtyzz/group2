from tkinter import *
import tkinter as tk
import Modules.Login.Login_Process as lgp


class Login_View:

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
        self.window.configure(bg = "#FFFFFF")
        self.window.title("Login")
        self.window.iconphoto(False, PhotoImage(file = f"./Images/Login/home.png"))

        self.canvas = Canvas(self.window, bg = "#FFFFFF", height = 720, width = 1080, bd = 0, highlightthickness = 0, relief = "ridge")
        self.canvas.place(x = 0, y = 0)

        self.background_img = PhotoImage(file = f"./Images/Login/BG.png")
        self.background = self.canvas.create_image(545, 360, image = self.background_img)

        self.login_image = PhotoImage(file = f"./Images/Login/Button_Login.png")
        self.login_button = Button(image = self.login_image, borderwidth = 0,
                                   highlightthickness = 0, relief = "flat", bg = "#ffffff", activebackground = "#ffffff", command = lambda: lgp.Login_Process.confirm_button_handle(self))
        self.login_button.place(x = 190, y = 485, width = 135, height = 45)

        self.signup_image = PhotoImage(file = f"./Images/Login/Button_Signup.png")
        self.signup_button = Button(image = self.signup_image, borderwidth = 0, highlightthickness = 0, relief = "flat", bg = "#B6B3FB", activebackground = "#B6B3FB", command = lambda: lgp.Login_Process.signup_button_handle(self))
        self.signup_button.place(x = 765, y = 430, width = 135, height = 50)

        self.entry_img = PhotoImage(file = f"./Images/Login/Textbox.png")
        self.entry_bg1 = self.canvas.create_image(260, 315, image = self.entry_img)
        self.entry_bg2 = self.canvas.create_image(260, 423, image = self.entry_img)

        self.name_entry = Entry(self.window, bd = 0, bg="#C9C3FB", highlightthickness = 0)
        self.name_entry.place(x = 110, y = 297, width = 300, height = 28)

        self.password_entry = Entry(self.window, show = "*", bd = 0, bg = "#C9C3FB", highlightthickness = 0)
        self.password_entry.place(x = 110, y = 405, width = 300, height = 28)
        self.window.resizable(FALSE, FALSE)