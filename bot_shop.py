from aiogram.utils import executor
from create_bot import dp
from data_base import sqlite_db
from handlers import client, admin


async def on_start_on(_):
    print('бот вышел в онлайн')


sqlite_db.sql_start()
client.register_handlers_client(dp)
admin.register_handlers_admin(dp)
executor.start_polling(dp, skip_updates=True, on_startup=on_start_on)
