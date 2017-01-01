from flask import render_template, request, session, escape, redirect, url_for

from wavvy import app, user


def requires_auth(view):
    def inner(*args, **kwargs):
        if user.logged_in():
            return view(*args, **kwargs)
        return redirect(url_for('login'))

    return inner


@app.route('/')
def index():
    if user.logged_in():
        return 'Logged in as {}'.format(escape(user.current_user()))
    return 'You are not logged in.'


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
