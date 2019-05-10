from app import bot, app
from config import WebhookConf
import flask
import telebot
from keyboards import Keyboards


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
    bot.send_message(message.chat.id, reply_markup=Keyboards.main_menu(), text='Приветствую в моем демо боте!')


@bot.message_handler(func=lambda message: True, content_types=['text'])
def welcome_mess(message):
    if message.text.lower() == 'подписки':
        bot.send_message(message.chat.id, reply_markup=Keyboards.subscribes(), text='Выберите нужный пункт')
