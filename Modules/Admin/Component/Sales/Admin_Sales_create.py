from tkinter import *
from pathlib import Path
import Service.Widget_service as ws 
import Modules.Admin.Component.Sales.Admin_Sales_process as asp
import Api.Admin_Api as Api

class Admin_Sales_create:
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
        self.window.configure(bg="#FFFFFF")
        self.window.title("Admin")

        self.canvas = Canvas(self.window, bg="#FFFFFF", height=492, width=685, bd=0, highlightthickness=0, relief="ridge")
        self.canvas.place(x=0, y=0)

        assets_path = Path(r"D:\do-an-cuoi-ki-nhom-2\Images\Admin\Component\Sales")

        self.background_img = PhotoImage(file=assets_path / "Background.png")
        self.films_image = PhotoImage(file=assets_path / "Button_Films.png")
        self.inventory_image = PhotoImage(file=assets_path / "Button_Inventory.png")
        self.sales_image = PhotoImage(file=assets_path / "Button_Sales.png")
        self.users_image = PhotoImage(file=assets_path / "Button_Users.png")
        self.switch_image = PhotoImage(file=assets_path / "Button_Switch.png")
        self.exit_image = PhotoImage(file=assets_path / "Button_Exit.png")
        self.entry_image = PhotoImage(file=assets_path / "Textbox.png")
        self.search_image = PhotoImage(file=assets_path / "Button_Search.png")
        self.visualize_image = PhotoImage(file=assets_path / "Button_Visualize.png")

        self.background = self.background_img.create_image(342.0, 246.0, image=self.background_img)

        self.films_button = Button(image=self.films_image, borderwidth=0, highlightthickness=0,
                               command=lambda: asp.Admin_Sales_process.films_button_handle(self))
        self.films_button.place(x=10.0, y=124.0, width=97.0, height=37.0)

        self.inventory_button = Button(image=self.inventory_image, borderwidth=0, highlightthickness=0,
                               command=lambda: asp.Admin_Sales_process.inventory_button_handle(self))
        self.inventory_button.place(x=118.0, y=125.0, width=102.0, height=35.0)

        self.sales_button = Button(image=self.sales_image, borderwidth=0, highlightthickness=0,
                               command=lambda: asp.Admin_Sales_process.sales_button_handle(self))
        self.sales_button.place(x=233.0, y=126.0, width=97.0, height=33.0)

        self.users_button = Button(image=self.users_image, borderwidth=0, highlightthickness=0,
                               command=lambda: asp.Admin_Sales_process.users_button_handle(self))
        self.users_button.place(x=349.0, y=126.0, width=97.0, height=33.0)

        self.switch_button = Button(image=self.switch_image, borderwidth=0, highlightthickness=0,
                               command=lambda: asp.Admin_Sales_process.switch_button_handle(self))
        self.switch_button.place(x=461.0, y=126.0, width=97.0, height=33.0)

        self.exit_button = Button(image=self.exit_image, borderwidth=0, highlightthickness=0,
                               command=lambda: asp.Admin_Sales_process.exit_button_handle(self))
        self.exit_button.place(x=576.0, y=126.0, width=97.0, height=33.0)


        self.entry_1 = self.canvas.create_image(514.0, 195.0, image=self.entry_image)
        self.entry_1 = Entry(bd=0, bg="#FCCBCB", fg="#000716", highlightthickness=0)
        self.entry_1.place(x=441.0, y=179.0, width=146.0, height=30.0)

        self.entry_2 = self.canvas.create_image(180.0, 195.0, image=self.entry_image)
        self.entry_2 = Entry(bd=0, bg="#FCCBCB", fg="#000716", highlightthickness=0)
        self.entry_2.place(x=107.0, y=179.0, width=146.0, height=30.0)


        self.search_button = Button(image=self.search_image, borderwidth=0, highlightthickness=0,
                               command=lambda:  asp.Admin_Sales_process.search_button_handle(self))
        self.search_button.place(x=253.0, y=178.0, width=64.0, height=33.0)

        self.visualize_button = Button(image=self.visualize_image, borderwidth=0, highlightthickness=0,
                               command=lambda: asp.Admin_Sales_process.visualize_button_handle(self))
        self.visualize_button.place(x=587.0, y=178.0, width=64.0, height=33.0)
        self.window.resizable(0, 0)

    @staticmethod 
    def generate_treeview(obj): 
        api = Api.Admin_Api() 
        #create a tree view 
        obj.tree = ttk.Treeview(obj.tableframe, columns = ("Invoice_Id", "InvoiceDate", "Films_id", "Films", "Quantity", "Price"), height=10)
        obj.tree.place(x = 0, y = 0, width = 1000, height = 400)
        obj.tree.heading("#0") 
        obj.tree.heading("Invoice_Id", text = "Invoice_Id") 
        obj.tree.heading("InvoiceDate", text = "InvoiceDate") 
        obj.tree.heading("Films_id", text = "Films_id")
        obj.tree.heading("Films", text = "Films")
        obj.tree.heading("Quantity", text = "Quantity")
        obj.tree.heading("Price", text = "Price")

        obj.tree.column("#0", width = 0, stretch =  False)
        obj.tree.column("Invoice_Id", width = 150, stretch = False)
        obj.tree.column("InvoiceDate", width = 150, stretch = False)
        obj.tree.column("Product_id", width = 150, stretch = False)
        obj.tree.column("Product_name", width = 150, stretch = False)
        obj.tree.column("Quantity", width = 150, stretch = False)
        obj.tree.column("Price", width = 150, stretch = False)

        data = api.get_all_invoices_data() 
        for row in data:
            obj.tree.insert('', 'end', values = (row['Invoice_Id'], row['InvoiceDate'], row['Films_id'], row['Films'], row['Quantity'], row['Price'])) 
