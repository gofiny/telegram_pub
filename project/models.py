from app import db
from flask_security import UserMixin, RoleMixin


user_subs = db.Table(
    'user_subs',
    db.Column('user_id', db.Integer, db.ForeignKey('users.id')),
    db.Column('sub_id', db.Integer, db.ForeignKey('subscriptions.id')),
    db.Column('buy_date', db.DateTime)
)

user_roles = db.Table(
    'user_roles',
    db.Column('user_id', db.Integer(), db.ForeignKey('users.id')),
    db.Column('role_id', db.Integer(), db.ForeignKey('role.id'))
)

post_subs = db.Table(
    'post_subs',
    db.Column('post_id', db.Integer(), db.ForeignKey('post.id')),
    db.Column('sub_id', db.Integer(), db.ForeignKey('subscriptions.id'))
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
        return Users.query.filter(Users.chat_id == chat_id).first()

    def __init__(self, *args, **kwargs):
        super(Users, self).__init__(*args, **kwargs)

    def __repr__(self):
        return f'<[{self.id}]Username: {self.username}>'


class Subscriptions(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(30))
    data = db.Column(db.String(30), default=None, nullable=True)  # Английские символы, для использования колбэков
    work_time = db.Column(db.Integer)  # Рабочее время подписки
    description = db.Column(db.Text)
    price = db.Column(db.Integer, default=0)  # Цена подписки, целое число!

    @staticmethod
    def get_subs():
        return Subscriptions.query.order_by(Subscriptions.price.desc())

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


class Post(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(35))
    text = db.Column(db.String(255))
    image_url = db.Column(db.String(255), nullable=True, default=None)
    roles = db.relationship('Subscriptions', secondary=post_subs, backref=db.backref('posts', lazy='dynamic'))

    def __init__(self, *args, **kwargs):
        super(Post, self).__init__(*args, **kwargs)

        #text = f'{self.title}\n\n{self.text}'

    def __repr__(self):
        return self.title

