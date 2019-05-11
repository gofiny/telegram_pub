from app import db
from flask_security import UserMixin, RoleMixin


user_subs = db.Table(
    'user_subs',
    db.Column('user_id', db.Integer, db.ForeignKey('users.id')),
    db.Column('sub_id', db.Integer, db.ForeignKey('subscriptions.id')))


class Users(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    chat_id = db.Column(db.Integer, unique=True)
    username = db.Column(db.String(50), default=None)
    first_name = db.Column(db.String(50), default=None)
    reg_date = db.Column(db.DateTime)

    subs = db.relationship('Subscriptions', secondary=user_subs, backref=db.backref('users', lazy='dynamic'))

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
        return f'{self.title}'


# Security

users_roles = db.Table(
    'users_roles',
    db.Column('user_id', db.Integer(), db.ForeignKey('SiteUsers.id')),
    db.Column('role_id', db.Integer(), db.ForeignKey('Role.id'))
)


class SiteUsers(db.Model, UserMixin):
    id = db.Column(db.Integer(), primary_key=True)
    email = db.Column(db.String(100), unique=True)
    password = db.Column(db.String(255))
    active = db.Column(db.Boolean())
    roles = db.relationship('Role', secondary=users_roles, backref=db.backref('site_users', lazy='dynamic'))


class Role(db.Model, RoleMixin):
    id = db.Column(db.Integer(), primary_key=True)
    name = db.Column(db.String(30), unique=True)
    description = db.Column(db.String(255))

