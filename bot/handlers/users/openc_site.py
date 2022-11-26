from aiogram import types
from aiogram.dispatcher.filters import Command

from loader import dp
from bot.data.config import OWNER as own


@dp.message_handler(commands="openc")
async def openc_command(message: types.Message, command: Command.CommandObj):
    if message.from_user.id == own:
        if command.args:
            args = command.args
            await message.answer(args)
            import webbrowser
            # Add a URL of JavaTpoint to open it in a browser
            url = f'https://{args}.com'
            # Open the URL using open() function of module
            webbrowser.open_new_tab(url)
        else:
            await message.answer("[COM] Введи текст в качестве аргумента команды, и я открою ссылку.")
