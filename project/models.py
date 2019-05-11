from app import db
from datetime import datetime


users_subs = db.Table(
    'user_subs',
    db.Column('user_id', db.Integer, db.ForeignKey('users.id')),
    db.Column('sub_id', db.Integer, db.ForeignKey('subscription.id')))


class Users(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    chat_id = db.Column(db.Integer, unique=True)
    username = db.Column(db.String(50), default=None)
    first_name = db.Column(db.String(50), default=None)
    reg_date = db.Column(db.DateTime, default=datetime.now())

    subs = db.relationship('subscriptions', secondary=users_subs, backref=db.backref('users', lazy='dynamic'))

    @staticmethod
    def get_user(chat_id):
        return Users.query.filter(Users.chat_id==chat_id).first()

    def __init__(self, *args, **kwargs):
        super(Users, self).__init__(*args, **kwargs)

    def __repr__(self):
        return f'<[{self.id}]Username: {self.username}>'


class Subscriptions(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(30))
    work_time = db.Column(db.Integer)  # Рабочее время подписки
    description = db.Column(db.Text)

    def __init__(self, *args, **kwargs):
        super(Subscriptions, self).__init__(*args, **kwargs)

    def __repr__(self):
        return f'<[{self.id}]Title: {self.title}>'
