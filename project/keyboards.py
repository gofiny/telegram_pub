from telebot import types


class Keyboards:

    @staticmethod
    def main_menu():
        keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)
        keyboard.row('Подписки')
        keyboard.row('Помощь')

        return keyboard