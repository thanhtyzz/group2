from tkinter import *
from pathlib import Path
import Service.Widget_service as ws 
import Modules.Admin.Component.Sales.Admin_Sales_process as asp
import Modules.Admin.Component.Admin_Main_View as amv
import Api.Admin_Api as Api
from tkinter import ttk

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

    @staticmethod 
    def generate_sales(obj): 
        # clear all frames 
        for frame in obj.allframes: 
            frame.destroy() 
        obj.allframes = [] 
    
        #create search frame 
        obj.searchframe = Frame(obj.window, bg = '#fccde0') 
        obj.searchframe.place(x = 80, y = 250, width = 900, height = 50) 
        obj.allframes.append(obj.searchframe) 

        #create table frame 
        obj.tableframe = Frame(obj.window, bg = '#D9D9D9') 
        obj.tableframe.place(x = 40, y = 150, width = 600, height = 200)
        obj.allframes.append(obj.tableframe)

        Admin_Sales_create.generate_search(obj)
        Admin_Sales_create.generate_invoices_table(obj)

    @staticmethod 
    def generate_search(obj): 
        api = Api.Admin_Api() 

        all_invoices = api.get_all_invoices_data()
        list = []
        for data in all_invoices: 
            list.append(data['Invoice_ID']) 


        assets_path = Path(r"D:\do-an-cuoi-ki-nhom-2\Images\Admin\Sales")

        obj.canvas = Canvas(obj.window, bg="#FFFFFF", height=492, width=685, bd=0, highlightthickness=0, relief="ridge")
        obj.canvas.place(x=0, y=0)        
        obj.background_img = PhotoImage(file=assets_path / "Background.png")
        obj.background = obj.canvas.create_image(342.0, 246.0, image=obj.background_img)
        
        # obj.canvas.create_rectangle(362.0, 178.0, 441.0, 211.0, fill="#4269E2", outline="")
        # obj.canvas.create_rectangle(35.0, 178.0, 107.0, 211.0, fill="#4269E2", outline="")
        # obj.search_image = PhotoImage(file=assets_path / "Image_Search.png")
        # obj.search_image = obj.canvas.create_image(342.0, 246.0, image=obj.search_image)

        # obj.visualize_image = PhotoImage(file=assets_path / "Image_Visualize.png")
        # obj.visualize_image = obj.canvas.create_image(342.0, 246.0, image=obj.visualize_image)

        obj.entry_image = PhotoImage(file=assets_path / "Textbox.png")
        
        obj.entry_1 = obj.canvas.create_image(514.0, 195.0, image=obj.entry_image)
        obj.entry_1 = Entry(obj.canvas, bd=0, bg="#FCCBCB", fg="#000716", highlightthickness=0)
        obj.entry_1.place(x=441.0, y=179.0, width=146.0, height=30.0)

        obj.entry_2 = obj.canvas.create_image(180.0, 195.0, image=obj.entry_image)
        obj.entry_2 = Entry(obj.canvas, bd=0, bg="#FCCBCB", fg="#000716", highlightthickness=0)
        obj.entry_2.place(x = 107, y = 179, width = 146, height = 30) 

        obj.search_image = PhotoImage(file=assets_path / "Button_Search.png")
        obj.visualize_image = PhotoImage(file=assets_path / "Button_Visualize.png")
        obj.search_button = Button(obj.canvas, image=obj.search_image, borderwidth=0, highlightthickness=0,
                               command=lambda:  asp.Admin_Sales_process.search_button_handle(obj))
        obj.search_button.place(x=253.0, y=178.0, width=64.0, height=33.0)

        obj.visualize_button = Button(obj.canvas, image=obj.visualize_image, borderwidth=0, highlightthickness=0,
                               command=lambda: asp.Admin_Sales_process.visualize_button_handle(obj))
        obj.visualize_button.place(x=587.0, y=178.0, width=64.0, height=33.0)

        obj.films_image = PhotoImage(file=assets_path / "Button_Films.png")
        obj.inventory_image = PhotoImage(file=assets_path / "Button_Inventory.png")
        obj.sales_image = PhotoImage(file=assets_path / "Button_Sales.png")
        obj.users_image = PhotoImage(file=assets_path / "Button_Users.png")
        obj.switch_image = PhotoImage(file=assets_path / "Button_Switch.png")
        obj.exit_image = PhotoImage(file=assets_path / "Button_Exit.png")

        obj.films_button = Button(obj.canvas, image=obj.films_image, borderwidth=0, highlightthickness=0,
                               command=lambda: amv.Admin_Main_View.click_button(obj, "films"), relief="flat")
        obj.films_button.place(x=10.0, y=124.0, width=97.0, height=37.0)

        obj.inventory_button = Button(obj.canvas, image=obj.inventory_image, borderwidth=0, highlightthickness=0,
                               command=lambda: amv.Admin_Main_View.click_button(obj, "inventory"), relief="flat")
        obj.inventory_button.place(x=118.0, y=125.0, width=102.0, height=35.0)

        obj.sales_button = Button(obj.canvas, image=obj.sales_image, borderwidth=0, highlightthickness=0,
                               command=lambda: amv.Admin_Main_View.click_button(obj, "sales"), relief="flat")
        obj.sales_button.place(x=233.0, y=126.0, width=97.0, height=33.0)

        obj.users_button = Button(obj.canvas, image=obj.users_image, borderwidth=0, highlightthickness=0,
                               command=lambda: amv.Admin_Main_View.click_button(obj, "users"), relief="flat")
        obj.users_button.place(x=349.0, y=126.0, width=97.0, height=33.0)

        obj.switch_button = Button(obj.canvas, image=obj.switch_image, borderwidth=0, highlightthickness=0,
                               command=lambda: amv.Admin_Main_View.switch_account(obj), relief="flat")
        obj.switch_button.place(x=461.0, y=126.0, width=97.0, height=33.0)

        obj.exit_button = Button(obj.canvas, image=obj.exit_image, borderwidth=0, highlightthickness=0,
                               command=lambda: amv.Admin_Main_View.exit(obj), relief="flat")
        obj.exit_button.place(x=576.0, y=126.0, width=97.0, height=33.0)


        obj.window.resizable(0, 0)

    @staticmethod
    def generate_invoices_table(obj):
        def clickprodtable(event):
            # get selected film
            cur = obj.tree.selection()
            cur = obj.tree.item(cur)
            try:
                obj.selected_invoice = cur['values']
                obj.invoice_id.set(cur['values'][1])
                obj.date.set(cur['values'][2])
                obj.product_id.set(cur['values'][3])
                obj.product_name.set(cur['values'][4])
                obj.quantity.set(cur['values'][5])
                obj.price.set(cur['values'][6])
            except:
                pass
    
        # create tree view
        obj.tree = ttk.Treeview(obj.tableframe, columns = ("Invoice_ID", "Invoice_Date", "Film_ID", "Film", "Quantity", "Price"))
        obj.tree.heading('#0')
        obj.tree.heading('#1', text='Invoice_ID')
        obj.tree.heading('#2', text='Invoice_Date')
        obj.tree.heading('#3', text='Film_ID')
        obj.tree.heading('#4', text='Film')
        obj.tree.heading('#5', text='Quantity')
        obj.tree.heading('#6', text='Price')

        obj.tree.column('#0', width=0)
        obj.tree.column('#1', width=100)
        obj.tree.column('#2', width=100)
        obj.tree.column('#3', width=100)
        obj.tree.column('#4', width=100)
        obj.tree.column('#5', width=100)
        obj.tree.column('#6', width=100)
        obj.tree.bind("<<TreeviewSelect>>", clickprodtable)

        # create scroll bar
        obj.scrollbary = ttk.Scrollbar(obj.tableframe, orient=VERTICAL, command=obj.tree.yview)

        obj.tree.pack(side=RIGHT, fill=BOTH)
        obj.scrollbary.pack(side=RIGHT, fill=Y)

        api = Api.Admin_Api()
        invoices = api.get_all_invoices_data()

        for invoice in invoices:
            obj.tree.insert('', 'end', values=(invoice['Invoice_ID'], invoice['Invoice_Date'], invoice['Film_ID'], invoice['Film'], invoice['Quantity'], invoice['Price']))
        obj.tree.pack(side=LEFT, fill=Y)    
        return obj.tree
        
        