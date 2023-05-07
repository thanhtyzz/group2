import Api.Login_Api as Login_Api
import Api.Signup_Api as Signup_Api
import Modules.Login.Login_View as loginview
from tkinter import END, messagebox as mbox
import tkinter as tk
from PIL import ImageTk, Image
from tkinter import *
import matplotlib.pyplot as plt
import matplotlib.image as mpimg
import Modules.Signup.Signup_View as suv

class Signup_Process: 
    
    # The screen displays a choice between "login" and "signup".
    @staticmethod
    def login_button_handle(obj):
        obj.window.destroy()
        app = loginview.LoginView()
        app.window.mainloop()

    @staticmethod 
    def signup_button_handle(obj): 
        username = obj.entry_1.get()
        password = obj.entry_2.get()
        reenterpassword = obj.entry_3.get()
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

class Trendingnow_process:
    @staticmethod
    def trendingnow(obj):
        obj.window.destroy()
        app = suv.Tredingnow_View()
        app.window.mainloop()

    
# class MoviePoster:
    def __init__(self, title, image_path):
        self.title = title
        self.image_path = image_path

    def load_image(self, width, height):
        image = mpimg.imread(self.image_path)
        # Hiển thị hình ảnh
        plt.imshow(image)
        # plt.axis('off')
        plt.show()


# class MoviePosterGrid:
#     def __init__(self, master, posters, rows, cols, width, height):
#         self.master = master
#         self.posters = posters
#         self.rows = rows
#         self.cols = cols
#         self.width = width
#         self.height = height

#     def create_widgets(self):
#         self.widgets = []
#         for row in range(self.rows):
#             row_widgets = []
#             for col in range(self.cols):
#                 index = row * self.cols + col
#                 if index < len(self.posters):
#                     poster = self.posters[index]
#                     img = poster.load_image(self.width, self.height)
#                     label = tk.Label(self.master, image=img)
#                     label.image = img
#                     label.grid(row=row, column=col)
#                     row_widgets.append(label)
#             self.widgets.append(row_widgets)

#     def pack(self):
#         self.create_widgets()


#     # Example usage:
#     def trendingnow(self):
#         posters = [
#             MoviePoster("The Shawshank Redemption", "D:\do-an-cuoi-ki-nhom-2\Modules\Signup\Background.png"),
#             MoviePoster("The Godfather", "D:\do-an-cuoi-ki-nhom-2\Modules\Signup\Background.png"),
#             MoviePoster("The Dark Knight", "Background.png"),
#             MoviePoster("12 Angry Men", "Background.png"),
#             # MoviePoster("Schindler's List", "5.jpg"),
#             # MoviePoster("The Lord of the Rings: The Return of the King", "6.jpg"),
#             # MoviePoster("Pulp Fiction", "7.jpg"),
#             # MoviePoster("The Good, the Bad and the Ugly", "8.jpg"),
#             # MoviePoster("Fight Club", "fight_club.jpg"),
#             # MoviePoster("Forrest Gump", "9.jpg"),
#         ]
#         root = tk.Tk()
#         grid = MoviePosterGrid(root, posters, rows=2, cols=5, width=6850, height=4920)
#         grid.pack()
#         root.mainloop()
