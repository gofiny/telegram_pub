from app import bot, app, db, user_datastore
from models import Users, Subscriptions, user_subs
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
    reg_date = datetime.now()

    if user is not None:
        user.username = username
        user.first_name = first_name
        user.reg_date = reg_date
    else:
        user = user_datastore.create_user(chat_id=chat_id, username=username, first_name=first_name, reg_date=reg_date)

    db.session.add(user)
    db.session.commit()

    bot.send_message(message.chat.id, reply_markup=Keyboards.main_menu(), text='Приветствую в моем демо боте!')


@bot.message_handler(func=lambda message: True, content_types=['text'])
def main_menu(message):
    if message.text == '📰 Подписки':
        subscriptions = Subscriptions.get_subs()
        keyboard = Keyboards.subscribes(subscriptions)
        bot.send_message(message.chat.id, reply_markup=keyboard, text='Выберите нужный пункт')
    elif message.text == '❓ Помощь':
        bot.send_message(message.chat.id, text='Тут будет помощь')


@bot.callback_query_handler(func=lambda call: True)
def callbacks(call):
    chat_id = call.message.chat.id
    message_id = call.message.message_id
    data = call.data.split()

    if data[0] == 'sub_info':
        sub = Subscriptions.query.filter(Subscriptions.data == data[1]).first()
        text = f'{sub.title}\n\n{sub.description}\nАктивна {sub.work_time} дней\nСтоимость: {sub.price}'
        keyboard = Keyboards.buy_button(sub.data)
        bot.edit_message_text(chat_id=chat_id, message_id=message_id, text=text, reply_markup=keyboard)
    elif data[0] == 'my_subs_info':
        all_subs = Subscriptions.get_subs()
        text = ''
        for sub in all_subs:
            if sub.users.filter(Users.chat_id == chat_id).first():
                days = user_subs.query.filter(Users.chat_id == chat_id).all()
                print(days)
                text += f'{sub.title}\n{sub.description}\nОсталось столько-то дней\n\n'
        if text == '':
            bot.edit_message_text(chat_id=chat_id, message_id=message_id, text='У вас нет ни одной подписки')
        else:
            bot.edit_message_text(chat_id=chat_id, message_id=message_id, text=text)
    elif data[0] == 'info_about':
        bot.edit_message_text(chat_id=chat_id, message_id=message_id, text='Скоро будет готово')

