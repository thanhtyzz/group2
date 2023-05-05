from tkinter import *
import Modules.User.Component.Items.User_Items_process as uip


class User_Items_create:

    @staticmethod
    def generate_items(obj):
        # clear all frames
        for frame in obj.allframes:
            frame.place_forget()
        obj.allframes = []
        # create new frames
        obj.tableframe = Frame(obj.window, bg = "#ffffff")
        obj.tableframe.place(x = 50, y = 250, width = 980, height = 400)
        obj.allframes.append(obj.tableframe)
        # create table
        uip.User_Items_process.generate_items_table(obj)