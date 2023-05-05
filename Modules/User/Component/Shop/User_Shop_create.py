from tkinter import *
import Modules.User.Component.Shop.User_Shop_process as usp
import Api.User_Api as Api
from tkinter import ttk
import Service.Widget_service as ws


class User_Shop_create:

    @staticmethod
    def generate_shop(obj):
        # clear all frames
        for frame in obj.allframes:
            frame.place_forget()
        obj.allframes = []

        # create new frames
        obj.tableframe = Frame(obj.window, bg="#fccde0")
        obj.tableframe.place(x=50, y=250, width=980, height=200)

        obj.formframe = Frame(obj.window, bg="#fccde0")
        obj.formframe.place(x=50, y=480, width=480, height=200)

        obj.buttonframe = Frame(obj.window, bg="#fccde0")
        obj.buttonframe.place(x=550, y=480, width=480, height=200)

        obj.allframes.append(obj.tableframe)
        obj.allframes.append(obj.formframe)
        obj.allframes.append(obj.buttonframe)

        User_Shop_create.generate_shop_table(obj)
        User_Shop_create.generate_shop_form(obj)
        User_Shop_create.generate_shop_buttons(obj)

    @staticmethod
    def generate_shop_table(obj):
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
        obj.tree = ttk.Treeview(obj.tableframe, columns=(
            "Product_id", "Product_name", "Quantity", "Price"), height=20)
        obj.tree.heading("#0")
        obj.tree.heading("#1", text="Product_id")
        obj.tree.heading("#2", text="Product_name")
        obj.tree.heading("#3", text="Quantity")
        obj.tree.heading("#4", text="Price")
        obj.tree.column("#0", width=0)
        obj.tree.column("#1", width=240, stretch=NO)
        obj.tree.column("#2", width=240, stretch=NO)
        obj.tree.column("#3", width=240, stretch=NO)
        obj.tree.column("#4", width=240, stretch=NO)
        obj.tree.bind("<<TreeviewSelect>>", clickprodtable)
        obj.tree.grid(row=1, column=0, columnspan=7, sticky=(N, S, W, E))
        # create scrollbar
        obj.scrollbary = Scrollbar(
            obj.tableframe, orient=VERTICAL, command=obj.tree.yview)
        obj.scrollbary.grid(row=1, column=7, sticky=(N, S, W, E))
        obj.scrollbarx = Scrollbar(
            obj.tableframe, orient=HORIZONTAL, command=obj.tree.xview)
        obj.scrollbarx.grid(row=2, column=0, columnspan=7, sticky=(N, S, W, E))
        obj.tree.configure(yscrollcommand=obj.scrollbary.set,
                           xscrollcommand=obj.scrollbarx.set)
        usp.User_Shop_process.refresh_treeview(obj)
        obj.window.resizable(0, 0)

    @staticmethod
    def generate_shop_form(obj):

        # create form in form frame
        obj.product_id = StringVar()
        obj.product_name = StringVar()
        obj.quantity = StringVar()
        obj.price = StringVar()
        obj.total = StringVar()

        obj.product_id_label = Label(
            obj.formframe, text="Product_id:", font=("Montserrat", 12, "bold"), bg="#fccde0")
        obj.product_id_label.place(x=0, y=10, width=150, height=30)
        obj.product_id_entry = Entry(obj.formframe, textvariable=obj.product_id, font=(
            "Montserrat", 12), state=DISABLED, width=20)
        obj.product_id_entry.place(x=160, y=10, width=300, height=30)

        obj.product_name_label = Label(
            obj.formframe, text="Product_name:", font=("Montserrat", 12, "bold"), bg="#fccde0")
        obj.product_name_label.place(x=13, y=50, width=150, height=30)

        obj.product_name_entry = Entry(obj.formframe, textvariable=obj.product_name, font=(
            "Montserrat", 12), state=DISABLED, width=150)
        obj.product_name_entry.place(x=160, y=50, width=300, height=30)

        obj.quantity_label = Label(obj.formframe, text="Quantity:", font=(
            "Montserrat", 12, "bold"), bg="#fccde0")
        obj.quantity_label.place(x=-12, y=90, width=150, height=30)
        obj.quantity_entry = Entry(obj.formframe, textvariable=obj.quantity, font=(
            "Montserrat", 12), state=DISABLED, width=150)
        obj.quantity_entry.place(x=160, y=90, width=300, height=30)

        obj.price_label = Label(obj.formframe, text="Price:", font=(
            "Montserrat", 12, "bold"), bg="#fccde0")
        obj.price_label.place(x=-24, y=130, width=150, height=30)
        obj.price_entry = Entry(obj.formframe, textvariable=obj.price, font=(
            "Montserrat", 12), state=DISABLED, width=150)
        obj.price_entry.place(x=160, y=130, width=300, height=30)

    @staticmethod
    def generate_shop_buttons(obj):
        api = Api.User_Api()
        # process button
        obj.process_button = Button(obj.buttonframe, text="Process", font=(
            "Montserrat", 12, "bold"), bg="#ccccfe", command=lambda: usp.User_Shop_process.process_cart_handle(obj))
        obj.process_button.place(x=10, y=10, width=100, height=120)

        obj.search_label = Label(obj.buttonframe, text="Search:", font=(
            "Montserrat", 12, "bold"), bg="#fccde0")
        obj.search_label.place(x=120, y=10, width=100, height=30)

        obj.quantity_label = Label(obj.buttonframe, text="Quantity:", font=(
            "Montserrat", 12, "bold"), bg="#fccde0")
        obj.quantity_label.place(x=126, y=50, width=100, height=30)

        # create search entry
        list = api.get_all_product_name()
        obj.searchvar = StringVar()
        obj.search_entry = ws.myentry(
            obj.buttonframe, textvariable=obj.searchvar, width=20)
        obj.search_entry.set_completion_list(list)
        # obj.search_entry = Entry(obj.buttonframe, font = ("Montserrat", 12), width=20)
        obj.search_entry.place(x=240, y=10, width=200, height=30)

        # create quantity entry
        obj.quantity_entry_bframe = Entry(
            obj.buttonframe, font=("Montserrat", 12), width=20)
        obj.quantity_entry_bframe.place(x=240, y=50, width=200, height=30)

        # create add to cart button
        obj.add_button = Button(obj.buttonframe, text="Add to cart", font=(
            "Montserrat", 12, "bold"), bg="#ccccfe", command=lambda: usp.User_Shop_process.add_to_cart(obj))
        obj.add_button.place(x=130, y=100, width=160, height=30)

        # create remove from cart button
        obj.remove_button = Button(obj.buttonframe, text="Remove", font=(
            "Montserrat", 12, "bold"), bg="#ccccfe", command=lambda: usp.User_Shop_process.remove_from_cart(obj))
        obj.remove_button.place(x=300, y=100, width=160, height=30)

        # create total amount label
        obj.total_label = Label(obj.buttonframe, text="Total:", font=(
            "Montserrat", 20, "bold"), bg="#fccde0")
        obj.total_label.place(x=10, y=150, width=100, height=30)

        # create total amount entry
        obj.total_entry = Entry(obj.buttonframe, textvariable=obj.total, font=(
            "Montserrat", 20), state=DISABLED, width=20)
        obj.total_entry.place(x=120, y=150, width=200, height=30)
        try:
            usp.User_Shop_process.get_total_ammount(obj)
        except:
            pass