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
        print ("Error occurred:", e)