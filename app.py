from flask import Flask, render_template, request, redirect, url_for, flash, jsonify, session
import sqlite3
from passlib.hash import sha256_crypt
import secrets
from flask_wtf import FlaskForm
from wtforms import SelectField
import mysql.connector as mysql
from mysql.connector import Error
import pandas as pd
import schema
from dotenv import load_dotenv
import os

load_dotenv()

app = Flask(__name__)
app.secret_key = 'some_secret'
app.config['FLASK_ENV'] = 'development'
app.config['DEBUG'] = True

config = {
    'host': os.getenv('MYSQL_HOST'),
    'port': 3306,
    'user': os.getenv('MYSQL_USER'),
    'password': os.getenv('MYSQL_PASSWORD'),
    'database': os.getenv('MYSQL_DATABASE')
}

def get_db_conn():
    try:
        conn = mysql.connect(**config)
        return conn
    except Error as e:
        return "<html><body><h1>500 Internal Server Error</h1></body></html>"

class Form(FlaskForm):
    choices = SelectField('choice', choices=['SELECT', 'INSERT', 'UPDATE', 'DELETE', 'CREATE', 'ALTER', 'DROP'])

schema.create_database(get_db_conn())
schema.create_user_table(get_db_conn())

@app.route('/', methods=['GET'])
def login():
    return render_template('login.html')

@app.route('/login', methods=['POST', 'GET'])
def login_post():
    conn = get_db_conn()
    cur = conn.cursor()
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        with app.app_context():
            cur.execute(f"SELECT * FROM users WHERE username = '{username}'")
            user = cur.fetchone()
            if user is None:
                flash('Username not found', 'danger')
                return redirect(url_for('login'))
            else:
                if sha256_crypt.verify(password, user[2]):
                    session['logged_in'] = True
                    session['username'] = username
                    flash('You are now logged in', 'success')
                    return redirect(url_for('analyzer'))
                else:
                    flash('Invalid password', 'danger')
                    return redirect(url_for('login'))
    
    return render_template('login.html')

@app.route('/register', methods=['POST', 'GET'])
def register():
    conn = get_db_conn()
    cur = conn.cursor()
    msg = ''
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        password_confirm = request.form['password_confirm']

        # checking if username is already registered
        with sqlite3.connect('user.db') as con:
            cur.execute(f"SELECT * FROM users WHERE username = '{username}'")
            users = cur.fetchone()
        if users is not None:
            msg = "Username already exists"
        if password == password_confirm:
            password = sha256_crypt.hash(password)
            try:
               with app.app_context():
                    schema.insert_user(conn, username, password)
                    msg = "Registered Successfully"
        
            except:
                msg = "Username already exists"
        # elif username in users:
        #     msg = "Username already exists"
        else:
            msg = "Password don't match"
    return render_template('register.html', msg=msg, csrf_token=secrets.token_hex(16))

@app.route('/logout')
def logout():
    session.clear()
    flash('You are now logged out', 'success')
    return redirect(url_for('login'))

@app.route('/analyzer', methods=['GET', 'POST'])
def analyzer():
    # choices = []
    form = Form()
    if request.method == 'POST':
        hostname = request.form['host']
        db_name = request.form['database']
        user = request.form['user']
        password = request.form['password']
        query = request.form['query']
        choice = (form.choices.data)

        print(choice)

        try:
            with mysql.connect(host=hostname, user=user, password=password, database=db_name) as conn:
                cur = conn.cursor()
                print("Connected to database")
                if choice == 'SELECT':
                    cur.execute(query)
                    results = cur.fetchall()
                    columns = [i[0] for i in cur.description]
                    # col_length = len(columns)
                    data = pd.DataFrame(results, columns=columns)
                    return render_template('analyzer.html', results=results, form=form, data = data.to_html())
                elif choice == 'INSERT' or choice == 'UPDATE' or choice == 'DELETE' or choice == 'CREATE' or choice == 'ALTER' or choice == 'DROP':
                    cur.execute(query)
                    conn.commit()
                    return render_template('analyzer.html', form=form)
                
                else:
                    return render_template('analyzer.html', form=form)
                
        except:
            return render_template('analyzer.html', form=form)
        
    
    return render_template('analyzer.html', form=form)

if __name__ == '__main__':
    app.run(debug=True, port=5000, host='0.0.0.0')

