from flask import Flask, session
from flask_socketio import SocketIO
from flask_login import LoginManager

from api.api_user import router_user
from functions.database_layer import Database
from models.User import User

app = Flask(__name__)
login_manager = LoginManager()

app.config['SECRET_KEY'] = 'secret_key'
socketio = SocketIO(app)
login_manager.init_app(app)


@login_manager.user_loader
def load_user(user_id):
    db = Database()
    result = db.get_one('uuid', user_id)
    id, uuid, first_name, last_name, email, password, profile_picture = result[0].values()

    user = User(first_name, last_name, email, password, profile_picture, uuid, id)

    return user


# APIS #
# User Api
app.register_blueprint(router_user)
# connect_db()

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')
