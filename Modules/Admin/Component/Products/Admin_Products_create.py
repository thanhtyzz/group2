from tkinter import *
import Modules.Admin.Component.Products.Admin_Products_process as app
import Api.Admin_Api as Api


class Admin_Products_create:

    @staticmethod
    def generate_products(obj):
        # clear all frames
        for frame in obj.allframes:
            frame.place_forget()
        obj.allframes = []

        # create new frames
        obj.formframe = Frame(obj.window, bg='#fccde0')
        obj.formframe.place(x=205, y=255, width=730, height=350)

        obj.buttonframe = Frame(obj.window, bg="#ffffff")
        obj.buttonframe.place(x=315, y=630, width=450, height=65)
        obj.allframes.append(obj.formframe)
        obj.allframes.append(obj.buttonframe)

        # Generate product button and product form
        Admin_Products_create.generate_products_button(obj)
        Admin_Products_create.generate_products_form(obj)

    @staticmethod
    def generate_products_form(obj):
        # create form in form frame
        obj.product_id = StringVar()

        api = Api.Admin_Api()
        obj.product_id.set(api.get_last_prod_id())

        obj.product_id_label = Label(obj.formframe, text="Product ID:", font=("Montserrat", 12, "bold"), bg='#fccde0')
        obj.product_id_label.place(x=45, y=35, width=125, height=25)
        obj.product_id_entry = Entry(obj.formframe, font=('Montserrat', 12), textvariable=obj.product_id)
        obj.product_id_entry.place(x=230, y=30, width=445, height=35)

        obj.product_name_label = Label(obj.formframe, text="Product name:", font=("Montserrat", 12, 'bold'),
                                       bg='#fccde0')
        obj.product_name_label.place(x=41, y=85, width=160, height=25)
        obj.product_name_entry = Entry(obj.formframe, font=('Montserrat', 12))
        obj.product_name_entry.place(x=230, y=80, width=445, height=35)

        obj.description_label = Label(obj.formframe, text="Description:", font=("Montserrat", 12, "bold"), bg='#fccde0')
        obj.description_label.place(x=45, y=135, width=130, height=25)
        obj.description_entry = Entry(obj.formframe, font=('Montserrat', 12))
        obj.description_entry.place(x=230, y=130, width=445, height=35)

        obj.category_label = Label(obj.formframe, text="Category:", font=("Montserrat", 12, "bold"), bg='#fccde0')
        obj.category_label.place(x=48, y=185, width=105, height=25)
        obj.category_entry = Entry(obj.formframe, font=('Montserrat', 12))
        obj.category_entry.place(x=230, y=180, width=445, height=35)

        obj.price_label = Label(obj.formframe, text="Price:", font=("Montserrat", 12, "bold"), bg='#fccde0')
        obj.price_label.place(x=51, y=235, width=65, height=25)
        obj.price_entry = Entry(obj.formframe, font=('Montserrat', 12))
        obj.price_entry.place(x=230, y=230, width=445, height=35)

        obj.stock_label = Label(obj.formframe, text="Stock:", font=("Montserrat", 12, "bold"), bg='#fccde0')
        obj.stock_label.place(x=50, y=285, width=70, height=25)
        obj.stock_entry = Entry(obj.formframe, font=('Montserrat', 12))
        obj.stock_entry.place(x=230, y=280, width=445, height=35)

    @staticmethod
    def generate_products_button(obj):
        obj.add_button = Button(obj.buttonframe, text="Add item", font=("Montserrat", 12, "bold"), bg='#CCCCFE',
                                command=lambda: app.Admin_Products_Process.add_item_button_handle(obj))
        obj.add_button.place(x=55, y=10, width=175, height=40)

        obj.remove_data = Button(obj.buttonframe, text="Remove", font=("Montserrat", 12, "bold"), bg='#CCCCFE',
                                 command=lambda: app.Admin_Products_Process.reset_button_handle(obj))
        obj.remove_data.place(x=265, y=10, width=175, height=40)