import sys
sys.path.append("Users.User.PycharmProjects.FinalTerm.Modules.Login.Login_View")
import Modules.Login.Login_View as lgv
if __name__ == "__main__":
    print("hehehehe")
    app = lgv.Login_View()
    app.window.mainloop()