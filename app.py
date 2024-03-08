"""
app.py
Created by Colin Gasiewicz on 03/06/2024
This is part 2 of the project and contains the frontend of the application
"""
import flask
app = flask.Flask(__name__)


@app.route('/login', methods=['POST', 'GET'])
def login():
    error = None
    if flask.method == 'POST':
        if flask.valid_login(flask.request.form['username'],
                       flask.request.form['password']):
            return flask.log_the_user_in(flask.request.form['username'])
        else:
            error = 'Invalid username/password'
    # the code below is executed if the request method
    # was GET or the credentials were invalid
    return flask.render_template('login.html', error=error)