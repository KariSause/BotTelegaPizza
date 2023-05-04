from aiogram.types import ReplyKeyboardMarkup, KeyboardButton, ReplyKeyboardRemove
from aiogram import types

item1 = types.KeyboardButton('/Режим_работы')
item2 = types.KeyboardButton('/Расположение')
item3 = types.KeyboardButton('/Меню')
item4 = types.KeyboardButton('Поделиться номером', request_contact=True)
item5 = types.KeyboardButton('Отправить где я', request_location=True)

mainMenu = ReplyKeyboardMarkup(resize_keyboard=True).add(item1,item2, item3).row(item4,item5)