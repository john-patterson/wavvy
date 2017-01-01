from wavvy import app

from flask import Flask, url_for, render_template, request, session, escape


class Auth:
    def __init__(self, s):
        self.session = s

    def __clear_session(self):
        if 'username' in self.session:
            del self.session['username']
        self.session['logged_in'] = False

    def login(self, r):
        username = r.form.get('username', None)
        password = r.form.get('password', None)

        self.__clear_session()
        if username is None or password is None:
            return False
        elif username != 'admin@admin' or password != 'admin':
            return False

        self.session['logged_in'] = True
        self.session['username'] = username
        return True

    def logout(self):
        self.__clear_session()

    def logged_in(self):
        return self.session.get('logged_in', False)

    def current_user(self):
        return self.session.get('username', None)


auth = Auth(session)


@app.route('/hello')
@app.route('/hello/<name>')
def hello(name=None):
    return render_template('hello.html', name=name)


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
