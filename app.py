# App.py
# Author: Ryan Quirk <ryan.quirk6@protonmail.ch>
#
# Description: This is the main flask application. This script
# initializes the app, and handles all http requests & api calls.
from flask import Flask, request, render_template, redirect, url_for, flash
import hashlib
import time
import sql
import re
app = Flask(__name__, static_folder="static")

app.config['SECRET_KEY'] = "secretkey"


# Landing page for app
@app.route('/')
def index():
   return render_template("landing.html")


@app.route('/submit', methods = ["POST"])
def check():
   if request.method == 'POST':
      if request.form['email'] == "" or request.form['password'] == "":
         flash("ALERT: Please enter email or password", "noFill")
         return redirect("/")

      email = request.form['email']
      password = request.form['password']
      # Hash password
      password = hashlib.sha256(password.encode('utf-8')).hexdigest()
      # Use regex to validate if input is a proper email
      if not re.search(r".+@.+\..*", email):
         flash("ALERT: Please enter valid email", "noFill")
         return redirect("/")

      start_time = time.time()
      # Hash the email
      email = hashlib.sha256(email.encode('utf-8')).hexdigest()
      # Check email
      if sql.checkEmail(email, con):
         # email is in db
         if sql.checkPassword(password, con):
            # password is in db
            flash("ALERT: Your account has been compromised consider changing passwords and email addresses", "danger")
            end_time = time.time()
            app.logger.info(end_time - start_time)
            return redirect("/")
         else:
            # email is in db password is not
            flash("ALERT: Your email was compromised in the data breach", "danger")
            end_time = time.time()
            app.logger.info(end_time - start_time)
            return redirect("/")
      else:
         flash("ALL GOOD: Your email and password have not been breached... live to fight another day", "good")
         end_time = time.time()
         app.logger.info(end_time - start_time)
         return redirect("/")



if __name__ == '__main__':
   global con
   con = sql.connect()
   app.run(debug=True)
