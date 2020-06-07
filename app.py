from flask import Flask
from flask_socketio import SocketIO
from flask_login import LoginManager



import functions.db_fns.db_connect
from api.api_user import router_user


app = Flask(__name__)
login_manager = LoginManager()

app.config['SECRET_KEY'] = 'secret_key'
socketio = SocketIO(app)
login_manager.init_app(app)


@login_manager.user_loader
def load_user(user_id):
    # return User.get(user_id)
    pass


# APIS #
# User Api
app.register_blueprint(router_user)

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')
