from wavvy.datalayer.models import User, Adjustment
from wavvy.datalayer.wrapper import DB
from passlib.hash import pbkdf2_sha256 as pass_algorithm

salt_bytes = 25
hash_iterations = 8000

__all__ = ['add_user']


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


def authenticate(*, username, plain_password):
    user = User.query.filter(User.username.ilike(username)).first()
    if pass_algorithm.verify(plain_password, user.password):
        return True
    return False
