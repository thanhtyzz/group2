from tkinter import *
import Modules.User.Component.Films.User_Films_create as uic
import Modules.User.Component.Buytickets.User_Buytickets_create as usc
from tkinter import messagebox
import Modules.Login.Login_View as lgv


class User_Main_View:

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

        self.window.title("User")
        self.window.configure(bg="#AFA4F9")
        self.window.iconphoto(False, PhotoImage(file=f"./Images/User/MainPage/UserIcon.png"))

        self.allframes = []

        self.canvas = Canvas(self.window, bg="#FFFFFF", height=720, width=1080, bd=0, highlightthickness=0,
                             relief="ridge")
        self.canvas.place(x=0, y=0)

        self.background_img = PhotoImage(file=f"./Images/User/MainPage/BG_MainPage.png")
        self.background = self.canvas.create_image(540, 360, image=self.background_img)

        self.invoice_image = PhotoImage(file=f"./Images/User/MainPage/Button_Invoice.png")
        self.invoice_button = Button(self.window, image=self.invoice_image, borderwidth=0, highlightthickness=0,
                                     relief="flat", bg="#FFFFFF", activebackground="#FFFFFF",
                                     command=lambda: self.click_button("shop"))
        self.invoice_button.place(x=80, y=160, width=185, height=60)

        self.items_image = PhotoImage(file=f"./Images/User/MainPage/Button_Items.png")
        self.items_button = Button(self.window, image=self.items_image, borderwidth=0, highlightthickness=0,
                                   relief="flat", bg="#FFFFFF", activebackground="#FFFFFF",
                                   command=lambda: self.click_button("items"))
        self.items_button.place(x=325, y=160, width=185, height=60)

        self.signout_image = PhotoImage(file=f"./Images/User/MainPage/Button_Signout.png")
        self.signout_button = Button(self.window, image=self.signout_image, borderwidth=0, highlightthickness=0,
                                     relief="flat", bg="#FFFFFF", activebackground="#FFFFFF",
                                     command=self.change_account)
        self.signout_button.place(x=570, y=160, width=185, height=60)

        self.quit_image = PhotoImage(file=f"./Images/User/MainPage/Button_Quit.png")
        self.quit_button = Button(self.window, image=self.quit_image, borderwidth=0, highlightthickness=0,
                                  relief="flat", bg="#FFFFFF", activebackground="#FFFFFF",
                                  command=self.quit_button_click)
        self.quit_button.place(x=815, y=160, width=185, height=60)
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
        if button == "items":
            uic.User_Items_create.generate_items(self)
        elif button == "shop":
            usc.User_Shop_create.generate_shop(self)