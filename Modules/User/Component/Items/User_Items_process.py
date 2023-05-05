from tkinter import *
import Api.User_Api as Api
from tkinter import ttk


class User_Items_process:

    @staticmethod
    def generate_items_table(obj):
        api = Api.User_Api()
        data = api.get_all_warehouse_data()
        # create a tree view in tableframe
        tree = ttk.Treeview(obj.tableframe, columns=(
            "Product_id", "Product_name", "Description", "Category", "Price", "Stock"), height = 20)
        tree.heading("#0")
        tree.heading("#1", text = "Product_id")
        tree.heading("#2", text = "Product_name")
        tree.heading("#3", text = "Description")
        tree.heading("#4", text = "Category")
        tree.heading("#5", text = "Price")
        tree.heading("#6", text = "Stock")
        tree.column("#0", width = 0)
        tree.column("#1", width = 160, stretch = NO)
        tree.column("#2", width = 160, stretch = NO)
        tree.column("#3", width = 160, stretch = NO)
        tree.column("#4", width = 160, stretch = NO)
        tree.column("#5", width = 160, stretch = NO)
        tree.column("#6", width = 160, stretch = NO)

        tree.grid(row = 0, column = 0, columnspan = 7, sticky = (N, S, W, E))
        # create scrollbar
        scrollbary = Scrollbar(
            obj.tableframe, orient = VERTICAL, command = tree.yview)
        scrollbary.grid(row = 0, column = 7, sticky = (N, S, W, E))
        scrollbarx = Scrollbar(
            obj.tableframe, orient = HORIZONTAL, command = tree.xview)
        tree.configure(yscrollcommand = scrollbarx.set,
                       xscrollcommand = scrollbary.set)

        # add data to tree view
        for i in range(len(data)):
            tree.insert("", i, text = str(i), values = (data[i]['Product_id'], data[i]['Product_name'],
                        data[i]['Description'], data[i]['Category'], data[i]['Price'], data[i]['Stock']))
