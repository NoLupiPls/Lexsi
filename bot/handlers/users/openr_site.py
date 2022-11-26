from aiogram import types
from aiogram.dispatcher.filters import Command

from bot.data.config import OWNER as own
from loader import dp


@dp.message_handler(commands="openr")
async def openr_command(message: types.Message, command: Command.CommandObj):
    if message.from_user.id == own:
        if command.args:
            args = command.args
            await message.answer(args)
            import webbrowser
            # Add a URL of JavaTpoint to open it in a browser
            url = f'https://{args}.ru'
            # Open the URL using open() function of module
            webbrowser.open_new_tab(url)
        else:
            await message.answer("[RU] Введи текст в качестве аргумента команды, и я открою ссылку.")
