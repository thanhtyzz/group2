from tkinter import ttk
from tkinter import *
from pathlib import Path
import Api.Admin_Api as Api
import Service.Widget_service as ws
import Modules.Admin.Component.Inventory.Admin_Inventory_process as aip
import Modules.Admin.Component.Admin_Main_View as adv
from PIL import ImageTk, Image


class Admin_Inventory_create:
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
        self.window.configure(bg="#4C4A4A")
        self.window.title("Admin")

        self.canvas = Canvas(self.window, bg="#4C4A4A", height=492, width=685, bd=0, highlightthickness=0, relief="ridge")
        self.canvas.place(x=0, y=0)

    @staticmethod
    def generate_inventory(obj):
        # Xóa các frame hiện tại
        for frame in obj.allframes:
            frame.destroy()
        obj.allframes = []

        # Tạo frame mới
        obj.formframe1 = Frame(obj.window, bg='#4C4A4A')
        obj.formframe1.place(x=15, y=170, width=300, height=250)
        obj.allframes.append(obj.formframe1)

        obj.formframe2 = Frame(obj.window, bg='#FFFFFF')
        obj.formframe2.place(x=325, y=165, width=350, height=50)
        obj.allframes.append(obj.formframe2)

        obj.formframe3 = Frame(obj.window, bg='pink')
        obj.formframe3.place(x=325, y=215, width=350, height=260)
        obj.allframes.append(obj.formframe3)

        obj.buttonframe = Frame(obj.window, bg="#4C4A4A")
        obj.buttonframe.place(x=315, y=630, width=450, height=65)
        obj.allframes.append(obj.buttonframe)

        # Tạo các thành phần trong frame
        Admin_Inventory_create.generate_inventory_button(obj)
        Admin_Inventory_create.generate_inventory_form(obj)
        Admin_Inventory_create.generate_inventory_entry(obj)
        Admin_Inventory_create.generate_inventory_table(obj)

    @staticmethod
    def generate_inventory_form(obj):
        # create form in form frame
        obj.product_id = StringVar()

        obj.product_id.get()
        
        assets_path = Path(r"D:\do-an-cuoi-ki-nhom-2\Images\Admin\Inventory")
        
        obj.background_img = PhotoImage(file=assets_path / "Background.png")
        obj.background = obj.canvas.create_image(342.0, 246.0, image=obj.background_img)

        obj.entry_image = PhotoImage(file=assets_path / "Textbox_2.png")
        obj.film_entry = Entry(obj.formframe1, bd=0, bg="#D9D9D9", fg="#000716", highlightthickness=0, textvariable = obj.product_id)
        obj.film_entry.place(x=130.0, y=10.0, width=162.0, height=24.0)

        obj.film_entry = Entry(obj.formframe1, bd=0, bg="#D9D9D9", fg="#000716", highlightthickness=0)
        obj.film_entry.place(x=130.0, y=50.0, width=162.0, height=24.0)

        obj.genre_entry = Entry(obj.formframe1, bd=0, bg="#D9D9D9", fg="#000716", highlightthickness=0)
        obj.genre_entry.place(x=130.0, y=90.0, width=162.0, height=24.0)

        obj.showtime_entry = Entry(obj.formframe1, bd=0, bg="#D9D9D9", fg="#000716", highlightthickness=0)
        obj.showtime_entry.place(x=130.0, y=130.0, width=162.0, height=24.0)

        obj.price_entry = Entry(obj.formframe1, bd=0, bg="#D9D9D9", fg="#000716", highlightthickness=0)
        obj.price_entry.place(x=130.0, y=170.0, width=162.0, height=24.0)

        obj.stock_entry = Entry(obj.formframe1, bd=0, bg="#D9D9D9", fg="#000716", highlightthickness=0)
        obj.stock_entry.place(x=130.0, y=210.0, width=162.0, height=24.0)

        obj.add_stock_entry = Entry(obj.formframe1, bd=0, bg="#D9D9D9", fg="#000716", highlightthickness=0)
        obj.add_stock_entry.place(x=130.0, y=210.0, width=162.0, height=24.0)

        image_path = "D:\do-an-cuoi-ki-nhom-2\Images\Admin\Inventory\letter.png"
        image = Image.open(image_path)
        image = image.resize((110, 245))
        photo = ImageTk.PhotoImage(image)
        label = Label(obj.formframe1, image=photo)
        label.image = photo
        label.place(x=0.0, y=0.0)
        label.configure(background='#4C4A4A')

    @staticmethod
    def generate_inventory_entry(obj): 
        # create form in form frame
        obj.product_id = StringVar()

        obj.product_id.get()
        assets_path = Path(r"D:\do-an-cuoi-ki-nhom-2\Images\Admin\Inventory")
        obj.entry_image = PhotoImage(file=assets_path / "Textbox_1.png")
        obj.film_entry = Entry(obj.formframe2, bd=0, bg="pink", fg="#000716", highlightthickness=0, textvariable = obj.product_id)
        obj.film_entry.place(x=2.0, y=10.0, width=180.0, height=24.0)
        
    @staticmethod
    def generate_inventory_button(obj):
        assets_path = Path(r"D:\do-an-cuoi-ki-nhom-2\Images\Admin\Inventory")

        obj.update_image = PhotoImage(file=assets_path / "Button_Update.png")
        obj.remove_image = PhotoImage(file=assets_path / "Button_Remove.png")
        obj.search_image = PhotoImage(file=assets_path / "Button_Search.png")
        obj.reset_image = PhotoImage(file=assets_path / "Button_Reset.png")

        obj.update_button = Button(image=obj.update_image, borderwidth=0, highlightthickness=0,
                               command=lambda: aip.Admin_Inventory_Process.update_button_handle(obj))
        obj.update_button.place(x=50.0, y=430.0, width=104.0, height=28.0)

        obj.remove_button = Button(image=obj.remove_image, borderwidth=0, highlightthickness=0,
                               command=lambda: aip.Admin_Inventory_Process.remove_button_handle(obj))
        obj.remove_button.place(x=170.0, y=430.0, width=104.0, height=28.0)

        obj.search_button = Button(image=obj.search_image, borderwidth=0, highlightthickness=0,
                               command=lambda: aip.Admin_Inventory_Process.search_button_handle(obj))
        obj.search_button.place(x=520.0, y=174.5, width=65.0, height=24.0)

        obj.reset_button = Button(image=obj.reset_image, borderwidth=0, highlightthickness=0,
                               command=lambda: aip.Admin_Inventory_Process.reset_button_handle(obj))
        obj.reset_button.place(x=595.0, y=174.5, width=65.0, height=24.0)


    @staticmethod
    def generate_inventory_table(obj):
        def clickprodtable(event):
            # get selected film
            cur = obj.tree.selection()
            cur = obj.tree.item(cur)
            try:
                obj.selected_film = cur['values']
                obj.film_name.set(cur['values'][1])
                obj.genre.set(cur['values'][2])
                obj.showtime.set(cur['values'][3])
                obj.price.set(cur['values'][4])
                obj.stock.set(cur['values'][5])
            except:
                pass
    
        # create tree view
        obj.tree = ttk.Treeview(obj.formframe3, columns=('Film_ID', 'Film', 'Genre', 'Showtime', 'Price', 'Stock'))
        obj.tree.heading('#0')
        obj.tree.heading('#1', text='Film_ID')
        obj.tree.heading('#2', text='Film')
        obj.tree.heading('#3', text='Genre')
        obj.tree.heading('#4', text='Showtime')
        obj.tree.heading('#5', text='Price')
        obj.tree.heading('#6', text='Stock')

        obj.tree.column('#0', width=0)
        obj.tree.column('#1', width=50)
        obj.tree.column('#2', width=100)
        obj.tree.column('#3', width=95)
        obj.tree.column('#4', width=70)
        obj.tree.column('#5', width=40)
        obj.tree.column('#6', width=58)
        obj.tree.bind("<<TreeviewSelect>>", clickprodtable)

        # create scroll bar
        obj.scrollbary = ttk.Scrollbar(obj.tableframe, orient=VERTICAL, command=obj.tree.yview)

        obj.tree.pack(side=RIGHT, fill=BOTH)
        obj.scrollbary.pack(side=RIGHT, fill=Y)

        api = Api.Admin_Api()
        products = api.get_all_warehouse_data()

        for product in products:
            obj.tree.insert('', 'end', values=(product['Film_ID'], product['Film'], product['Genre'], product['Showtime'], product['Price'], product['Stock']))
            
        return obj.tree

