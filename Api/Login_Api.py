import Api.Main_Api as main_api


class Login_Api(main_api.Api):

    def __init__(self):
        super().__init__()
        self.connector()

    # user login api
    def check_user_login(self, username, password):
        if username == "" or password == "":
            return -1  # error 1: username or password is empty
        user = self.users_collection.find_one({'username': username})
        if user == None:
            return -2  # error 2: user not found
        if user["password"] != password:
            return -3  # error 3: password is wrong
        return user["roles"]