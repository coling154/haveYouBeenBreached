# App.py
# Author: Ryan Quirk <ryan.quirk6@protonmail.ch>
#
# Description: This is the main flask application. This script
# initializes the app, and handles all http requests & api calls.
from flask import Flask, request, render_template, redirect, url_for, flash
import hashlib
import sql
import re
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

      # Send alert if form is empty
      if request.form['value'] == "":
         flash("ALERT: Please enter email or password", "noFill") 
         return redirect("/")
      
      pwd = request.form['value']
      pwd = hashlib.sha256(pwd.encode("utf-8")).hexdigest() # Hash the password

      # If password is in database redirect to according page
      if sql.checkPassword(pwd, con):
         flash("WARNING: Your password has been breached!", "danger")
         return redirect("/")
      else:
         flash("ALL GOOD: Your password has not been breached... live to fight another day", "good")
         return redirect("/")

# Handles the Check Email button
@app.route('/checkEmail', methods = ["POST"])
def checkEmail():
   if request.method == 'POST':

      # Send alert if form is empty
      if request.form['value'] == "":
         flash("ALERT: Please enter email or password", "noFill") 
         return redirect("/")

      email = request.form['value']

      # Use regex to validate if input is a proper email
      if not re.search(r".+@.+\..*", email):
         flash("ALERT: Please enter valid email", "noFill")
         return redirect("/")

      # Hash the email
      email = hashlib.sha256(email.encode('utf-8')).hexdigest() 

      # If the email is in the database redirect to the according page
      if sql.checkEmail(email, con):
         flash("WARNING: Your email has been breached!", "danger")
         return redirect("/")
      else:
         flash("ALL GOOD: Your email has not been breached... live to fight another day", "good")
         return redirect("/")


if __name__ == '__main__':
   global con
   con = sql.connect()
   app.run(debug=True)
