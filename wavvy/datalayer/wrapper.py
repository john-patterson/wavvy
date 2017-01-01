from wavvy.datalayer.models import db

__all__ = ['DB']


class DB:
    def __enter__(self):
        return db.session

    def __exit__(self, exc_type, exc_val, exc_tb):
        if exc_type is not None:
            db.session.rollback()
            return False
        db.session.commit()
        return True
