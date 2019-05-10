from app import db
from datetime import datetime


class Users(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    chat_id = db.Column(db.Integer, unique=True)
    username = db.Column(db.String(50), default=None)
    first_name = db.Column(db.String(50), default=None)
    reg_date = db.Column(db.DateTime, default=datetime.now())

    @staticmethod
    def get_user(chat_id):
        return Users.query.filter(Users.chat_id==chat_id)

    def __init__(self, *args, **kwargs):
        super(Users, self).__init__(*args, **kwargs)

    def __repr__(self):
        return f'<[{self.id}]Username: {self.username}>'
