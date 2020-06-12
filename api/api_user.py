import psycopg2
from flask import Blueprint, render_template, request, jsonify, session, redirect, url_for
from flask_login import login_user, login_required, logout_user, current_user

from functions.fn_login_user import fn_login_user
from functions.fn_save_user import fn_save_user
from models.User import User

router_user = Blueprint('api_user', __name__)


@router_user.route('/register', methods=['GET', 'POST'])
def api_register_user():
    if current_user.is_authenticated:
        return redirect('/')

    method = request.method

    if method == 'GET':
        return render_template('register.html')

    else:
        try:
            result = fn_save_user(request)
            return jsonify(result)

        except psycopg2.IntegrityError as e:
            # print(f'{e} database error')
            return jsonify('That email is already registered'), 409

        except Exception as e:
            print(e)
            return jsonify(e.args)


@router_user.route('/login', methods=['GET', 'POST'])
def api_login_user():
    if current_user.is_authenticated:
        return redirect('/')

    method = request.method

    if method == 'GET':
        return render_template('login.html')

    else:
        try:
            # TODO: Check For credentials
            email, password = request.json.values()
            user = fn_login_user('email', email, password)

            login_user(user)
            session.permanent = True
            return jsonify({"redirect": "/"})

        except Exception as e:
            print(e)
            return jsonify(e.args), 401


@router_user.route('/logout', methods=['GET', 'POST'])
@login_required
def api_logout():
    logout_user()
    return 'Logged Out'
