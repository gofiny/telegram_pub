from app import db
from flask_security import UserMixin, RoleMixin


user_subs = db.Table(
    'user_subs',
    db.Column('user_id', db.Integer, db.ForeignKey('users.id')),
    db.Column('sub_id', db.Integer, db.ForeignKey('subscriptions.id'))
)

user_roles = db.Table(
    'user_roles',
    db.Column('user_id', db.Integer(), db.ForeignKey('users.id')),
    db.Column('role_id', db.Integer(), db.ForeignKey('role.id'))
)


class Users(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    chat_id = db.Column(db.Integer, unique=True)
    username = db.Column(db.String(50), default=None)
    first_name = db.Column(db.String(50), default=None)
    reg_date = db.Column(db.DateTime)
    email = db.Column(db.String(100), default=None, nullable=True)
    password = db.Column(db.String(255), default=None, nullable=True)
    active = db.Column(db.Boolean, default=0)

    subs = db.relationship('Subscriptions', secondary=user_subs, backref=db.backref('users', lazy='dynamic'))
    roles = db.relationship('Role', secondary=user_roles, backref=db.backref('users', lazy='dynamic'))

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


class Role(db.Model, RoleMixin):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(30), unique=True)
    description = db.Column(db.String(255))

    def __init__(self, *args, **kwargs):
        super(Role, self).__init__(*args, **kwargs)

    def __repr__(self):
        return f'{self.name}'

