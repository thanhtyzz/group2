from tkinter import *
import Api.Admin_Api as Api
from datetime import datetime
import Modules.Admin.Component.Sales.Admin_Sales_create as asc
import matplotlib.pyplot as plt
import seaborn as sns
import warnings


class Admin_Sales_process:

    @staticmethod
    def search_button_handle(obj):
        api = Api.Admin_Api()
        search = obj.entry_2.get()

        for i in obj.tree.get_children():
            obj.tree.delete(i)
        data = api.get_all_invoices_data()
        for row in data:
            if search in row["Invoice_ID"]:
                obj.tree.insert("", "end", values = (row["Invoice_ID"], row["Invoice_Date"], row["Film_ID"], row["Film"], row["Quantity"], row["Price"]))

    @staticmethod
    def visualize_button_handle(obj):
        api = Api.Admin_Api()
        invoices = api.invoices_collection.find()
        date = []
        total_price = []
        for row in invoices:
            date.append(row["Invoice_Date"].date())
            total_price.append(row["Total"])

        if len(date) > 30:
            date = date[-30:]
            total_price = total_price[-30:]
        warnings.simplefilter(action = "ignore", category = FutureWarning)
        x = date
        y = total_price
        #increase DPI
        plt.figure(figsize = (12, 6), dpi = 100)
        sns.regplot(x = x, y = y)
        plt.show()
