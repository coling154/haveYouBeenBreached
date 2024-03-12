"""
input.py
Created by Colin Gasiewicz on 03/06/2024
This is for project1 part 1 of EE468
This script inserts data into the users database from credentials1.txt & credentials2.txt
"""
import hashlib
import sql
import time
file1 = "../data/credentials1.txt"
file2 = "../data/credentials2.txt"


def write_to_db(file):
    DBcon = sql.connect()
    with open(file, 'r', encoding='utf-8') as file:
        for line in file:
            parts = line.split(":")
            # Hash email and password
            user = hashlib.sha256(parts[0].encode('utf-8'), usedforsecurity=True).hexdigest()
            password = hashlib.sha256(parts[1].encode('utf-8'), usedforsecurity=True).hexdigest()
            # Insert Hashed data into database
            sql.insert(user, password, DBcon)
            # Print out data
            print(user, password)
        DBcon.close()


def write_to_db2(file):
    DBcon = sql.connect()
    with open(file, 'r', encoding='utf-8') as file:
        buffer = []
        for line in file:
            parts = line.split(":")
            # Hash email and password
            user = hashlib.sha256(parts[0].encode('utf-8'), usedforsecurity=True).hexdigest()
            password = hashlib.sha256(parts[1].encode('utf-8'), usedforsecurity=True).hexdigest()
            if len(buffer) >= 5:
                sql.fast_insert(buffer, DBcon)
            tup = (user, password)
            buffer.append(tup)
            # Print out data
            print(user, password)
        DBcon.close()


if __name__ == '__main__':
    startTime = time.time()
    write_to_db2(file1)
    write_to_db2(file2)
    endTime = time.time()
    print("Total time: " + str(endTime - startTime))