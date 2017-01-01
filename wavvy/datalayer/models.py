from wavvy import app

from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy(app)


__all__ = ['User', 'Adjustment']


class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True, nullable=False)
    password = db.Column(db.String(100), nullable=False)
    team = db.Column(db.String(25), nullable=True)

    def __init__(self, *, username, password, team=None):
        self.username = username
        self.password = password
        self.team = team

    def __repr__(self):
        return '<User %r>' % self.username


class Adjustment(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    old_temp = db.Column(db.Float)
    new_temp = db.Column(db.Float)
    outside_temp = db.Column(db.Float)
    room_temp = db.Column(db.Float)
    timestamp = db.Column(db.DateTime)

    adjuster_id = db.Column(db.Integer, db.ForeignKey('user.id'))
    adjuster = db.relationship('User',
                               backref=db.backref('accounts', lazy='dynamic'))

    def __init__(self, *, old_temp, new_temp, outside_temp, room_temp,
                 timestamp, adjuster):
        self.old_temp = old_temp
        self.new_temp = new_temp
        self.outside_temp = outside_temp
        self.timestamp = timestamp
        self.adjuster = adjuster
        self.room_temp = room_temp

    def __repr__(self):
        return '<Adjustment {}>'.format(repr(self.id))
