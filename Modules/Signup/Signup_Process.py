import Api.Login_Api as Login_Api
import Api.Signup_Api as Signup_Api
import Modules.Login.Login_View as loginview
from tkinter import END, messagebox as mbox
import tkinter as tk
from PIL import ImageTk, Image
from tkinter import *

class Sign_up_Process: 
    
    # The screen displays a choice between "login" and "signup".
    @staticmethod
    def login_button_handle(obj):
        obj.window.destroy()
        app = loginview.LoginView()
        app.window.mainloop()

    @staticmethod 
    def signup_button_handle(obj): 
        username = obj.entry_3.get()
        password = obj.entry_1.get()
        reenterpassword = obj.entry_2.get()
        api = Signup_Api.Signup_Api()
        error = api.check_user_signup(username,password,reenterpassword)
        standard_pass = api.check_user_signup(password, username, reenterpassword)

        if error == -1:
            mbox.showerror('Warning','Invalid User Input')
            obj.entry_3.delete(0, END)
            obj.entry_1.delete(0, END)
            obj.entry_2.delete(0, END)

        elif error == -2:
            mbox.showerror('Warning', 'Password is not the same')
            obj.entry_3.delete(0, END)
            obj.entry_1.delete(0, END)
            obj.entry_2.delete(0, END)

        elif error == -3:
            mbox.showerror('Warning', 'Existed user')
            obj.entry_3.delete(0, END)
            obj.entry_1.delete(0, END)
            obj.entry_2.delete(0, END)
            
        else:
            if standard_pass == 1:
                mbox.showerror('Weak password', 'Password is too short')
                obj.entry_3.delete(0, END)
                obj.entry_1.delete(0, END)
                obj.entry_2.delete(0, END)
            if standard_pass == 2:
                mbox.showerror('Password does not meet criteria', 'No uppercase letters')
                obj.entry_3.delete(0, END)
                obj.entry_1.delete(0, END)
                obj.entry_2.delete(0, END)
            if standard_pass == 3:
                mbox.showerror('Password does not meet criteria', 'No lowercase letters')
                obj.entry_3.delete(0, END)
                obj.entry_1.delete(0, END)
                obj.entry_2.delete(0, END)
            if standard_pass == 4:
                mbox.showerror('Password does not meet criteria', 'Need special characters')
                obj.entry_3.delete(0, END)
                obj.entry_1.delete(0, END)
                obj.entry_2.delete(0, END)
            if standard_pass == 5:
                mbox.showerror('Password does not meet criteria', 'Need letters')
                obj.entry_3.delete(0, END)
                obj.entry_1.delete(0, END)
                obj.entry_2.delete(0, END)
            if standard_pass == 6:
                mbox.showerror('Password does not meet criteria', 'Need numbers')
                obj.entry_3.delete(0, END)
                obj.entry_1.delete(0, END)
                obj.entry_2.delete(0, END)
            else:
                mbox.showinfo('Success', 'Account created successfully')
                obj.entry_3.delete(0, END)
                obj.entry_1.delete(0, END)
                obj.entry_2.delete(0, END)

class MoviePoster:


    def __init__(self, title, image_path):
        self.title = title
        self.image_path = image_path
   
    def load_image(self, width, height):
        img = Image.open(self.image_path)
        img = img.resize((width, height), Image.LANCZOS)
        return ImageTk.PhotoImage(img)


class MoviePosterGrid:
   
    def __init__(self, master, posters, rows, cols, width, height):
        self.master = master
        self.posters = posters
        self.rows = rows
        self.cols = cols
        self.width = width
        self.height = height
   
    def create_widgets(self):
        self.widgets = []
        for row in range(self.rows):
            row_widgets = []
            for col in range(self.cols):
                index = row * self.cols + col
                if index < len(self.posters):
                    poster = self.posters[index]
                    img = poster.load_image(self.width, self.height)
                    label = tk.Label(self.master, image=img)
                    label.image = img
                    label.grid(row=row, column=col)
                    row_widgets.append(label)
            self.widgets.append(row_widgets)
   
    def pack(self):
        self.create_widgets()


    # Example usage:
    def trendingnow(self):
        posters = [
        MoviePoster("The Shawshank Redemption", "Background.png"),
        MoviePoster("The Godfather", "Background.png"),
        MoviePoster("The Dark Knight", "Background.png"),
        MoviePoster("12 Angry Men", "Background.png"),
        # MoviePoster("Schindler's List", "5.jpg"),
        # MoviePoster("The Lord of the Rings: The Return of the King", "6.jpg"),
        # MoviePoster("Pulp Fiction", "7.jpg"),
        # MoviePoster("The Good, the Bad and the Ugly", "8.jpg"),
        # MoviePoster("Fight Club", "fight_club.jpg"),
        # MoviePoster("Forrest Gump", "9.jpg"),
            ]
        root = tk.Tk()
        grid = MoviePosterGrid(root, posters, rows=2, cols=5, width=200, height=300)
        grid.pack()
        root.mainloop()