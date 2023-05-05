from tkinter import *
import Api.User_Api as Api
from tkinter import ttk

class User_Films_Process:

    @staticmethod
    def generate_films_table(obj):
        api = Api.User_Api()
        data = api.get_all_warehouse_data()
        #create a tree view in table frame
        tree = ttk.Treeview(obj.tableframe, columns=("Film id","Film", "Genre", "Showtime", "Price", "Stock"), height = 10)
        tree.heading("#0")
        tree.heading("#1", text = "Film id")
        tree.heading("#2", text = "Film")
        tree.heading("#3", text = "Genre")
        tree.heading("#4", text = "Showtime")
        tree.heading("#5", text = "Price")
        tree.heading("#6", text = "Stock")
        tree.column("#0", width = 80, stretch = NO)
        tree.column("#1", width = 80, stretch = NO)
        tree.column("#2", width = 80, stretch = NO)
        tree.column("#3", width = 80, stretch = NO)
        tree.column("#4", width = 80, stretch = NO)
        tree.column("#5", width = 80, stretch = NO)
        tree.column("#6", width = 80, stretch = NO)

        tree.grid(row = 0, column = 0, columnspan = 7, sticky = (N, S, W, E))
        scrollbarx = Scrollbar(obj.tableframe, orient = HORIZONTAL, command=tree.xview())
        scrollbary= Scrollbar(obj.tableframe, orient = VERTICAL, command=tree.yview())
        scrollbary.grid(row=0, column=7, sticky=(N, S, W, E))

        #add data to tree view
        for i in range(len(data)):
            tree.insert("", i, text = str(i),  values = (data[i]['Film id'], data[i]['Film'], data[i]['Genre'], data[i]['Showtime'], data[i]['Price'], data[i]['Stock']))
