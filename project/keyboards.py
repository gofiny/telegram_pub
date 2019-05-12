from telebot import types


class Keyboards:

    @staticmethod
    def main_menu():
        keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)
        keyboard.row('📰 Подписки')
        keyboard.row('❓ Помощь')

        return keyboard

    @staticmethod
    def subscribes(subs):
        keyboard = types.InlineKeyboardMarkup()
        keyboard.row(types.InlineKeyboardButton(text='Мои подписки', callback_data='my_subs_info'))
        for sub in subs:
            keyboard.row(types.InlineKeyboardButton(text=sub.title, callback_data=f'sub_info {sub.data}'))

        return keyboard

    @staticmethod
    def my_subs_info(subs):
        keyboard = types.InlineKeyboardMarkup()
        for sub in subs:
            keyboard.row(types.InlineKeyboardButton(text=sub.title, callback_data=f'info_about {sub.data}'))

        return keyboard

    @staticmethod
    def buy_button(sub_data):
        keyboard = types.InlineKeyboardMarkup()
        keyboard.row(types.InlineKeyboardButton(text='Приобрести', callback_data=f'sub_buy {sub_data}'))

        return keyboard
