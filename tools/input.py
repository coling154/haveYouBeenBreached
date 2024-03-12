"""
input.py
Created by Colin Gasiewicz on 03/06/2024
This is for project1 part 1 of EE468
This script inserts data into the users database from credentials1.txt & credentials2.txt
"""
import hashlib
import sql
import time
file1 = "credentials1.txt"
file2 = "credentials2.txt"

def write_to_db(file):
    DBcon = sql.connect()
    with open(file, 'r', encoding='utf-8') as file:
        for line in file:
            try:   
                parts = line.split(":")
                # Hash email and password
                user = hashlib.sha256(parts[0].encode('utf-8'), usedforsecurity=True).hexdigest()
                password = hashlib.sha256(parts[1][:-1].encode('utf-8'), usedforsecurity=True).hexdigest()
                # Insert Hashed data into database
                sql.insert(user, password, DBcon)
                # Print out data
                print(user, password)
            except ValueError:
                print("VALUE: ", line)
            except Exception as e:
                print("ERROR: ", e)
        DBcon.close()
    file.close()


if __name__ == '__main__':
    startTime = time.time()
    write_to_db(file1)
    write_to_db(file2)
    endTime = time.time()
    print("Total time: " + str(endTime - startTime))

