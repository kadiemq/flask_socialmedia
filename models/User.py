class User:
    def __init__(self, first_name, last_name, email, password, profile_pic):
        self.first_name = first_name
        self.last_name = last_name
        self.email = email
        self.password = password
        self.profile_pic = profile_pic
        pass

    def hashPassword(self):
        pass

    def check_password(self, pw):
        pass