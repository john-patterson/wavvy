__all__ = ['Auth']


class Auth:
    def __init__(self, session):
        self.session = session

    def __clear_session(self):
        if 'username' in self.session:
            del self.session['username']
        self.session['logged_in'] = False

    def login(self, request):
        username = request.form.get('username', None)
        password = request.form.get('password', None)

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
