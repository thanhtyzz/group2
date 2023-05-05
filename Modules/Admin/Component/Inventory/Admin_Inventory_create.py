from tkinter import *
from pathlib import Path
import Api.Admin_Api as Api
import Service.Widget_service as ws
import Modules.Admin.Component.Inventory.Admin_Inventory_process as aip

class Admin_Inventory_create:
    
    @staticmethod
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

        assets_path = Path(r"D:\do-an-cuoi-ki-nhom-2\Images\Admin\Component\Inventory")

        self.background_img = PhotoImage(file=assets_path / "Background.png")
        self.films_image = PhotoImage(file=assets_path / "Button_Films.png")
        self.inventory_image = PhotoImage(file=assets_path / "Button_Inventory.png")
        self.sales_image = PhotoImage(file=assets_path / "Button_Sales.png")
        self.users_image = PhotoImage(file=assets_path / "Button_Users.png")
        self.switch_image = PhotoImage(file=assets_path / "Button_Switch.png")
        self.exit_image = PhotoImage(file=assets_path / "Button_Exit.png")
        self.entry_image_1 = PhotoImage(file=assets_path / "Textbox_1.png")
        self.entry_image_2 = PhotoImage(file=assets_path / "Textbox_2.png")
        self.update_image = PhotoImage(file=assets_path / "Button_Update.png")
        self.remove_image = PhotoImage(file=assets_path / "Button_Remove.png")
        self.search_image = PhotoImage(file=assets_path / "Button_Search.png")
        self.reset_image = PhotoImage(file=assets_path / "Button_Reset.png")

        self.background = self.background_img.create_image(342.0, 246.0, image=self.background_img)

        self.films_button = Button(image=self.films_image, borderwidth=0, highlightthickness=0,
                               command=lambda: self.click_button("films"))
        self.films_button.place(x=10.0, y=124.0, width=97.0, height=37.0)

        self.inventory_button = Button(image=self.inventory_image, borderwidth=0, highlightthickness=0,
                               command=lambda: self.click_button("inventory"))
        self.inventory_button.place(x=118.0, y=125.0, width=102.0, height=35.0)

        self.sales_button = Button(image=self.sales_image, borderwidth=0, highlightthickness=0,
                               command=lambda: self.click_button("sales"))
        self.sales_button.place(x=233.0, y=126.0, width=97.0, height=33.0)

        self.users_button = Button(image=self.users_image, borderwidth=0, highlightthickness=0,
                               command=lambda: self.click_button("users"))
        self.users_button.place(x=349.0, y=126.0, width=97.0, height=33.0)

        self.switch_button = Button(image=self.switch_image, borderwidth=0, highlightthickness=0,
                               command=lambda: self.switch_account())
        self.switch_button.place(x=461.0, y=126.0, width=97.0, height=33.0)

        self.exit_button = Button(image=self.exit_image, borderwidth=0, highlightthickness=0,
                               command=lambda: self.exit_button())
        self.exit_button.place(x=576.0, y=126.0, width=97.0, height=33.0)

        self.update_button = Button(image=self.update_image, borderwidth=0, highlightthickness=0,
                               command=lambda: aip.Admin_Inventory_process.update_button_handle(self))
        self.update_button.place(x=42.0, y=446.0, width=104.0, height=28.0)

        self.canvas.create_rectangle(325.0, 220.0, 657.0, 472.0, fill="#D9D9D9", outline="")
       
        self.entry_1 = self.canvas.create_image(422.0, 195.0, image=self.entry_image_1)
        self.entry_1 = Entry(bd=0, bg="#FCCBCB", fg="#000716", highlightthickness=0)
        self.entry_1.place(x=322.0, y=185.0, width=200.0, height=18.0)

        self.entry_2 = self.canvas.create_image(216.0, 399.0, image=self.entry_image_2)
        self.entry_2 = Entry(bd=0, bg="#D9D9D9", fg="#000716", highlightthickness=0)
        self.entry_2.place( x=141.0, y=386.0, width=150.0, height=24.0)

        self.entry_3 = self.canvas.create_image(216.0, 361.0, image=self.entry_image_2)
        self.entry_3 = Entry(bd=0, bg="#D9D9D9", fg="#000716", highlightthickness=0)
        self.entry_3.place(x=141.0, y=348.0, width=150.0, height=24.0)

        self.entry_4 = self.canvas.create_image(216.0, 323.0, image=self.entry_image_2)
        self.entry_4 = Entry(bd=0, bg="#D9D9D9", fg="#000716", highlightthickness=0)
        self.entry_4.place(x=141.0, y=310.0, width=150.0, height=24.108795166015625)

        self.entry_5 = self.canvas.create_image(400.5, 246.0, image=self.entry_image_2)
        self.entry_5 = Entry(bd=0, bg="D9D9D9", fg="#000716", highlightthickness=0)
        self.entry_5.place(x=141.0, y=272.0, width=150.0, height=24.108795166015625)

        self.entry_6 = self.canvas.create_image(400.5, 209.0, image=self.entry_image_2)
        self.entry_6 = Entry(bd=0, bg="#D9D9D9", fg="#000716", highlightthickness=0)
        self.entry_6.place(x=141.0, y=234.0, width=150.0, height=24.108795166015625)

        self.entry_7 = self.canvas.create_image(400.5, 209.0, image=self.entry_image_2)
        self.entry_7 = Entry(bd=0, bg="#D9D9D9", fg="#000716", highlightthickness=0)
        self.entry_7.place(x=141.0, y=196.0, width=150.0, height=24.108795166015625)

        self.canvas.create_rectangle(15.0, 181.0, 308.0, 426.0, fill="#4C4A4A", outline="")
    
        self.update_button = Button(image=self.update_image, borderwidth=0, highlightthickness=0,
                               command=lambda: aip.Admin_Inventory_process.update_button_handle(self))
        self.update_button.place(x=42.0, y=446.0, width=104.0, height=28.0)

        self.remove_button = Button(image=self.remove_image, borderwidth=0, highlightthickness=0,
                               command=lambda: aip.Admin_Inventory_process.remove_button_handle(self))
        self.remove_button.place(x=176.0, y=446.0, width=104.0, height=28.0)

        self.search_button = Button(image=self.search_image, borderwidth=0, highlightthickness=0,
                               command=lambda: aip.Admin_Inventory_process.search_button_handle(self))
        self.search_button.place(x=532.0, y=185.0, width=61.0, height=21.0)

        self.reset_button = Button(image=self.reset_image, borderwidth=0, highlightthickness=0,
                               command=lambda: aip.Admin_Inventory_process.reset_button_handle(self))
        self.reset_button.place(x=603.0, y=185.0, width=61.0, height=21.0)
        self.window.resizable(0, 0)

    @staticmethod
    def generate_inventory_table(obj):
        def clickprodtable(event):
            # get selected film
            cur = obj.tree.selection()
            cur = obj.tree.item(cur)
            try:
                obj.selected_film = cur['values']
                obj.film.set(cur['values'][1])
                obj.genre.set(cur['values'][2])
                obj.showtime.set(cur['values'][3])
                obj.price.set(cur['values'][4])
                obj.current_stock.set(cur['values'][5])
            except:
                pass

        # create tree view
        obj.tree = ttk.Treeview(obj.tableframe, columns = ('ID', 'Name', 'Genre',
                                                         'Showtime', 'Price', 'Stock'))
        obj.tree.heading('#0')
        obj.tree.heading('#1', text ='ID') 
        obj.tree.heading('#2', text = 'Name')
        obj.tree.heading('#3', text = 'Genre')
        obj.tree.heading('#4', text = 'Showtime')
        obj.tree.heading('#5', text = 'Price')
        obj.tree.heading('#6', text = 'Stock')

        obj.tree.column('#0', width = 0)
        obj.tree.column('#1', width = 40)
        obj.tree.column('#2', width = 100)
        obj.tree.column('#3', width = 170)
        obj.tree.column('#4', width = 110)
        obj.tree.column('#5', width = 110)
        obj.tree.column('#6', width = 70)
        obj.tree.bind("<<TreeviewSelect>>", clickprodtable)
        obj.tree.grid(row = 1, column = 0, columnspan = 6)

        # create scroll bar
        obj.scrollbary = ttk.Scrollbar(obj.tableframe, orient = VERTICAL, command = obj.tree.yview)
        obj.scrollbary.grid(row = 1, column = 6)

        api = Api.Admin_Api()
        films = api.get_all_warehouse_data()

        for film in films: 
            obj.tree.insert('', 'end', values = (film['film_id'], film['film'], film['Genre'], film['Showtime'], film['Price'], film['Stock']))
