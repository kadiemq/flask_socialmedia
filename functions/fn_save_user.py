from functions.database_layer import Database
from models.User import User


def fn_save_user(request):
    # db = Database(user.first_name, user.last_name, user.email, user.password)
    db = Database()
    first_name, last_name, email, password = request.json.values()
    user = User(first_name, last_name, email, password)
    user.hash_password()
    user.gen_uuid()

    result = db.save_user(user)
    return result
