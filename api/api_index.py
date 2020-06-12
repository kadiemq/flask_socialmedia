from flask import Blueprint, render_template, redirect
from flask_login import current_user

router_index = Blueprint('router_index', __name__)


@router_index.route('/')
def index():
    if not current_user.is_authenticated:
        return redirect('/login')

    return render_template('index.html')
