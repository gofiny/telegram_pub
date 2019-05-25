from app import bot, app, db, user_datastore
from models import Users, Subscriptions, user_subs
from config import WebhookConf
import flask
import telebot
from keyboards import Keyboards
from datetime import datetime


def write_stuff(text):
    with open('/tel_pub/telegram_pub/project/logs/stuff.log', 'a') as file_:
        file_.write(text)


def del_sub(user_id, sub_id):
    db.session.execute(user_subs.delete().where(user_subs.c.user_id == user_id).where(user_subs.c.sub_id == sub_id))
    db.session.commit()


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
def register(message):
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
    user = Users.query.filter(Users.chat_id == chat_id).first()

    if data[0] == 'sub_info':
        sub = Subscriptions.query.filter(Subscriptions.data == data[1]).first()
        text = f'{sub.title}\n\n{sub.description}\nАктивна {sub.work_time} дней\nСтоимость: {sub.price}'
        keyboard = Keyboards.buy_button(sub.data)
        bot.edit_message_text(chat_id=chat_id, message_id=message_id, text=text, reply_markup=keyboard)
    elif data[0] == 'my_subs_info':
        text = ''
        subs = db.session.query(user_subs).filter(user_subs.c.user_id == user.id).all()
        for row in subs:
            sub = Subscriptions.query.filter(Subscriptions.id == row[1]).first()
            sub_buy_time = str(row[2])[0:-7]
            sub_buy_time = datetime.strptime(sub_buy_time, '%Y-%m-%d %H:%M:%S')
            time_left = sub_buy_time.second + (sub.work_time * 24 * 60 * 60)
            time_left = time_left - datetime.now().second
            if time_left < 0:
                del_sub(user_id=user.id, sub_id=sub.id)
                left_str = 'Подписка истекла'
            else:
                time_left = time_left / 60 / 60
                if time_left > 24:
                    time_left = time_left / 24
                    left_str = f'Подписка заканчивается через {round(time_left)} дней'
                else:
                    left_str = f'Подписка заканчивается через {round(time_left)} часов'

            text += f'{sub.title}\n\n{sub.description}\n{left_str}\n\n'

        if text == '':
            bot.edit_message_text(chat_id=chat_id, message_id=message_id, text='У вас нет ни одной подписки')
        else:
            bot.edit_message_text(chat_id=chat_id, message_id=message_id, text=text)

    elif data[0] == 'sub_buy':
        sub = Subscriptions.query.filter_by(data=data[1]).first()
        db.session.execute(user_subs.insert().values(user_id=user.id, sub_id=sub.id, buy_date=datetime.now()))
        db.session.commit()
        bot.edit_message_text(chat_id=chat_id, message_id=message_id, text='Поздравляю! Подписка приобретина')

    elif data[0] == 'info_about':
        bot.edit_message_text(chat_id=chat_id, message_id=message_id, text='Скоро будет готово')

