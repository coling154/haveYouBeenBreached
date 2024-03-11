import sql
if __name__ == '__main__':
    con = sql.connect()
    user_hash = "000000f1a6959fcbbb21610fcdc72110d4f48c9b40ca210526873109d6d50dd3"
    password_hash = "1255d15145191c57bc0b2fad63edfba28eb9431052b16f047deb959663250840"
    res = sql.check(user_hash, password_hash, con)
    print("sql.check.test 1 : valid username & password : expected 0")
    print(res)
    res = sql.check(user_hash, "", con)
    print("sql.check.test 2 : valid username invalid password : expected 2")
    print(res)
    res = sql.check("cnou1qond", password_hash, con)
    print("sql.check.test 3 : invalid username & password : expected 1")
    print(res)