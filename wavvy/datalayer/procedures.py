from wavvy.datalayer.models import User, Adjustment
from wavvy.datalayer.wrapper import DB
from passlib.hash import pbkdf2_sha256 as pass_algorithm

from datetime import datetime

salt_bytes = 25
hash_iterations = 8000

__all__ = ['add_user', 'authenticate', 'adjust', 'get_current_setting']


def hash_pass(plain_password):
    return pass_algorithm \
        .using(rounds=hash_iterations, salt_size=salt_bytes) \
        .hash(plain_password)


def add_user(*, username, plain_password, team=None):
    user = User(
        username=username,
        password=hash_pass(plain_password),
        team=team)
    with DB() as db:
        db.add(user)


def get_by_username(username):
    return User.query \
        .filter(User.username.ilike(username)) \
        .first()


def authenticate(username, plain_password):
    user = get_by_username(username)
    if pass_algorithm.verify(plain_password, user.password):
        return True
    return False


def get_last_adjustment():
    return Adjustment.query.order_by(Adjustment.timestamp.desc()).first()


def get_current_setting():
    last_adjustment = get_last_adjustment()
    return last_adjustment.new_temp if last_adjustment else None


def adjust(*, new, outside, room, username):
    user = get_by_username(username)
    time = datetime.now()
    old = get_last_adjustment()
    old = old.new_temp if old else 0
    adjustment = Adjustment(
        old_temp=old,
        new_temp=new,
        outside_temp=outside,
        room_temp=room,
        adjuster=user,
        timestamp=time)
    with DB() as db:
        db.add(adjustment)
