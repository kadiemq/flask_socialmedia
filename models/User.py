import bcrypt
from datetime import *


class User:
    def __init__(self, first_name, last_name, email, password, profile_picture="None", uuid='None', id='None'):
        self.is_active = True
        self.is_authenticated = True
        self.first_name = first_name
        self.last_name = last_name
        self.email = email
        self.password = password
        self.profile_picture = profile_picture
        self.uuid = uuid
        self.id = id
        # self.uuid = self.first_name[0].upper() + self.last_name[0].upper() + str(time.day) + str(time.hour) + str(
        #     time.microsecond)

    def __enter__(self):
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        return

    def hash_password(self):
        self.password = bcrypt.hashpw(self.password.encode('utf8'), bcrypt.gensalt()).decode('utf8')

    def gen_uuid(self):
        time = datetime.now()
        self.uuid = self.first_name[0].upper() + self.last_name[0].upper() + str(time.day) + str(time.hour) + str(time.microsecond)

    def check_password(self, passed_password):
        return bcrypt.checkpw(passed_password.encode('utf8'), self.password.encode('utf8'))

    def get_id(self):
        return self.uuid

    # def is_authenticated(self):
    #     return self.is_authenticated
