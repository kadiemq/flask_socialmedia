from functions.database_layer import Database
from models.User import User


def fn_login_user(param, value, passed_password):
    db = Database()
    result = db.get_one(param, value)

    id, uuid, first_name, last_name, email, password, profile_picture = result[0].values()

    user = User(first_name, last_name, email, password, profile_picture, uuid, id)

    with user as u:
        if not u.check_password(passed_password):
            raise Exception('Wrong Password')
            # return 'Wrong Password'

        return user
