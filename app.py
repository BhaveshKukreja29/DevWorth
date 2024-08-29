import os
import time

from cs50 import SQL
from flask import Flask, jsonify, redirect, render_template, request, session, flash
from flask_session import Session
from werkzeug.security import check_password_hash, generate_password_hash

from helpers import login_required

app = Flask(__name__)

app.config["SESSION_PERMANENT"] = False
app.config["SESSION_TYPE"] = "filesystem"
Session(app)

db = SQL("sqlite:///data.db")

@app.route('/')
@login_required
def index():
    return render_template('home.html')


@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']

        nameErr = None
        passErr = None

        if not username:
            nameErr = 'Username required!'
        elif not password:
            passErr = 'Password required!'
        else:
            user = db.execute("SELECT * FROM users WHERE username = ?", username)

            if len(user) == 0:
                nameErr = 'Invalid username'

            if len(user) != 1 or not check_password_hash(user[0]['password'], password):
                passErr = 'Invalid Password'
            else:
                session['user_id'] = user[0]['id']
                return redirect('/')

        return render_template('login.html', nameErr=nameErr, passErr=passErr)

    else:
        return render_template('login.html')

@app.route('/logout', methods=['POST'])
def logout():
    session.clear()
    return redirect('/login')

@app.route('/signup', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        username = request.form['username']
        password1 = request.form['password1']
        password2 = request.form['password2']

        user = db.execute("SELECT * FROM users WHERE username = ?", username)

        nameErr = None
        passErr = None
        pass2Err = None
        passMatch = None

        if len(user) > 0:
            nameErr = 'User already exists'

        elif not username:
            nameErr = 'Username required!'

        elif not password1:
            passErr = 'Password required!'

        elif not password2:
            pass2Err = 'Confirm Password required!'

        elif password1 != password2:
            passMatch = 'Passwords do not match!'

        else:
            hash = generate_password_hash(password1)

            db.execute("INSERT INTO users (username, password) VALUES(?, ?)", username, hash)

            return redirect('/login')

        return render_template('signup.html', nameErr = nameErr,
        passErr = passErr,
        pass2Err = pass2Err,
        passMatch = passMatch)

    else:
        return render_template('signup.html')
