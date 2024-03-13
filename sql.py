"""
sql.py
Created by Colin Gasiewicz on 03/06/2024
This script compliments input.py
it contains sql functions to interface with the database
such as inserting and searching the data
"""
import mysql.connector
from mysql.connector import IntegrityError, Error


def connect():
    """
    Connect to the database
    :return: connection object
    """
    try:
        conn = mysql.connector.connect(
            host='localhost',
            user='root',
            password='',
            database='users'
        )
        if conn.is_connected():
            return conn
    except mysql.connector.Error as e:
        print(e)


def insert(usr, pas, con):
    """
    Insert data into the database

    :param usr: String with the username
    :param pas: String with the password
    :param con: Connection object
    """
    connection = con
    cursor = connection.cursor()
    try:
        query = "INSERT INTO users (username, password) VALUES (%s, %s)"
        cursor.execute(query, (usr, pas))
        connection.commit()
    except IntegrityError as e:
        print("IntegrityError occurred:", e)
        print("User already exists: " + usr)
    except Error as e:
        print("Error occurred:", e)


def checkEmail(email, con):
    """
    This function will ensure if an email is in the database

    :param email: hash of email address
    :type email: str
    :param con: connection object
    :return: True if email is in the database, False otherwise
    :rtype: bool
    """
    cursor = con.cursor()
    query = f'SELECT username FROM users WHERE username = "{email}" LIMIT 1'

    cursor.execute(query)

    return bool(cursor.fetchone())


def checkPassword(pwd, con):
    """
    This function will ensure if a password is in the database

    :param pwd: hash of password
    :type pwd: str
    :param con: connection object
    :return: True if password is in database, False otherwise
    """
    cursor = con.cursor()
    query = f'SELECT password FROM users WHERE password = "{pwd}" LIMIT 1'

    cursor.execute(query)

    return bool(cursor.fetchone())

