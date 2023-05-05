import Modules.Signup.Sign_up_Process as signup_process
from tkinter import *


class Sign_up_View:
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

        self.window.title("Sign Up")
        self.window.configure(bg="#f6efff")
        self.window.iconphoto(False, PhotoImage(file=f"./Images/Login/home.png"))

        self.canvas = Canvas(self.window, bg="#f6efff", height=768, width=1366, bd=0, highlightthickness=0,
                             relief="ridge")
        self.canvas.place(x=0, y=0)

        self.background_img = PhotoImage(file=f"./Images/SignUp/BG.png")
        self.background = self.canvas.create_image(540, 360, image=self.background_img)

        self.username_entry = Entry(self.window, bd=0, bg="#9E94FF", highlightthickness=0)
        self.username_entry.place(x=335, y=230, height=33, width=390)

        self.password_entry = Entry(self.window, show="*", bd=0, bg="#9E94FF", highlightthickness=0)
        self.password_entry.place(x=335, y=330, height=33, width=390)

        self.reenterpass_entry = Entry(self.window, show="*", bd=0, bg="#9E94FF", highlightthickness=0)
        self.reenterpass_entry.place(x=335, y=430, height=33, width=390)

        self.signup_image = PhotoImage(file=f"./Images/SignUp/Button_Signup.png")
        self.signup_button = Button(self.window, image=self.signup_image, borderwidth=0, highlightthickness=0,
                                    relief="flat", bg="#A8AAFC", activebackground="#A8AAFC",
                                    command=lambda: signup_process.Sign_up_Process.signup_button_handle(self))
        self.signup_button.place(x=460, y=530, width=135, height=45)

        self.signin_image = PhotoImage(file=f"./Images/SignUp/Button_Back.png")
        self.signin_button = Button(self.window, image=self.signin_image, borderwidth=0, highlightthickness=0,
                                    relief="flat", bg="#A4A6FD", activebackground="#A4A6FD",
                                    command=lambda: signup_process.Sign_up_Process.login_button_handle(self))
        self.signin_button.place(x=460, y=585, width=135, height=45)

        self.entry_image = PhotoImage(file=f"./Images/SignUp/Textbox.png")
        self.entry_bg1 = self.canvas.create_image(535, 450, image=self.entry_image)
        self.entry_bg2 = self.canvas.create_image(535, 350, image=self.entry_image)
        self.entry_bg3 = self.canvas.create_image(535, 250, image=self.entry_image)

        self.window.resizable(0, 0)