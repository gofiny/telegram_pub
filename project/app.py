from flask import Flask, redirect, url_for, request
import telebot
import time
from config import Configuration, WebhookConf

from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate, MigrateCommand
from flask_script import Manager
from flask_admin import Admin, AdminIndexView
from flask_admin.contrib.sqla import ModelView
from flask_security import SQLAlchemyUserDatastore, Security, current_user


bot = telebot.TeleBot(WebhookConf.API_TOKEN)
app = Flask(__name__)
app.config.from_object(Configuration)
db = SQLAlchemy(app)
migrate = Migrate(app, db)
manager = Manager(app)
manager.add_command('db', MigrateCommand)

# Admin
from models import Users, Subscriptions, Role, user_subs


class AdminView(ModelView):
    def is_accessible(self):
        return current_user.has_role('admin')

    def inaccessible_callback(self, name, **kwargs):
        return redirect(url_for('security.login', next=request.url))


class HomeAdminView(AdminIndexView):
    def is_accessible(self):
        return current_user.has_role('admin')

    def inaccessible_callback(self, name, **kwargs):
        return redirect(url_for('security.login', next=request.url))


admin = Admin(app, 'FlaskApp', url='/', index_view=HomeAdminView(name='Home'))
admin.add_view(AdminView(Users, db.session))
admin.add_view(AdminView(Subscriptions, db.session))

# Security
user_datastore = SQLAlchemyUserDatastore(db, Users, Role)
security = Security(app, user_datastore)


bot.remove_webhook()
time.sleep(2)
bot.set_webhook(url=WebhookConf.WEBHOOK_URL_BASE + WebhookConf.WEBHOOK_URL_PATH,
                certificate=open(WebhookConf.WEBHOOK_SSL_CERT, 'r'))


import view, bot_views
