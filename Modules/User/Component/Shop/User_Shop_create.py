from tkinter import *
from pathlib import Path
import Modules.User.Component.Buytickets.User_Buytickets_process as usp
from tkinter import ttk


class User_Buytickets_create:
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
        self.window.title("Buytickets")

        self.canvas = Canvas(self.window, bg="#FFFFFF", height=492, width=685, bd=0, highlightthickness=0, relief="ridge")
        self.canvas.place(x=0, y=0)

        assets_path = Path(r"D:\Study\HK2\KY THUAT LAP TRINH\Do_an-cuoi_ki_Nhom2\File\Images\Login")

        self.background_img = PhotoImage(file=assets_path / "Background.png")
        self.entry_image_1 = PhotoImage(file=assets_path / "Textbox_1.png")
        self.entry_image_2 = PhotoImage(file=assets_path / "Textbox_2.png")
        self.process_image = PhotoImage(file=assets_path / "Button_Process.png")
        self.addtocart_image = PhotoImage(file=assets_path / "Button_Addtocart.png")
        self.remove_image = PhotoImage(file=assets_path / "Button_Remove.png")

        self.background = self.canvas.create_image(342.0, 246.0, image=self.background_img)

        self.process_button = Button(image=self.process_image, borderwidth=0, highlightthickness=0,
                               command=lambda: usp.User_Buytickets_process.process_cart_handle(obj))
        self.process_button.place(x=358.0, y=343.0, width=70.0, height=88.0)

        self.addtocart_button = Button(image=self.addtocart_image, borderwidth=0, highlightthickness=0,
                               command=lambda: usp.User_Buytickets_process.add_to_cart(obj))
        self.addtocart_button.place(x=446.0, y=406.0, width=95.0, height=25.0)

        self.remove_button = Button(image=self.remove_image, borderwidth=0, highlightthickness=0,
                               command=lambda: usp.User_Buytickets_process.remove_from_cart(obj))
        self.remove_button.place(x=559.0, y=406.0, width=95.0, height=25.0)

        self.entry_bg_1 = self.canvas.create_image(231.0, 459.0, image=self.entry_image_1)
        self.entry_1 = Entry(bd=0, bg="#D9D9D9", fg="#000716", highlightthickness=0)
        self.entry_1.place(x=146.0, y=448.0, width=170.0, height=20.0)

        self.entry_bg_2 = self.canvas.create_image(231.0, 425.0, image=self.entry_image_1)
        self.entry_2 = Entry(bd=0, bg="#D9D9D9", fg="#000716", highlightthickness=0)
        self.entry_2.place(x=146.0, y=414.0, width=170.0, height=20.0)

        self.entry_bg_3 = self.canvas.create_image(231.0, 389.0, image=self.entry_image_1)
        self.entry_1 = Entry(bd=0, bg="#D9D9D9", fg="#000716", highlightthickness=0)
        self.entry_1.place(x=146.0, y=378.0, width=170.0, height=20.0)

        self.entry_bg_4 = self.canvas.create_image(231.0, 354.0, image=self.entry_image_1)
        self.entry_2 = Entry(bd=0, bg="#D9D9D9", fg="#000716", highlightthickness=0)
        self.entry_2.place(x=146.0, y=343.0, width=170.0, height=20.0)

        self.entry_bg_5 = self.canvas.create_image(541.0, 455.0, image=self.entry_image_1)
        self.entry_1 = Entry(bd=0, bg="#D9D9D9", fg="#000716", highlightthickness=0)
        self.entry_1.place(x=461.0, y=444.0, width=160.0, height=20.0)

        self.entry_bg_6 = self.canvas.create_image(590.5, 383.0, image=self.entry_image_2)
        self.entry_2 = Entry(bd=0, bg="#D9D9D9", fg="#000716", highlightthickness=0)
        self.entry_2.place(x=519.0, y=372.0, width=143.0, height=20.0)

        self.entry_bg_7 = self.canvas.create_image(590.5, 354.0, image=self.entry_image_2)
        self.entry_1 = Entry(bd=0, bg="#D9D9D9", fg="#000716", highlightthickness=0)
        self.entry_1.place(x=519.0, y=343.0, width=143.0, height=20.0)

        self.canvas.create_rectangle(27.0, 187.0, 664.0, 321.0, fill="#D9D9D9", outline="")
        self.canvas.create_rectangle(15.0, 33.0, 337.0, 478.0, fill="#4C4A4A", outline="")
        self.canvas.create_rectangle(348.0, 33.0, 670.0, 478.0, fill="#4C4A4A", outline="")

        self.window.resizable(0, 0)

    @staticmethod
    def generate_buytickets_table(obj):
        def clickprodtable(event):
            # get selected product
            cur = obj.tree.selection()
            cur = obj.tree.item(cur)
            try:
                obj.selected_product = cur['values']
                obj.product_id.set(cur['values'][0])
                obj.product_name.set(cur['values'][1])
                obj.quantity.set(cur['values'][2])
                obj.price.set(cur['values'][3])
            except:
                pass

        # create tree view
        obj.tree = ttk.Treeview(obj.tableframe, columns = (
            "Product_id", "Product_name", "Quantity", "Price"), height = 20)
        obj.tree.heading("#0")
        obj.tree.heading("#1", text = "Product_id")
        obj.tree.heading("#2", text = "Product_name")
        obj.tree.heading("#3", text = "Quantity")
        obj.tree.heading("#4", text = "Price")
        obj.tree.column("#0", width = 0)
        obj.tree.column("#1", width = 240, stretch = NO)
        obj.tree.column("#2", width = 240, stretch = NO)
        obj.tree.column("#3", width = 240, stretch = NO)
        obj.tree.column("#4", width = 240, stretch = NO)
        obj.tree.bind("<<TreeviewSelect>>", clickprodtable)
        obj.tree.grid(row = 1, column = 0, columnspan = 7, sticky = (N, S, W, E))
        # create scrollbar
        obj.scrollbary = Scrollbar(
            obj.tableframe, orient = VERTICAL, command = obj.tree.yview)
        obj.scrollbary.grid(row = 1, column = 7, sticky = (N, S, W, E))
        obj.scrollbarx = Scrollbar(
            obj.tableframe, orient = HORIZONTAL, command = obj.tree.xview)
        obj.scrollbarx.grid(row = 2, column = 0, columnspan = 7, sticky = (N, S, W, E))
        obj.tree.configure(yscrollcommand = obj.scrollbary.set,
                           xscrollcommand = obj.scrollbarx.set)
        usp.User_Buytickets_process.refresh_treeview(obj)
        obj.window.resizable(0,0)
        
