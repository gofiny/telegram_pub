from flask import Flask
import telebot

from config import Configuration, WebhookConf

from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate, MigrateCommand
from flask_script import Manager
from flask_admin import Admin
from flask_admin.contrib.sqla import ModelView
from flask_security import SQLAlchemyUserDatastore, Security


bot = telebot.TeleBot(WebhookConf.API_TOKEN)
app = Flask(__name__)
app.config.from_object(Configuration)
db = SQLAlchemy(app)
migrate = Migrate(app, db)
manager = Manager(app)
manager.add_command('db', MigrateCommand)

# Admin
from models import Users, Subscriptions, Role
admin = Admin(app)
admin.add_view(ModelView(Users, db.session))
admin.add_view(ModelView(Subscriptions, db.session))

# Security
user_datastore = SQLAlchemyUserDatastore(db, Users, Role)
security = Security(app, user_datastore)
