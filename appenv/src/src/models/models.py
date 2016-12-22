from datetime import datetime

from ..core import db
from .. import app


class Key(db.Model):
    id = db.Column(db.Integer, primary_key=True, unique=True, nullable=False)
    tag_id = db.Column(db.Integer, unique=True)
    room_id = db.Column(db.Integer, unique=True)


class User(db.Model):
    id = db.Column(db.Integer, primary_key=True, unique=True, nullable=False)
    tag_id = db.Column(db.Integer, unique=True)
    first_name = db.Column(db.String(80))
    last_name = db.Column(db.String(100))
    profile_pic = db.Column(db.LargeBinary)


class Session(db.Model):
    id = db.Column(db.Integer, primary_key=True, unique=True, nullable=False)
    user_id = db.Column(db.Integer, db.ForeignKey(User.id))
    key_id = db.Column(db.Integer, db.ForeignKey(Key.id))
    timestamp = db.Column(db.DateTime)
    user = db.relationship(User, backref=db.backref('sessions', lazy='dynamic'))
    key = db.relationship(Key, backref=db.backref('sessions', lazy='dynamic'))

    def __init__(self, user_id, key_id, timestamp=None):
        self.user_id = user_id
        self.key_id = key_id
        if timestamp is None:
            timestamp = datetime.utcnow()
        self.timestamp = timestamp

    def __repr__(self):
        return '<Session %r>' % self.id

# models for which we want to create API endpoints
app.config['API_MODELS'] = {'session': Session, 'user': User, 'key': Key}

# models for which we want to create CRUD-style URL endpoints,
# and pass the routing onto our AngularJS application
app.config['CRUD_URL_MODELS'] = {'session': Session, 'user': User, 'key': Key}
