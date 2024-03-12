# App.py
# Author: Ryan Quirk <ryan.quirk6@protonmail.ch>
#
# Description: This is the main flask application. This script
# initializes the app, and handles all http requests & api calls.
from flask import Flask, request, render_template, redirect, url_for, flash
from flaskr import sql
import hashlib
app = Flask(__name__, static_folder="static")

app.config['SECRET_KEY'] = "secretkey"

# Landing page for app
@app.route('/')
def index():
   return render_template("landing.html")

# Handles the Check Pass button
@app.route('/checkPass', methods = ["POST"])
def checkPass():
   if request.method == "POST":
      pwd = request.form['value'].encode("utf-8")
      pwd = hashlib.sha3_256(pwd).hexdigest() # Hash the password

      # If password is in database redirect to according page
      if sql.checkPassword(pwd, 1):
         flash("WARNING: Your password has been breached!", "danger")
         return redirect("/")
      else:
         flash("ALL GOOD: Your password has not been breached... live to fight another day", "good")
         return redirect("/")

# Handles the Check Email button
@app.route('/checkEmail', methods = ["POST"])
def checkEmail():
   if request.method == 'POST':
      email = request.form['value'].encode('utf-8')
      email = hashlib.sha3_256(email).hexdigest() # Hash the email

      # If the email is in the database redirect to the according page
      if sql.checkEmail(email, 1):
         flash("WARNING: Your email has been breached!", "danger")
         return redirect("/")
      else:
         flash("ALL GOOD: Your email has not been breached... live to fight another day", "good")
         return redirect("/")


if __name__ == '__main__':
   app.run(debug=True)
