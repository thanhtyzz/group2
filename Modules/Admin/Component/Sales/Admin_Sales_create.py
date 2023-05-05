from tkinter import *
import Service.Widget_service as ws
import Api.Admin_Api as Api
from tkinter import ttk
import Modules.Admin.Component.Sales.Admin_Sales_process as asp


class Admin_Sales_create:

    @staticmethod
    def generate_sales(obj):
        # clear all frames
        for frame in obj.allframes:
            frame.place_forget()
        obj.allframes = []

        # create search frame
        obj.searchframe = Frame(obj.window, bg='#fccde0')
        obj.searchframe.place(x=80, y=250, width=900, height=50)
        obj.allframes.append(obj.searchframe)

        # create table frame
        obj.tableframe = Frame(obj.window, bg='#fccde0')
        obj.tableframe.place(x=80, y=310, width=900, height=400)
        obj.allframes.append(obj.tableframe)

        Admin_Sales_create.generate_search(obj)
        Admin_Sales_create.generate_treeview(obj)

    @staticmethod
    def generate_search(obj):
        api = Api.Admin_Api()
        # create search label
        obj.searchlabel = Label(obj.searchframe, text="SEARCH", bg='#fccde0', font=("Montserrat", 10, "bold"))
        obj.searchlabel.place(x=0, y=0, width=100, height=50)
        # create search entry

        all_invoices = api.get_all_invoices_data()
        list = []
        for data in all_invoices:
            list.append(data['Invoice_Id'])

        obj.searchentry = ws.myentry(obj.searchframe)
        obj.searchentry.place(x=100, y=0, width=200, height=50)
        obj.searchentry.set_completion_list(list)
        # create search button
        obj.searchbutton = Button(obj.searchframe, text="Search", font=("Montserrat", 10, "bold"), bg='#CCCCFE',
                                  command=lambda: asp.Admin_Sales_Process.search_button_handle(obj))
        obj.searchbutton.place(x=300, y=0, width=100, height=50)
        # create visualize button
        obj.visualizebutton = Button(obj.searchframe, text="Visualize", font=("Montserrat", 10, "bold"), bg='#CCCCFE',
                                     command=lambda: asp.Admin_Sales_Process.visualize_button_handle(obj))
        obj.visualizebutton.place(x=400, y=0, width=100, height=50)

    @staticmethod
    def generate_treeview(obj):
        api = Api.Admin_Api()
        # create a tree view
        obj.tree = ttk.Treeview(obj.tableframe, columns=(
        "Invoice_Id", "InvoiceDate", "Product_id", "Product_name", "Quantity", "Price"), height=10)
        obj.tree.place(x=0, y=0, width=1000, height=400)
        obj.tree.heading("#0")
        obj.tree.heading("Invoice_Id", text="Invoice_Id")
        obj.tree.heading("InvoiceDate", text="InvoiceDate")
        obj.tree.heading("Product_id", text="Product_id")
        obj.tree.heading("Product_name", text="Product_name")
        obj.tree.heading("Quantity", text="Quantity")
        obj.tree.heading("Price", text="Price")

        obj.tree.column("#0", width=0, stretch=False)
        obj.tree.column("Invoice_Id", width=150, stretch=False)
        obj.tree.column("InvoiceDate", width=150, stretch=False)
        obj.tree.column("Product_id", width=150, stretch=False)
        obj.tree.column("Product_name", width=150, stretch=False)
        obj.tree.column("Quantity", width=150, stretch=False)
        obj.tree.column("Price", width=150, stretch=False)

        data = api.get_all_invoices_data()
        for row in data:
            obj.tree.insert('', 'end', values=(
            row['Invoice_Id'], row['InvoiceDate'], row['Product_id'], row['Product_name'], row['Quantity'],
            row['Price']))