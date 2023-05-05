from tkinter import *
from pathlib import Path
import Service.Widget_service as ws
import Api.Admin_Api as Api 
import Modules.Admin.Component.Users.Admin_User_process as aup
from tkinter import messagebox as mbox


class Admin_Users_create:
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

        assets_path = Path(r"D:\do-an-cuoi-ki-nhom-2\Images\Admin\Component\Users")

        self.background_img = PhotoImage(file=assets_path / "Background.png")
        self.films_image = PhotoImage(file=assets_path / "Button_Films.png")
        self.inventory_image = PhotoImage(file=assets_path / "Button_Inventory.png")
        self.sales_image = PhotoImage(file=assets_path / "Button_Sales.png")
        self.users_image = PhotoImage(file=assets_path / "Button_Users.png")
        self.switch_image = PhotoImage(file=assets_path / "Button_Switch.png")
        self.exit_image = PhotoImage(file=assets_path / "Button_Exit.png")
        self.entry_image = PhotoImage(file=assets_path / "Textbox.png")
        self.update_image = PhotoImage(file=assets_path / "Button_Update.png")
        self.delete_image = PhotoImage(file=assets_path / "Button_Delete.png")
        self.create_image = PhotoImage(file=assets_path / "Button_Create.png")

        self.background = self.background_img.create_image(342.0, 246.0, image=self.background_img)

        self.films_button = Button(image=self.films_image, borderwidth=0, highlightthickness=0,
                               command=lambda: aup.Admin_User_Process.films_button_handle(self))
        self.films_button.place(x=10.0, y=124.0, width=97.0, height=37.0)

        self.inventory_button = Button(image=self.inventory_image, borderwidth=0, highlightthickness=0,
                               command=lambda: aup.Admin_User_Process.inventory_button_handle(self))
        self.inventory_button.place(x=118.0, y=125.0, width=102.0, height=35.0)

        self.sales_button = Button(image=self.sales_image, borderwidth=0, highlightthickness=0,
                               command=lambda: aup.Admin_User_Process.sales_button_handle(self))
        self.sales_button.place(x=233.0, y=126.0, width=97.0, height=33.0)

        self.users_button = Button(image=self.users_image, borderwidth=0, highlightthickness=0,
                               command=lambda: aup.Admin_User_Process.users_button_handle(self))
        self.users_button.place(x=349.0, y=126.0, width=97.0, height=33.0)

        self.switch_button = Button(image=self.switch_image, borderwidth=0, highlightthickness=0,
                               command=lambda: aup.Admin_User_Process.switch_button_handle(self))
        self.switch_button.place(x=461.0, y=126.0, width=97.0, height=33.0)

        self.exit_button = Button(image=self.exit_image, borderwidth=0, highlightthickness=0,
                               command=lambda: aup.Admin_User_Process.exit_button_handle(self))
        self.exit_button.place(x=576.0, y=126.0, width=97.0, height=33.0)

        self.canvas.create_rectangle(346.0, 178.0, 639.0, 469.0, fill="#D9D9D9", outline="")
       
        self.entry_1 = self.canvas.create_image(422.0, 195.0, image=self.entry_image)
        self.entry_1 = Entry(bd=0, bg="#D9D9D9", fg="#000716", highlightthickness=0)
        self.entry_1.place( x=141.6767578125, y=291.0, width=154.42425537109375, height=30.0)

        self.entry_2 = self.canvas.create_image(216.0, 399.0, image=self.entry_image)
        self.entry_2 = Entry(bd=0, bg="#D9D9D9", fg="#000716", highlightthickness=0)
        self.entry_2.place( x=141.6767578125, y=245.0, width=154.42425537109375, height=30.0)

        self.entry_3 = self.canvas.create_image(216.0, 361.0, image=self.entry_image)
        self.entry_3 = Entry(bd=0, bg="#D9D9D9", fg="#000716", highlightthickness=0)
        self.entry_3.place( x=141.6767578125, y=199.0, width=154.42425537109375, height=30.0)

    

        self.canvas.create_rectangle(47.0, 178.0, 319.02545166015625, 469.0, fill="#4C4A4A", outline="")
    
        self.update_button = Button(image=self.update_image, borderwidth=0, highlightthickness=0,
                               command=lambda: aup.Admin_User_Process.update_button_handle(self)) 
        self.update_button.place(x=91.0, y=343.0, width=47.0, height=25.0)

        self.delete_button = Button(image=self.delete_image, borderwidth=0, highlightthickness=0,
                               command=lambda: aup.Admin_User_Process.delete_button_handle(self)) 
        self.delete_button.place(x=152.0, y=343.0, width=47.0, height=25.0)

        self.create_button = Button(image=self.create_image, borderwidth=0, highlightthickness=0,
                               command=lambda: aup.Admin_User_create.create_user(self))
        self.create_button.place(x=213.0, y=343.0, width=80.0, height=25.0)


class create_user:
    def __init__(self):
        self.window = Tk()
        # get screen width and height
        self.screen_width = self.window.winfo_screenwidth()
        self.screen_height = self.window.winfo_screenheight()

        # set window width and height
        self.window_width = 366
        self.window_height = 377
        # set window position
        self.window.geometry("%dx%d+%d+%d" % (self.window_width, self.window_height,
                             (self.screen_width - self.window_width) / 2, (self.screen_height - self.window_height) / 2))
        self.window.configure(bg="#FFFFFF")
        self.window.title("Create new user")

        self.canvas = Canvas(self.window, bg="#FFFFFF", height=377, width=366, bd=0, highlightthickness=0, relief="ridge")
        self.canvas.place(x=0, y=0)



@staticmethod 
def create_user(obj): 
        window = Tk()
        window.title("Create new user") 
        window.geometry("366x377") 
        window.resizable(False, False) 
        window.configure(background = "#FFFFFF") 

        # create entry 
        entry_username = Entry(window) 
        entry_username.place(x = 100, y = 0, width = 200, height = 50) 

        # create entry
        entry_password = Entry(window) 
        entry_password.place(x = 100, y = 70, width = 200, height = 50) 

        # create entry
        entry_role = ws.mycombobox(window)
        entry_role.set_completion_list(["Admin", "User"])
        entry_role.place(x = 100, y = 140, width = 200, height = 50)

        # create create button 
        button_create = Button(window, text = "Create",command = lambda: add_new_user(entry_username, entry_password, entry_role))
        button_create.place(x = 100, y = 200, width = 100, height = 50) 
        
        #exit button 
        button_exit = Button(window, text = "Exit", command = window.destroy) 
        button_exit.place(x = 200, y = 200, width = 100, height = 50) 

        def add_new_user(entry_username, entry_password, entry_role):
            username = entry_username.get()
            password = entry_password.get()
            roles = entry_role.get()
            
            if username == "" or password == "" or roles == "": 
                mbox.showerror("Error", "PLease fill in all fields")
                return
            data = {
                "username": username, 
                "password": password, 
                "roles": roles
            }
            api = Api.Admin_Api()
            check = api.add_new_user(data)
            if check == -1: 
                mbox.showerror("Error", "User already existed")
            else: 
                mbox.showinfo("Success", "New User created")
                obj.tree.insert('', 'end', values=(username, password, roles))



        
