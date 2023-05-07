from tkinter import *
from pathlib import Path
import Modules.Admin.Component.Films.Admin_Films_process as app
import Api.Admin_Api as Api
from PIL import ImageTk, Image

class Admin_Films_create:
    def __init__(self):
        self.window = Tk()
        # get screen width and height
        self.screen_width = self.window.winfo_screenwidth()
        self.screen_height = self.window.winfo_screenheight()

        # set window width and height
        self.window_width = 685
        self.window_height = 492
        # set window position
        self.window.geometry("%dx%d+%d+%d" % (self.window_width, self.window_height,
                             (self.screen_width - self.window_width) / 2, (self.screen_height - self.window_height) / 2))
        self.window.configure(bg="#4C4A4A")
        self.window.title("Admin")

        self.canvas = Canvas(self.window, bg="#4C4A4A", height=492, width=685, bd=0, highlightthickness=0, relief="ridge")
        self.canvas.place(x=0, y=0)

    @staticmethod


    @staticmethod
    def generate_films(obj):
        # Xóa các frame hiện tại
        for frame in obj.allframes:
            frame.destroy()
        obj.allframes = []

        # Tạo frame mới
        obj.formframe = Frame(obj.window, bg='#4C4A4A')
        obj.formframe.place(x=121, y=185, width=444, height=240)
        obj.allframes.append(obj.formframe)

        obj.buttonframe = Frame(obj.window, bg="#ffffff")
        obj.buttonframe.place(x=315, y=630, width=450, height=65)
        obj.allframes.append(obj.buttonframe)

        # Tạo các thành phần trong frame
        Admin_Films_create.generate_films_button(obj)
        Admin_Films_create.generate_films_form(obj)

        image_path = "D:\do-an-cuoi-ki-nhom-2\Images\Admin\Films\letter.png"
        image = Image.open(image_path)
        image = image.resize((111, 235))
        photo = ImageTk.PhotoImage(image)
        label = Label(obj.formframe, image=photo)
        label.image = photo
        label.place(x=0.0, y=0.0)
        label.configure(background='#4C4A4A')


    @staticmethod
    def generate_films_form(obj):
        # create form in form frame
        obj.product_id = StringVar()

        api = Api.Admin_Api()
        obj.product_id.set(api.get_last_prod_id())
        
        assets_path = Path(r"D:\do-an-cuoi-ki-nhom-2\Images\Admin\Films")
        
        obj.background_img = PhotoImage(file=assets_path / "Background.png")
        obj.background = obj.canvas.create_image(342.0, 246.0, image=obj.background_img)

        obj.entry_image = PhotoImage(file=assets_path / "Textbox.png")
        obj.film_id_entry = Entry(obj.formframe, bd=0, bg="#D9D9D9", fg="#000716", highlightthickness=0, textvariable = obj.product_id)
        obj.film_id_entry.place(x=150.0, y=10.0, width=284.0, height=24.0)

        obj.film_entry = Entry(obj.formframe, bd=0, bg="#D9D9D9", fg="#000716", highlightthickness=0)
        obj.film_entry.place(x=150.0, y=50.0, width=284.0, height=24.0)

        obj.genre_entry = Entry(obj.formframe, bd=0, bg="#D9D9D9", fg="#000716", highlightthickness=0)
        obj.genre_entry.place(x=150.0, y=90.0, width=284.0, height=24.0)

        obj.showtime_entry = Entry(obj.formframe, bd=0, bg="#D9D9D9", fg="#000716", highlightthickness=0)
        obj.showtime_entry.place(x=150.0, y=130.0, width=284.0, height=24.0)

        obj.price_entry = Entry(obj.formframe, bd=0, bg="#D9D9D9", fg="#000716", highlightthickness=0)
        obj.price_entry.place(x=150.0, y=170.0, width=284.0, height=24.0)

        obj.stock_entry = Entry(obj.formframe, bd=0, bg="#D9D9D9", fg="#000716", highlightthickness=0)
        obj.stock_entry.place(x=150.0, y=210.0, width=284.0, height=24.0)
        
    @staticmethod
    def generate_films_button(obj):
        assets_path = Path(r"D:\do-an-cuoi-ki-nhom-2\Images\Admin\Films")

        obj.addfilm_image = PhotoImage(file=assets_path / "Button_Addfilm.png")
        obj.remove_image = PhotoImage(file=assets_path / "Button_Remove.png")

        obj.addfilm_button = Button(image=obj.addfilm_image, borderwidth=0, highlightthickness=0,
                               command=lambda: app.Admin_Films_process.addfilm_button_handle(obj))
        obj.addfilm_button.place(x=219.0, y=448.0, width=104.0, height=28.0)

        obj.remove_button = Button(image=obj.remove_image, borderwidth=0, highlightthickness=0,
                               command=lambda: app.Admin_Films_process.remove_button_handle(obj))
        obj.remove_button.place(x=361.0, y=448.0, width=104.0, height=28.0)