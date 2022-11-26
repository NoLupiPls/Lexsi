from aiogram import types
# import pyautogui as pag
import os

from loader import dp
from bot.data.config import OWNER as own
from bot.middlewares.i18n import setup_middleware

i18n = setup_middleware(dp)
_ = i18n.gettext


@dp.message_handler(commands="tg")
async def open_tg(message: types.Message):
    if message.from_user.id == own:
        # import webbrowser
        # Add a URL of JavaTpoint to open it in a browser
        # url = 'https://web.telegram.org/z/'
        # Open the URL using open() function of module
        # webbrowser.open_new_tab(url)
        os.startfile("C:/Users/ilyas/AppData/Roaming/Telegram Desktop/Telegram.exe")
        await message.answer(_("📊 <b>Telegram</b> открыт!"))
    else:
        pass
