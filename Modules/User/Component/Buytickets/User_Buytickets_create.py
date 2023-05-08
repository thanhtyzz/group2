from tkinter import *
from pathlib import Path
import Modules.User.Component.Buytickets.User_Buytickets_process as usp
import Api.User_Api as Api
from tkinter import ttk
import Service.Widget_service as ws


class User_Buytickets_create:

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
        self.window.title("Buytickets")

        self.canvas = Canvas(self.window, bg="#FFFFFF", height=492, width=685, bd=0, highlightthickness=0, relief="ridge")
        self.canvas.place(x=0, y=0)

        assets_path = Path(r"D:\do-an-cuoi-ki-nhom-2\Images\User\BuyTickets")

        self.background_img = PhotoImage(file=assets_path / "Background.png")
        self.background = self.canvas.create_image(342.0, 246.0, image=self.background_img)

    @staticmethod
    def generate_buytickets(obj):
        # clear all frames
        for frame in obj.allframes:
            frame.place_forget()
        obj.allframes = []

        # create new frames
        obj.tableframe = Frame(obj.window, bg = "#D9D9D9")
        obj.tableframe.place(x = 27, y = 187, width = 637, height = 134)

        # obj.formframe = Frame(obj.window, bg = "#4C4A4A")
        # obj.formframe.place(x = 200, y = 333, width = 322, height = 145)

        # obj.buttonframe = Frame(obj.window, bg = "#4C4A4A")
        # obj.buttonframe.place(x = 348, y = 333, width = 322, height = 145)

        obj.allframes.append(obj.tableframe)
        # obj.allframes.append(obj.formframe)
        # obj.allframes.append(obj.buttonframe)

        User_Buytickets_create.generate_buytickets_table(obj)
        User_Buytickets_create.generate_buytickets_form(obj)
        User_Buytickets_create.generate_buytickets_buttons(obj)

    @staticmethod
    def generate_buytickets_table(obj):
        def clickprodtable(event):
            # get selected film
            cur = obj.tree.selection()
            cur = obj.tree.item(cur)
            try:
                obj.selected_film = cur['values']
                obj.film_id.set(cur['values'][0])
                obj.film.set(cur['values'][1])
                obj.quantity.set(cur['values'][2])
                obj.price.set(cur['values'][3])
            except:
                pass

        # create tree view
        obj.tree = ttk.Treeview(obj.tableframe, columns = (
            "Film_ID", "Film", "Quantity", "Price"), height = 5)
        obj.tree.heading("#0")
        obj.tree.heading("#1", text = "Film_ID")
        obj.tree.heading("#2", text = "Film")
        obj.tree.heading("#3", text = "Quantity")
        obj.tree.heading("#4", text = "Price")
        obj.tree.column("#0", width = 0)
        obj.tree.column("#1", width = 150, stretch = NO)
        obj.tree.column("#2", width = 150, stretch = NO)
        obj.tree.column("#3", width = 150, stretch = NO)
        obj.tree.column("#4", width = 150, stretch = NO)
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
        
    @staticmethod
    def generate_buytickets_form(obj):
        
        obj.film_id = StringVar()
        obj.film = StringVar()
        obj.quantity = StringVar()
        obj.price = StringVar()
        obj.total = StringVar()

        assets_path = Path(r"D:\do-an-cuoi-ki-nhom-2\Images\User\BuyTickets")

        obj.entry_image_1 = PhotoImage(file=assets_path / "Textbox_1.png")
        obj.entry_image_2 = PhotoImage(file=assets_path / "Textbox_2.png")
        

        obj.entry_bg_1 = obj.canvas.create_image(231.0, 459.0, image=obj.entry_image_1)
        obj.entry_1 = Entry(obj.canvas, textvariable=obj.film_id, bd=0, bg="#D9D9D9", fg="#000716", highlightthickness=0)
        obj.entry_1.place(x=146.0, y=343.0, width=170.0, height=20.0)

        obj.entry_bg_2 = obj.canvas.create_image(231.0, 425.0, image=obj.entry_image_1)
        obj.entry_2 = Entry(obj.canvas, textvariable=obj.film, bd=0, bg="#D9D9D9", fg="#000716", highlightthickness=0)
        obj.entry_2.place(x=146.0, y=378.0, width=170.0, height=20.0)

        obj.entry_bg_3 = obj.canvas.create_image(231.0, 389.0, image=obj.entry_image_1)
        obj.entry_3 = Entry(obj.canvas, textvariable=obj.quantity, bd=0, bg="#D9D9D9", fg="#000716", highlightthickness=0)
        obj.entry_3.place(x=146.0, y=414.0, width=170.0, height=20.0)

        obj.entry_bg_4 = obj.canvas.create_image(231.0, 354.0, image=obj.entry_image_1)
        obj.entry_4 = Entry(obj.canvas, textvariable = obj.price, bd=0, bg="#D9D9D9", fg="#000716", highlightthickness=0)
        obj.entry_4.place(x=146.0, y=448.0, width=170.0, height=20.0)

        obj.entry_bg_1 = obj.canvas.create_image(231.0, 459.0, image=obj.entry_image_1)
        obj.entry_1 = Entry(obj.canvas, textvariable=obj.film_id, bd=0, bg="#D9D9D9", fg="#000716", highlightthickness=0)
        obj.entry_1.place(x=146.0, y=343.0, width=170.0, height=20.0)

    @staticmethod
    def generate_buytickets_buttons(obj):
        api = Api.User_Api()

        assets_path = Path(r"D:\do-an-cuoi-ki-nhom-2\Images\User\BuyTickets")

        obj.process_image = PhotoImage(file=assets_path / "Button_Process.png")
        obj.addtocart_image = PhotoImage(file=assets_path / "Button_Addtocart.png")
        obj.remove_image = PhotoImage(file=assets_path / "Button_Remove.png")


        obj.process_button = Button(obj.canvas, image=obj.process_image, borderwidth=0, highlightthickness=0,
                               command=lambda: usp.User_Buytickets_process.process_cart_handle(obj))
        obj.process_button.place(x=358.0, y=343.0, width=70.0, height=88.0)

        obj.addtocart_button = Button(obj.canvas, image=obj.addtocart_image, borderwidth=0, highlightthickness=0,
                               command=lambda: usp.User_Buytickets_process.add_to_cart(obj))
        obj.addtocart_button.place(x=446.0, y=406.0, width=95.0, height=25.0)

        obj.remove_button = Button(obj.canvas, image=obj.remove_image, borderwidth=0, highlightthickness=0,
                               command=lambda: usp.User_Buytickets_process.remove_from_cart(obj))
        obj.remove_button.place(x=559.0, y=406.0, width=95.0, height=25.0)

        list = api.get_all_film_name()
        obj.searchvar = StringVar()
        obj.entry_6 = ws.myentry(
            obj.canvas, textvariable = obj.searchvar, width = 20)
        obj.entry_6.set_completion_list(list)

        obj.entry_bg_5 = obj.canvas.create_image(541.0, 455.0, image=obj.entry_image_1)
        obj.entry_5 = Entry(obj.canvas, textvariable = obj.total, bd=0, bg="#D9D9D9", fg="#000716", highlightthickness=0)
        obj.entry_5.place(x=461.0, y=444.0, width=160.0, height=20.0)
        try: 
            usp.User_Buytickets_process.get_total_ammount(obj)
        except:
            pass 

        obj.entry_bg_6 = obj.canvas.create_image(590.5, 383.0, image=obj.entry_image_2)
        obj.entry_6 = Entry(obj.canvas, bd=0, bg="#D9D9D9", fg="#000716", highlightthickness=0)
        obj.entry_6.place(x=519.0, y=372.0, width=143.0, height=20.0)

        obj.entry_bg_7 = obj.canvas.create_image(590.5, 354.0, image=obj.entry_image_2)
        obj.entry_7 = Entry(obj.canvas, bd=0, bg="#D9D9D9", fg="#000716", highlightthickness=0)
        obj.entry_7.place(x=519.0, y=343.0, width=143.0, height=20.0)

        # obj.canvas.create_rectangle(27.0, 187.0, 637.0, 134.0, fill="#D9D9D9", outline="")
        obj.canvas.create_rectangle(340.0, 333.0, 678.0, 480.0, fill="#4C4A4A", outline="")
        obj.canvas.create_rectangle(10.0, 333.0, 330.0, 480.0, fill="#4C4A4A", outline="")

        # obj.formframe.place(x = 200, y = 333, width = 322, height = 145)


    
        
