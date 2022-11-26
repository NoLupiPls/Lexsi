from aiogram.dispatcher.filters import Command
from aiogram import types

from loader import dp
from bot.data.config import OWNER as own
from bot.middlewares.i18n import setup_middleware

i18n = setup_middleware(dp)
_ = i18n.gettext


@dp.message_handler(commands="site")
async def openr_command(message: types.Message, command: Command.CommandObj):
    if message.from_user.id == own:
        if command.args:
            args = command.args
            await message.answer(args)
            import webbrowser
            # Add a URL of JavaTpoint to open it in a browser
            url = f'{args}'
            # Open the URL using open() function of module
            webbrowser.open_new_tab(url)
        else:
            await message.answer(_("Введи текст в качестве аргумента команды, и я открою ссылку."))
