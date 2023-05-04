from aiogram import types, Dispatcher
import string, json
from create_bot import dp

@dp.message_handler()
async def echo_send(message: types.Message):
    if {i.lower().translate(str.maketrans('', '', string.punctuation)) for i in message.text.split(" ")}\
        .intersection(set(json.load(open('cenz.json')))) != set():
        await message.reply(' Маты запрещены')
        await message.delete()
        
    #def mes
    #await message.answer("И тебе привет")
    #ping
    #await message.reply(message.text)
    #Write to private anyways
    #await bot.send_message(message.from_user.id, message.text)

def register_handlers_other(dp: Dispatcher):
    dp.register_message_handler(echo_send)