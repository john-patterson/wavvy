from flask import render_template, request, session, escape

from wavvy import app
from wavvy.auth import Auth

auth = Auth(session)


@app.route('/')
def index():
    if auth.logged_in():
        return 'Logged in as {}'.format(escape(auth.current_user()))
    return 'You are not logged in.'


@app.route('/login', methods=['POST', 'GET'])
def login():
    error = None
    if request.method == 'POST':
        auth.login(request)
        if auth.logged_in():
            return '{} logged in!'.format(auth.current_user())
        error = 'Incorrect username or password!'
    return render_template('login.html', error=error)


@app.route('/logout')
def logout():
    auth.logout()
    return 'You are logged out.'
