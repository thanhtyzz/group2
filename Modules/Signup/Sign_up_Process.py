import Api.Login_Api as Login_Api
import Api.Signup_Api as Signup_Api
import Modules.Login.Login_View as loginview
from tkinter import END, messagebox as mbox


class Sign_up_Process: 
    
    # Hiện màn hình lựa chọn giữa đăng nhập (login) và đăng kí (signup)
    @staticmethod
    def login_button_handle(obj):
        obj.window.destroy()
        app = loginview.Login_View()
        app.window.mainloop()

    @staticmethod 
    def signup_button_handle(obj): 
        username = obj.username_entry.get()
        password = obj.password_entry.get()
        reenterpassword = obj.reenterpass_entry.get()
        api = Signup_Api.Signup_Api()
        error = api.check_user_signup(username,password,reenterpassword)
        standard_pass = api.check_password_standard(password, username)

        if error == -1:
            mbox.showerror('Warning','Invalid User Input')
            obj.username_entry.delete(0, END)
            obj.password_entry.delete(0, END)
            obj.reenterpass_entry.delete(0, END)

        elif error == -2:
            mbox.showerror('Warning', 'Password is not the same')
            obj.username_entry.delete(0, END)
            obj.password_entry.delete(0, END)
            obj.reenterpass_entry.delete(0, END)

        elif error == -3:
            mbox.showerror('Warning', 'Existed user')
            obj.username_entry.delete(0, END)
            obj.password_entry.delete(0, END)
            obj.reenterpass_entry.delete(0, END)
            
        else:
            if standard_pass == 1:
                mbox.showerror('Mật khẩu yếu', 'Kí tự quá ngắn')
                obj.username_entry.delete(0, END)
                obj.password_entry.delete(0, END)
                obj.reenterpass_entry.delete(0, END)
            if standard_pass == 2:
                mbox.showerror('Mật khẩu chưa đủ tiêu chuẩn', 'Không có chữ cái viết hoa')
                obj.username_entry.delete(0, END)
                obj.password_entry.delete(0, END)
                obj.reenterpass_entry.delete(0, END)
            if standard_pass == 3:
                mbox.showerror('Mật khẩu chưa đủ tiêu chuẩn', 'Không có chữ cái viết thường')
                obj.username_entry.delete(0, END)
                obj.password_entry.delete(0, END)
                obj.reenterpass_entry.delete(0, END)
            if standard_pass == 4:
                mbox.showerror('Mật khẩu chưa đủ tiêu chuẩn', 'Cần thêm kí tự đặc biệt')
                obj.username_entry.delete(0, END)
                obj.password_entry.delete(0, END)
                obj.reenterpass_entry.delete(0, END)
            if standard_pass == 5:
                mbox.showerror('Mật khẩu chưa đủ tiêu chuẩn', 'Cần thêm kí tự chữ cái')
                obj.username_entry.delete(0, END)
                obj.password_entry.delete(0, END)
                obj.reenterpass_entry.delete(0, END)
            if standard_pass == 6:
                mbox.showerror('Mật khẩu chưa đủ tiêu chuẩn', 'Cần thêm chữ số')
                obj.username_entry.delete(0, END)
                obj.password_entry.delete(0, END)
                obj.reenterpass_entry.delete(0, END)
            else:
                mbox.showinfo('Success', 'Account created successfully')
                obj.username_entry.delete(0, END)
                obj.password_entry.delete(0, END)
                obj.reenterpass_entry.delete(0, END)
