# App.py
# Author: Ryan Quirk <ryan.quirk6@protonmail.ch>
#
# Description: This is the main flask application. This script
# initializes the app, and handles all http requests & api calls.
from flask import Flask, request, render_template, redirect, url_for
app = Flask(__name__, static_folder="static")

# Landing page for app
@app.route('/')
def index():
   return render_template("landing.html")

# Handles the Check Pass button
@app.route('/checkPass', methods = ["POST"])
def checkPass():
   if request.method == "POST":
      pwd = request.form['value']
      print(pwd)
      redirect(url_for('index'))

# Handles the Check Email button
@app.route('/checkEmail', methods = ["POST"])
def checkEmail():
   if request.method == 'POST':
      email = request.form['value']
      print(email)
      return redirect(url_for('index'))


if __name__ == '__main__':
   app.run()
