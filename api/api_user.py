from flask import Blueprint

router_user = Blueprint('api_user', __name__)


@router_user.route('/register', methods=['GET', 'POST'])
def register_user():
    pass


@router_user.route('/login', methods=['GET', 'POST'])
def login_user():
    pass
