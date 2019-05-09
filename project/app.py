from flask import Flask
import telebot
from config import Configuration, WebhookConf


bot = telebot.TeleBot(WebhookConf.API_TOKEN)
app = Flask(__name__)
app.config.from_object(Configuration)
