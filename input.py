"""
input.py
Created by Colin Gasiewicz on 03/06/2024
This is for project1 part 1 of EE468
This script inserts data into the users database from data.txt
"""
import hashlib
import sql
file = "../data/data.txt"
DBcon = sql.connect()
with open(file, 'r', encoding='utf-8') as file:
    for line in file:
        parts = line.split(":")
        user = parts[0]
        password = hashlib.sha256(parts[1].encode('utf-8'), usedforsecurity=True).hexdigest()
        sql.insert(user, password, DBcon)
        print(user, password)
    DBcon.close()
