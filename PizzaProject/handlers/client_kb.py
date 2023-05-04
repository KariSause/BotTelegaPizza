from aiogram.types import ReplyKeyboardMarkup, KeyboardButton, ReplyKeyboardRemove, types

#b1 = KeyboardButton('/Режим_работы')
#b2 = KeyboardButton('/Расположение')
#b3 = KeyboardButton('/Меню')


item1 = types.KeyboardButton('/Режим_работы')
item2 = types.KeyboardButton('/Расположение')
item3 = types.KeyboardButton('/Меню')
mainMenu = ReplyKeyboardMarkup(resize_keyboard=True).add(item1, item2, item3)

#kb_client = ReplyKeyboardMarkup()

#kb_client.add(b1, b2, b3)