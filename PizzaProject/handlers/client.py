from aiogram import types, Dispatcher
from aiogram.types import ReplyKeyboardRemove
from create_bot import dp, bot
from keyboards.client_kb import mainMenu
from data_base import sqllite_db

'''###########КЛИЕНТСКАЯ ЧАСТЬ#############'''
#@dp.message_handler(commands=['start', 'help'])
async def command_start(message: types.Message):
    try:
        await bot.send_message(message.from_user.id, "Приятного аппетита", reply_markup=mainMenu)
        await message.delete()
    except:
        await message.reply('Общение с ботом через ЛС недоступно, напишите ему: \nhttps://t.me/PizzaDel_bot')
#@dp.message_handler(commands=['Расположение'])
async def pizza_place_command(message: types.Message):
    await bot.send_message(message.from_user.id, 'ул. Колбасная 15')

#@dp.message_handler(commands=['Режим_работы'])
async def pizza_open_command(message: types.Message):
    await bot.send_message(message.from_user.id, 'Вс-Чт с 9:00 до 20:00, Пт-Сб с 10:00 до 23:00', reply_markup=ReplyKeyboardRemove())

#@dp.message_handler(commands=['Меню'])
async def pizza_menu_command(message: types.Message):
    await sqllite_db.sql_read(message)

def register_handlers_client(dp: Dispatcher):
    dp.register_message_handler(command_start, commands=['start', 'help'])
    dp.register_message_handler(pizza_open_command, commands=['Режим_работы'])
    dp.register_message_handler(pizza_place_command, commands=['Расположение'])
    dp.register_message_handler(pizza_menu_command, commands=['Меню'])

register_handlers_client(dp)