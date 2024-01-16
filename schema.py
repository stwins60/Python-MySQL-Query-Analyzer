import sqlite3 as sql
import mysql.connector as mysql
from mysql.connector import Error
import os
from dotenv import load_dotenv


# conn = sql.connect('user.db')
# c = conn.cursor()

# query = 'CREATE TABLE IF NOT EXISTS users (id INTEGER PRIMARY KEY AUTOINCREMENT, username TEXT UNIQUE, password TEXT)'

# c.execute(query)
# print('Table user created')
# conn.commit()

# c.execute('SELECT * FROM users')
# print(c.fetchall())

load_dotenv()

def check_if_table_exists(conn, table_name):
    cursor = conn.cursor()
    cursor.execute(f"SHOW TABLES LIKE '{table_name}'")
    result = cursor.fetchone()
    if result:
        return True
    else:
        return False

def create_database(conn):
    try:
        cursor = conn.cursor()
        cursor.execute("CREATE DATABASE IF NOT EXISTS mysqlAnalyzer")
        print("Database has been created successfully")
    except Exception as e:
        print(e)

def create_user_table(conn):
    try:
        if check_if_table_exists(conn, "users"):
            print("User table already exists")
            return
        else:
            cursor = conn.cursor()
            query = """CREATE TABLE IF NOT EXISTS users(
            id INTEGER PRIMARY KEY AUTO_INCREMENT,
            username VARCHAR(50) NOT NULL UNIQUE,
            password VARCHAR(255) NOT NULL,
            created_at DATETIME DEFAULT CURRENT_TIMESTAMP
            );"""
            cursor.execute(query)
            print("user table has been created successfully")
    except Exception as e:
        print(e)


def insert_user(conn, username, password):
    try:
        cursor = conn.cursor()
        query = "INSERT INTO users(username, password) VALUES(%s, %s)"
        cursor.execute(query, (username, password))
        conn.commit()
        print("User has been inserted successfully")
    except Exception as e:
        print(e)