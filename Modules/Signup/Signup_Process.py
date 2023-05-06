import Api.Login_Api as Login_Api
import Api.Signup_Api as Signup_Api
import Modules.Login.Login_View as loginview
from tkinter import END, messagebox as mbox


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
        reenterpassword = obj.reenterpass_entry.get()
        api = Signup_Api.Signup_Api()
        error = api.check_user_signup(username,password,reenterpassword)
        standard_pass = api.check_user_signup(password, username)

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
