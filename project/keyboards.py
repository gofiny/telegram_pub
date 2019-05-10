from telebot import types


class Keyboards:

    @staticmethod
    def main_menu():
        keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)
        keyboard.row('Подписки')
        keyboard.row('Помощь')

        return keyboard

    @staticmethod
    def subscribes():
        keyboard = types.InlineKeyboardMarkup()
        keyboard.add(
            types.InlineKeyboardButton(text='Мои подписки', callback_data='my_subs_info'),
            types.InlineKeyboardButton(text='Начальная', callback_data='start_subs_info'),
            types.InlineKeyboardButton(text='Прогрессивная', callback_data='progressive_subs_info'),
            types.InlineKeyboardButton(text='Ультра', callback_data='ultra_subs_info')
        )