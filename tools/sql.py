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
def check(usr, pas, con):
    """
    Check if the user exists
    :param usr: user hash string
    :type usr: str
    :param pas: password hash string
    :type pas: str
    :param con: connection object
    :return: true if user exists and false otherwise
    :rtype: int
    """
    connection = con
    cursor = connection.cursor()
    query = "SELECT username FROM users WHERE username = %s LIMIT 1"
    cursor.execute(query, (usr,))
    # if email is in database
    if cursor.fetchone():
        query = "SELECT password FROM users WHERE password = %s AND username = %s LIMIT 1"
        cursor.execute(query, (pas, usr))
        # email is in database but password is not
        status = 2
        if cursor.fetchone():
            # email and password are in database
            status = 0
    else:
        # email is not in database
        status = 1
    return status

"""
Adding the skeleton to functions checkEmail and checkPassword
that will be accessed by application.
"""

def checkEmail(email, con):
    cursor = con.cursor()
    query = f'SELECT username FROM users WHERE username = "{email}" LIMIT 1'

    cursor.execute(query)    

    if cursor.fetchone(): return True
    else: return False

def checkPassword(pwd, con):
    cursor = con.cursor()
    query = f'SELECT password FROM users WHERE password = "{pwd}" LIMIT 1'

    cursor.execute(query)    

    if cursor.fetchone(): return True
    else: return False

