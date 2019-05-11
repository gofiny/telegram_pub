from app import bot, app, db
from models import Users
from config import WebhookConf
import flask
import telebot
from keyboards import Keyboards
from datetime import datetime


@app.route(WebhookConf.WEBHOOK_URL_PATH, methods=['POST'])
def webhook():
    if flask.request.headers.get('content-type') == 'application/json':
        json_string = flask.request.get_data().decode('utf-8')
        update = telebot.types.Update.de_json(json_string)
        bot.process_new_updates([update])
        return ''
    else:
        flask.abort(403)


@bot.message_handler(commands=['start'])
def test(message):
    user = Users.get_user(message.chat.id)
    chat_id = message.chat.id
    username = message.chat.username
    first_name = message.chat.first_name

    if user is not None:
        user.username = username
        user.first_name = first_name
        user.reg_date = datetime.now()
    else:
        user = Users(chat_id=chat_id, username=username, first_name=first_name, reg_date=datetime.now())

    db.session.add(user)
    db.session.commit()

    bot.send_message(message.chat.id, reply_markup=Keyboards.main_menu(), text='Приветствую в моем демо боте!')


@bot.message_handler(func=lambda message: True, content_types=['text'])
def welcome_mess(message):
    if message.text == '📰 Подписки':
        bot.send_message(message.chat.id, reply_markup=Keyboards.subscribes(), text='Выберите нужный пункт')
    elif message.text == '❓ Помощь':
        bot.send_message(message.chat.id, text='Тут будет помощь')
