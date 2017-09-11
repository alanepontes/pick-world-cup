from abc import ABCMeta
from plugins import db


class MetaModel():
    __metaclass__ = ABCMeta

    def save(self):
        try:
            db.create_all()
            db.session.add(self)
            db.session.commit()
        except Exception as e:
            db.session.rollback()
            raise e

    def delete(self):
        try:
            db.create_all()
            db.session.delete(self)
            db.session.commit()
        except Exception as e:
            db.session.rollback()
            raise e