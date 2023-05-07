from tkinter import *
import Modules.User.Component.Films.User_Films_process as uip


class User_Films_create:

    @staticmethod
    def generate_films(obj):
        # clear all frames
        for frame in obj.allframes:
            frame.place_forget()
        obj.allframes = []
        # create new frames
        obj.tableframe = Frame(obj.window, bg = "#ffffff")
        obj.tableframe.place(x = 52, y = 190, width = 980, height = 400)
        obj.allframes.append(obj.tableframe)
        # create table
        uip.User_Films_process.generate_films_table(obj)