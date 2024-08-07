import os
import time

from cs50 import SQL
from flask import Flask, flash, jsonify, redirect, render_template, request, session, flash
from flask_session import Session
from werkzeug.security import check_password_hash, generate_password_hash

from helpers import login_required

app = Flask(__name__)

app.config["SESSION_PERMANENT"] = False
app.config["SESSION_TYPE"] = "filesystem"
Session(app)

db = SQL("sqlite:///data.db")

@app.route('/home')
@login_required
def index():
    return render_template('index.html')


@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']

        if not username:
            flash('Username required!')

        elif not password:
            flash('Password required!')

        else:
            user = db.execute("SELECT * FROM users WHERE username = ?", username)

            if len(user) != 1 or not check_password_hash(user[0]['password'],password):
                flash('Invalid Username or Password')
                print('Invalid Username or Password')
            else:
                session['user_id'] = user[0]['id']
                return redirect('/home')


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

        if not username:
            flash('Username required!')

        elif not password1:
            flash('Password required!')

        elif not password2:
            flash('Confirm Password required!')

        elif password1 != password2:
            flash('Passwords do not match!')

        else:
            hash = generate_password_hash(password1)

            db.execute("INSERT INTO users (username, password) VALUES(?, ?)", username, hash)
            flash('Registeration Succesful!')
            return redirect('/login')

    else:
        return render_template('signup.html')
