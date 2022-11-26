from aiogram import types
import os

from loader import dp
from bot.data.config import OWNER as own
from bot.middlewares.i18n import setup_middleware

i18n = setup_middleware(dp)
_ = i18n.gettext


@dp.message_handler(commands="music")
async def open_music(message: types.Message):
    if message.from_user.id == own:
        os.startfile("C:/Users/ilyas/Desktop/Яндекс.Музыка.lnk")
        # import webbrowser
        # Add a URL of JavaTpoint to open it in a browser
        # url = 'https://vk.com/audios252841255'
        # Open the URL using open() function of module
        # webbrowser.open_new_tab(url)
        await message.answer(_("🎧 <b>Яндекс.Музыка</b> открыта!"))
    else:
        pass
