from aiogram.types import ReplyKeyboardMarkup, KeyboardButton
b1 = KeyboardButton('/режим работы')
b2 = KeyboardButton('/расположение')
b3 = KeyboardButton('/меню')
kb_client = ReplyKeyboardMarkup(resize_keyboard=True)
kb_client.add(b1).add(b2).add(b3)
