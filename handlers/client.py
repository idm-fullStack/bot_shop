from aiogram import types, Dispatcher
from create_bot import bot
from keybords import kb_client
from data_base import sqlite_db


async def command_start(message: types.Message):
    await bot.send_message(message.from_user.id, 'уже работаю', reply_markup=kb_client)
    await message.delete()


async def shop_open_command(message: types.Message):
    await bot.send_message(message.from_user.id, 'ПН-ПТ с 8.15 до 18.00')


async def bot_shop_plase_command(message: types.Message):
    await bot.send_message(message.from_user.id, 'ул. Лермонтова, 83')


async def shop_product_list(message: types.Message):
    await sqlite_db.sql_read(message)


def register_handlers_client(dp: Dispatcher):
    dp.register_message_handler(command_start, commands=['start', 'help'])
    dp.register_message_handler(bot_shop_plase_command, commands=['расположение'])
    dp.register_message_handler(shop_open_command, commands=['режим работы'])
    dp.register_message_handler(shop_product_list, commands=['меню'])
