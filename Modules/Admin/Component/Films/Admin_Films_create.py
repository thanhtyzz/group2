from tkinter import *
from pathlib import Path
import Modules.Admin.Component.Films.Admin_Films_process as app
import Api.Admin_Api as Api

class Admin_Films_create:
    # def __init__(self):
    #     self.window = Tk()
    #     # get screen width and height
    #     self.screen_width = self.window.winfo_screenwidth()
    #     self.screen_height = self.window.winfo_screenheight()

    #     # set window width and height
    #     self.window_width = 685
    #     self.window_height = 492
    #     # set window position
    #     self.window.geometry("%dx%d+%d+%d" % (self.window_width, self.window_height,
    #                          (self.screen_width - self.window_width) / 2, (self.screen_height - self.window_height) / 2))
    #     self.window.configure(bg="#FFFFFF")
    #     self.window.title("Admin")

    #     self.canvas = Canvas(self.window, bg="#FFFFFF", height=492, width=685, bd=0, highlightthickness=0, relief="ridge")
    #     self.canvas.place(x=0, y=0)

    @staticmethod
    def generate_products(obj):
        # clear all frames
        for frame in obj.allframes:
            frame.place_forget()
        obj.allframes = []

        # create new frames
        obj.formframe = Frame(obj.window, bg = '#fccde0')
        obj.formframe.place(x = 205, y = 255, width = 730, height = 350)

        obj.buttonframe = Frame(obj.window, bg = "#ffffff")
        obj.buttonframe.place(x = 315, y = 630, width = 450, height = 65)
        obj.allframes.append(obj.formframe)
        obj.allframes.append(obj.buttonframe)

        #Generate product button and product form 
        Admin_Films_create.generate_films_button(obj)
        Admin_Films_create.generate_films_form(obj)

    @staticmethod
    def generate_products_form(obj):
        # create form in form frame
        obj.product_id = StringVar()

        api = Api.Admin_Api()
        obj.product_id.set(api.get_last_prod_id())
        
        assets_path = Path(r"D:\do-an-cuoi-ki-nhom-2\Images\Admin\Component\Films")
        
        obj.background_img = PhotoImage(file=assets_path / "Background.png")
        obj.background = obj.background_img.create_image(342.0, 246.0, image=obj.background_img)

        obj.entry_image = PhotoImage(file=assets_path / "Textbox.png")
        obj.film_id_entry = Entry(obj.formframe, bd=0, bg="#D9D9D9", fg="#000716", highlightthickness=0, textvariable = obj.product_id)
        obj.film_id_entry.place(x=258.0, y=196.0, width=285.0, height=24.0)

        obj.film_entry = Entry(obj.formframe, bd=0, bg="#D9D9D9", fg="#000716", highlightthickness=0)
        obj.film_entry.place(x=258.0, y=233.0, width=285.0, height=24.0)

        obj.genre_entry = Entry(obj.formframe, bd=0, bg="#D9D9D9", fg="#000716", highlightthickness=0)
        obj.genre_entry.place(x=258.0, y=271.0, width=285.0, height=24.0)

        obj.showtime_entry = Entry(obj.formframe, bd=0, bg="#D9D9D9", fg="#000716", highlightthickness=0)
        obj.showtime_entry.place(x=258.0, y=309.0, width=285.0, height=24.0)

        obj.price_entry = Entry(obj.formframe, bd=0, bg="#D9D9D9", fg="#000716", highlightthickness=0)
        obj.price_entry.place(x=258.0, y=347.0, width=285.0, height=35.0)

        obj.stock_entry = Entry(obj.formframe, bd=0, bg="#D9D9D9", fg="#000716", highlightthickness=0)
        obj.stock_entry.place(x=258.0, y=385.0, width=285.0, height=24.0)

    @staticmethod
    def generate_products_button(obj):
        assets_path = Path(r"D:\do-an-cuoi-ki-nhom-2\Images\Admin\Component\Films")

        obj.addfilm_image = PhotoImage(file=assets_path / "Button_Addfilm.png")
        obj.remove_image = PhotoImage(file=assets_path / "Button_Remove.png")

        obj.addfilm_button = Button(image=obj.addfilm_image, borderwidth=0, highlightthickness=0,
                               command=lambda: app.Admin_Films_process.addfilm_button_handle(obj))
        obj.addfilm_button.place(x=219.0, y=448.0, width=104.0, height=28.0)

        obj.remove_button = Button(image=obj.remove_image, borderwidth=0, highlightthickness=0,
                               command=lambda: app.Admin_Films_process.remove_button_handle(obj))
        obj.remove_button.place(x=361.0, y=448.0, width=104.0, height=28.0)



        # self.background_img = PhotoImage(file=assets_path / "Background.png")
        # self.films_image = PhotoImage(file=assets_path / "Button_Films.png")
        # self.inventory_image = PhotoImage(file=assets_path / "Button_Inventory.png")
        # self.sales_image = PhotoImage(file=assets_path / "Button_Sales.png")
        # self.users_image = PhotoImage(file=assets_path / "Button_Users.png")
        # self.switch_image = PhotoImage(file=assets_path / "Button_Switch.png")
        # self.exit_image = PhotoImage(file=assets_path / "Button_Exit.png")
        # self.entry_image = PhotoImage(file=assets_path / "Textbox.png")
        # self.addfilm_image = PhotoImage(file=assets_path / "Button_Addfilm.png")
        # self.remove_image = PhotoImage(file=assets_path / "Button_Remove.png")

        # self.background = self.background_img.create_image(342.0, 246.0, image=self.background_img)

        # self.films_button = Button(image=self.films_image, borderwidth=0, highlightthickness=0,
        #                        command=lambda: self.click_button("films"))
        # self.films_button.place(x=10.0, y=124.0, width=97.0, height=37.0)

        # self.inventory_button = Button(image=self.inventory_image, borderwidth=0, highlightthickness=0,
        #                        command=lambda: self.click_button("inventory"))
        # self.inventory_button.place(x=118.0, y=125.0, width=102.0, height=35.0)

        # self.sales_button = Button(image=self.sales_image, borderwidth=0, highlightthickness=0,
        #                        command=lambda: self.click_button("sales"))
        # self.sales_button.place(x=233.0, y=126.0, width=97.0, height=33.0)

        # self.users_button = Button(image=self.users_image, borderwidth=0, highlightthickness=0,
        #                        command=lambda: self.click_button("users"))
        # self.users_button.place(x=349.0, y=126.0, width=97.0, height=33.0)

        # self.switch_button = Button(image=self.switch_image, borderwidth=0, highlightthickness=0,
        #                        command=lambda: self.switch_account())
        # self.switch_button.place(x=461.0, y=126.0, width=97.0, height=33.0)

        # self.exit_button = Button(image=self.exit_image, borderwidth=0, highlightthickness=0,
        #                        command=lambda: self.exit_button())
        # self.exit_button.place(x=576.0, y=126.0, width=97.0, height=33.0)


        # self.entry_1 = self.canvas.create_image(400.5, 398.0, image=self.entry_image)

        # self.entry_2 = self.canvas.create_image(400.5, 360.0, image=self.entry_image)

        # self.entry_3 = self.canvas.create_image(400.5, 322.0, image=self.entry_image)

        # self.entry_4 = self.canvas.create_image(400.5, 284.0, image=self.entry_image)

        # self.entry_5 = self.canvas.create_image(400.5, 246.0, image=self.entry_image)

        

        # self.addfilm_button = Button(image=self.addfilm_image, borderwidth=0, highlightthickness=0,
        #                        command=lambda: app.Admin_Films_process.addfilm_button_handle(self))
        # self.addfilm_button.place(x=219.0, y=448.0, width=104.0, height=28.0)

        # self.remove_button = Button(image=self.remove_image, borderwidth=0, highlightthickness=0,
        #                        command=lambda: app.Admin_Films_process.remove_button_handle(self))
        # self.remove_button.place(x=361.0, y=448.0, width=104.0, height=28.0)
        # # self.window.resizable(0, 0)
