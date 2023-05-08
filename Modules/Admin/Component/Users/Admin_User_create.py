from tkinter import *
from tkinter import ttk
from pathlib import Path
from PIL import ImageTk, Image
from tkinter import messagebox as mbox
import Service.Widget_service as ws
import Api.Admin_Api as Api 
import Modules.Admin.Component.Users.Admin_User_process as aup

class Admin_User_create:
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

    @staticmethod
    def generate_users(obj):
        # Xóa các frame hiện tại
        for frame in obj.allframes:
            frame.destroy()
        obj.allframes = []

        # Tạo frame mới
        obj.formframe1 = Frame(obj.window, bg='#4C4A4A')
        obj.formframe1.place(x=30, y=175, width=280, height=300)
        obj.allframes.append(obj.formframe1)

        obj.formframe2 = Frame(obj.window, bg='pink')
        obj.formframe2.place(x=335, y=175, width=320, height=300)
        obj.allframes.append(obj.formframe2)


        # Tạo các thành phần trong frame
        Admin_User_create.generate_users_button(obj)
        Admin_User_create.generate_users_form(obj)
        Admin_User_create.generate_users_table(obj)

    @staticmethod
    def generate_users_form(obj):
        # create form in form frame
        
        assets_path = Path(r"D:\do-an-cuoi-ki-nhom-2\Images\Admin\Users")
        
        obj.username = StringVar()
        obj.username.get()

        image_path = r"D:\do-an-cuoi-ki-nhom-2\Images\Admin\Users\image_1.png"
        image = Image.open(image_path)
        image = image.resize((85, 140))
        photo = ImageTk.PhotoImage(image)
        label = Label(obj.formframe1, image=photo)
        label.image = photo
        label.place(x=0.0, y=0.0)
        label.configure(background='#4C4A4A')

        obj.entry_image = PhotoImage(file=assets_path / "entry_1.png")
        obj.username_entry = Entry(obj.formframe1, bd=0, bg="#D9D9D9", fg="#000716", highlightthickness=0, textvariable = obj.username)
        obj.username_entry.place(x=105.0, y=20.0, width=155.0, height=30.0)

        obj.password_entry = Entry(obj.formframe1, bd=0, bg="#D9D9D9", fg="#000716", highlightthickness=0)
        obj.password_entry.place(x=105.0, y=65.0, width=155.0, height=30.0)

        obj.role_entry = Entry(obj.formframe1, bd=0, bg="#D9D9D9", fg="#000716", highlightthickness=0)
        obj.role_entry.place(x=105.0, y=110.0, width=155.0, height=30.0)

    @staticmethod
    def generate_users_button(obj):
        assets_path = Path(r"D:\do-an-cuoi-ki-nhom-2\Images\Admin\Users")

        obj.update_image = PhotoImage(file=assets_path / "button_9.png")
        obj.delete_image = PhotoImage(file=assets_path / "button_8.png")
        obj.create_image = PhotoImage(file=assets_path / "button_7.png")

        obj.update_button = Button(image=obj.update_image, borderwidth=0, highlightthickness=0,
                               command=lambda: aup.Admin_User_Process.update_button_handle(obj))
        obj.update_button.place(x=70.0, y=335.0, width=50.0, height=28.0)

        obj.delete_button = Button(image=obj.delete_image, borderwidth=0, highlightthickness=0,
                               command=lambda: aup.Admin_User_Process.delete_button_handle(obj))
        obj.delete_button.place(x=135.0, y=335.0, width=50.0, height=28.0)

        obj.create_button = Button(image=obj.create_image, borderwidth=0, highlightthickness=0,
                               command=lambda: aup.Admin_User_Process.create_button_handle(obj))
        obj.create_button.place(x=200.0, y=335.0, width=80.0, height=28.0)

    @staticmethod
    def generate_users_table(obj):
        def clickprodtable(event):
            # get selected film
            cur = obj.tree.selection()
            cur = obj.tree.item(cur)
            try:
                obj.selected_username = cur['values']
                obj.user.set(cur['values'][1])
                obj.password.set(cur['values'][2])
                obj.role.set(cur['values'][3])
            except:
                pass
    
        # create tree view
        obj.tree = ttk.Treeview(obj.formframe2, columns=('Username', 'Password', 'Roles'))
        obj.tree.heading('#0')
        obj.tree.heading('#1', text='Username')
        obj.tree.heading('#2', text='Password')
        obj.tree.heading('#3', text='Roles')

        obj.tree.column('#0', width=0)
        obj.tree.column('#1', width=100)
        obj.tree.column('#2', width=147)
        obj.tree.column('#3', width=70)
        obj.tree.bind("<<TreeviewSelect>>", clickprodtable)

        # create scroll bar
        obj.scrollbary = ttk.Scrollbar(obj.formframe2, orient=VERTICAL, command=obj.tree.yview)

        obj.tree.pack(side=RIGHT, fill=BOTH)
        obj.scrollbary.pack(side=RIGHT, fill=Y)

        api = Api.Admin_Api()
        users = api.get_all_users_data()

        for user in users:
            obj.tree.insert('', 'end', values=(user['Username'], user['Password'], user['Roles']))
            
        return obj.tree
