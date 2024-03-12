# App.py
# Author: Ryan Quirk <ryan.quirk6@protonmail.ch>
#
# Description: This is the main flask application. This script
# initializes the app, and handles all http requests & api calls.
from flask import Flask, request, render_template, redirect, url_for
import hashlib
from flaskr import sql
app = Flask(__name__, static_folder="static")

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
         return redirect(url_for('passIn'))
      else:
         return redirect(url_for('index'))

# Handles the Check Email button
@app.route('/checkEmail', methods = ["POST"])
def checkEmail():
   if request.method == 'POST':
      email = request.form['value'].encode('utf-8')
      email = hashlib.sha3_256(email).hexdigest() # Hash the email

      # If the email is in the database redirect to the according page
      if sql.checkEmail(email, 1):
         return redirect(url_for('emailIn'))
      else:
         return redirect(url_for('index'))


@app.route('/Breached-Password')
def passIn():
   return render_template('passWarning.html')

@app.route('/Breached-Email')
def emailIn():
   return render_template('emailWarning.html')

if __name__ == '__main__':
   app.run()
