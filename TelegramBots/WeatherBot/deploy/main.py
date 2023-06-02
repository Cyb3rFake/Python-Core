from aiogram.utils import executor
from create_bot import dp
from aiogram import types
from weather import get_weather


commands_list = '/map - получить положение города на карте\n' \
                '/start - \n' \
                '/list - получить список команд\n' \
                '/description - описание бота\n' \
                '/weather - текущая погода в городе\n' \
                '/city - ввести город'


async def on_startup(_):
    print('Бот онлайн')


@dp.message_handler(commands=['start'])
async def cmd_start(message: types.Message):
    await message.answer(commands_list)


@dp.message_handler()
async def get_wtr(message: types.Message):
    await message.reply(get_weather(message.text))


if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True, on_startup=on_startup)
