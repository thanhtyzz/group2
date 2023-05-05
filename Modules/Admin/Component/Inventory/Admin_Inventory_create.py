from tkinter import *
from tkinter import ttk
import Api.Admin_Api as Api
import Service.Widget_service as ws
import Modules.Admin.Component.Inventory.Admin_Inventory_process as aip


class Admin_Inventory_create:

    @staticmethod
    def generate_inventory(obj):

        # clear all frames
        for frame in obj.allframes:
            frame.place_forget()
        obj.allframes = []

        # create new frames
        obj.formframe = Frame(obj.window, bg='#fccde0')
        obj.formframe.place(x=30, y=265, width=400, height=335)

        obj.tableframe = Frame(obj.window, bg='#fccde0')
        obj.tableframe.place(x=455, y=320, width=605, height=360)

        obj.searchframe = Frame(obj.window, bg='#ffffff')
        obj.searchframe.place(x=455, y=265, width=605, height=45)

        obj.buttonframe = Frame(obj.window, bg='#ffffff')
        obj.buttonframe.place(x=30, y=620, width=400, height=60)

        obj.allframes.append(obj.formframe)
        obj.allframes.append(obj.tableframe)
        obj.allframes.append(obj.buttonframe)
        obj.allframes.append(obj.searchframe)

        Admin_Inventory_create.generate_inventory_form(obj)
        Admin_Inventory_create.generate_inventory_button(obj)
        Admin_Inventory_create.generate_inventory_table(obj)
        Admin_Inventory_create.generate_inventory_search(obj)

    @staticmethod
    def generate_inventory_form(obj):
        # create form in form frame
        obj.product_name = StringVar()
        obj.description = StringVar()
        obj.category = StringVar()
        obj.price = StringVar()
        obj.current_stock = StringVar()
        obj.add_stock = StringVar()

        obj.product_name_label = Label(obj.formframe, text="Product name:", font=("Montserrat", 12, "bold"),
                                       bg='#fccde0')
        obj.product_name_label.place(x=16, y=25, width=170, height=25)
        obj.product_name_entry = Entry(obj.formframe, textvariable=obj.product_name, font=("Montserrat", 12))
        obj.product_name_entry.place(x=190, y=20, width=200, height=35)

        obj.description_label = Label(obj.formframe, text="Description:", font=('Montserrat', 12, 'bold'), bg='#fccde0')
        obj.description_label.place(x=20, y=75, width=140, height=25)
        obj.description_entry = Entry(obj.formframe, textvariable=obj.description, font=("Montserrat", 12))
        obj.description_entry.place(x=190, y=70, width=200, height=35)

        obj.category_label = Label(obj.formframe, text="Category:", font=('Montserrat', 12, 'bold'), bg='#fccde0')
        obj.category_label.place(x=25, y=125, width=110, height=25)
        obj.category_entry = Entry(obj.formframe, textvariable=obj.category, font=('Montserrat', 12))
        obj.category_entry.place(x=190, y=120, width=200, height=35)

        obj.price_label = Label(obj.formframe, text="Price:", font=('Montserrat', 12, 'bold'), bg='#fccde0')
        obj.price_label.place(x=30, y=175, width=70, height=25)
        obj.price_entry = Entry(obj.formframe, textvariable=obj.price, font=("Montserrat", 12))
        obj.price_entry.place(x=190, y=170, width=200, height=35)

        obj.current_stock_label = Label(obj.formframe, text="Current stock:", font=('Montserrat', 12, 'bold'),
                                        bg='#fccde0')
        obj.current_stock_label.place(x=19, y=225, width=155, height=25)

        obj.current_stock = StringVar()
        obj.current_stock_entry = Entry(obj.formframe, textvariable=obj.current_stock, font=("Montserrat", 12),
                                        state=DISABLED)
        obj.current_stock_entry.place(x=190, y=220, width=200, height=35)

        obj.add_stock_label = Label(obj.formframe, text="Add stock:", font=('Montserrat', 12, 'bold'), bg='#fccde0')
        obj.add_stock_label.place(x=18, y=275, width=130, height=25)
        obj.add_stock_entry = Entry(obj.formframe, textvariable=obj.add_stock, font=("Montserrat", 12))
        obj.add_stock_entry.place(x=190, y=270, width=200, height=35)

    @staticmethod
    def generate_inventory_button(obj):
        # create buttons in button frame
        obj.update_button = Button(obj.buttonframe, text='Update', font=('Montserrat', 12, 'bold'), bg='#ccccfe',
                                   command=lambda: aip.Admin_Inventory_Process.update_button_handle(obj))
        obj.update_button.place(x=20, y=5, width=150, height=50)

        obj.remove_button = Button(obj.buttonframe, text="Remove", font=('Montserrat', 12, 'bold'), bg='#ccccfe',
                                   command=lambda: aip.Admin_Inventory_Process.remove_button_handle(obj))
        obj.remove_button.place(x=230, y=5, width=150, height=50)

    @staticmethod
    def generate_inventory_search(obj):
        api = Api.Admin_Api()
        data = api.get_all_warehouse_data()
        # get all Product name in data
        product_name = []
        for i in data:
            product_name.append(i['Product_name'])

        # create entry in search frame
        obj.search_entry = ws.myentry(obj.searchframe, font=('Montserrat', 12), width=20)
        obj.search_entry.place(x=15, y=5, width=335, height=35)
        obj.search_entry.set_completion_list(product_name)

        # create button in search frame
        obj.search_button = Button(obj.searchframe, text="Search", font=('Montserrat', 12, 'bold'), bg='#ccccfe',
                                   command=lambda: aip.Admin_Inventory_Process.search_button_handle(obj))
        obj.search_button.place(x=360, y=6, width=80, height=25)

        obj.reset_button = Button(obj.searchframe, text='Reset', font=('Montserrat', 12, 'bold'), bg='#ccccfe',
                                  command=lambda: aip.Admin_Inventory_Process.reset_button_handle(obj))
        obj.reset_button.place(x=460, y=6, width=80, height=25)

    @staticmethod
    def generate_inventory_table(obj):
        def clickprodtable(event):
            # get selected product
            cur = obj.tree.selection()
            cur = obj.tree.item(cur)
            try:
                obj.selected_product = cur['values']
                obj.product_name.set(cur['values'][1])
                obj.description.set(cur['values'][2])
                obj.category.set(cur['values'][3])
                obj.price.set(cur['values'][4])
                obj.current_stock.set(cur['values'][5])
            except:
                pass

        # create tree view
        obj.tree = ttk.Treeview(obj.tableframe, columns=('ID', 'Name', 'Description',
                                                         'Category', 'Price', 'Stock'))
        obj.tree.heading('#0')
        obj.tree.heading('#1', text='ID')
        obj.tree.heading('#2', text='Name')
        obj.tree.heading('#3', text='Description')
        obj.tree.heading('#4', text='Category')
        obj.tree.heading('#5', text='Price')
        obj.tree.heading('#6', text='Stock')

        obj.tree.column('#0', width=0)
        obj.tree.column('#1', width=40)
        obj.tree.column('#2', width=100)
        obj.tree.column('#3', width=170)
        obj.tree.column('#4', width=110)
        obj.tree.column('#5', width=110)
        obj.tree.column('#6', width=70)
        obj.tree.bind("<<TreeviewSelect>>", clickprodtable)
        obj.tree.grid(row=1, column=0, columnspan=6)

        # create scroll bar
        obj.scrollbary = ttk.Scrollbar(obj.tableframe, orient=VERTICAL, command=obj.tree.yview)
        obj.scrollbary.grid(row=1, column=6)

        api = Api.Admin_Api()
        products = api.get_all_warehouse_data()

        for product in products:
            obj.tree.insert('', 'end', values=(
            product['Product_id'], product['Product_name'], product['Description'], product['Category'],
            product['Price'], product['Stock']))