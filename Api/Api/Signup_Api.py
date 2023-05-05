import Api.Main_Api as main_api


class Signup_Api(main_api.Api):
    
    def __init__(self):
        super().__init__()
        self.connector()

    # user sign up api
    def check_user_signup(self, username, password, reenterpassword):
        if username == "" or password == "" or reenterpassword == "":
            return -1  # error 1: username or password is empty
        if password != reenterpassword:
            return -2  # error 2: password is not the same
        user = self.users_collection.find_one({'username': username})
        if user != None:
            return -3  # error 3: username is already exist
        self.users_collection.insert_one(
            {'username': username, 'password': password, 'roles': "User"})
        return 0  # success
