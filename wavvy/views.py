from flask import render_template, request, session, escape, redirect, url_for

from wavvy import app, user
import wavvy.data as data
from functools import wraps


def requires_auth(view):
    @wraps(view)
    def inner(*args, **kwargs):
        if user.logged_in():
            return view(*args, **kwargs)
        return redirect(url_for('login'))

    return inner


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/adjust', methods=['POST', 'GET'])
@requires_auth
def adjust():
    if request.method == 'POST':
        new_temp = request.form['new_temp']
        data.adjust_temp(new_temp)
    current_temp = data.current_room_temp()
    current_setting = data.get_current_setting()
    return render_template('adjust.html',
                           error=None,
                           current_temp=current_temp,
                           current_setting=current_setting)


@app.route('/login', methods=['POST', 'GET'])
def login():
    error = None
    if request.method == 'POST':
        user.login(request)
        if user.logged_in():
            return '{} logged in!'.format(user.current_user())
        error = 'Incorrect username or password!'
    return render_template('login.html', error=error)


@app.route('/logout')
def logout():
    user.logout()
    return 'You are logged out.'
