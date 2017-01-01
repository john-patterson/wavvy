from wavvy.datalayer.models import User, Adjustment
from wavvy.datalayer.wrapper import DB
from passlib.hash import pbkdf2_sha256 as pass_algorithm

from datetime import datetime

salt_bytes = 25
hash_iterations = 8000

__all__ = ['add_user', 'authenticate', 'adjust']


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
    results = User.query.filter(User.username.ilike(username))
    if not results:
        return None
    return results.first()


def authenticate(username, plain_password):
    user = get_by_username(username)
    if pass_algorithm.verify(plain_password, user.password):
        return True
    return False

def get_last_adjustment():
    return Adjustment.query.order_by(desc(Adjustment.timestamp)).first()

def adjust(*, new, outside, room, username):
    user = get_by_username(username)
    time = datetime.now()
    old = get_last_adjustment()
    adjustment = Adjustment(
        old_temp=old,
        new_temp=new,
        outside_temp=outside,
        room_temp=room,
        adjuster=user,
        timestamp=time)
    with DB() as db:
        db.add(adjustment)

