# test.py
# Author: Colin Gasiewicz <gasiewca@clarkson.edu>
#
# Description: This script tests some of the database calls
# and validates the data integrity
import sql
import hashlib


if __name__ == '__main__':
    con = sql.connect()
    # Testing with known hash in database
    user_hash = "000000f1a6959fcbbb21610fcdc72110d4f48c9b40ca210526873109d6d50dd3"
    password_hash = "1255d15145191c57bc0b2fad63edfba28eb9431052b16f047deb959663250840"
    res = sql.check(user_hash, password_hash, con)
    print("sql.check.test 1 : valid username & password\n"
          "expected 0 : result ", res)
    res = sql.check(user_hash, "", con)
    print("sql.check.test 2 : valid username invalid password\n"
          "expected 2 : result ", res)
    res = sql.check("cnou1qond", password_hash, con)
    print("sql.check.test 3 : invalid username & password\n"
          "expected 1 : result ", res)
    # test with plain text email and password
    plainTextEmail = "dominic.dominguez97@yahoo.com"
    # BUG: password stored in database with "\n" character on the end
    plainTextPassword = "tombrady\n"
    print("Test with plaintext email: ", plainTextEmail, "and plaintext password: ", plainTextPassword)
    hashEmail = hashlib.sha256(plainTextEmail.encode('utf-8'), usedforsecurity=True).hexdigest()
    hashPassword = hashlib.sha256(plainTextPassword.encode('utf-8'), usedforsecurity=False).hexdigest()
    print("Email hash: ", hashEmail, "Password hash: ", hashPassword)
    res = sql.check(hashEmail, hashPassword, con)
    print("sql.check.test 4 : checking known plaintext email & password\n"
          "expected 0 : result ", res)

