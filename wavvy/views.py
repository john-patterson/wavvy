from wavvy import app
from flask import Flask, url_for, render_template, request, session, escape


def clear_session(s):
    if 'username' in s:
        del s['username']
    s['logged_in'] = False


@app.route('/hello')
@app.route('/hello/<name>')
def hello(name=None):
    return render_template('hello.html', name=name)


@app.route('/')
def index():
    if session.get('logged_in', False):
        return 'Logged in as {}'.format(escape(session['username']))
    return 'You are not logged in.'


@app.route('/login', methods=['POST', 'GET'])
def login():
    error = None
    if request.method == 'POST':
        session['logged_in'] = True
        session['username'] = request.form['username']
        password = escape(request.form['password'])
        return 'Validating a login! U:{} P:{}'.format(escape(session['username']), password)
    return render_template('login.html', error=error)


@app.route('/logout')
def logout():
    clear_session(session)
    return 'You are logged out.'
