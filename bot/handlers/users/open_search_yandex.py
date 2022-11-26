from aiogram import types
from aiogram.dispatcher.filters import Command

from bot.data.config import OWNER as own
from loader import dp


@dp.message_handler(commands="search")
async def openr_command(message: types.Message, command: Command.CommandObj):
    if message.from_user.id == own:
        if command.args:
            args = command.args
            await message.answer(f"Ваш поисковой запрос <b>«{args}»</b>, открыт!")
            import webbrowser
            # Add a URL of JavaTpoint to open it in a browser
            url = f'https://yandex.ru/search/?text={args}'
            # Open the URL using open() function of module
            webbrowser.open_new_tab(url)
        else:
            await message.answer("Введи что ты будешь искать и я тебе открою ссылку в браузере!")
