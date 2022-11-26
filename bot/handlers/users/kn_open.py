from aiogram import types
import webbrowser

from loader import dp
from bot.data.config import OWNER as own
from bot.middlewares.i18n import setup_middleware

i18n = setup_middleware(dp)
_ = i18n.gettext


@dp.message_handler(commands="kino")
async def open_kinopoisk(message: types.Message):
    if message.from_user.id == own:
        # Add a URL of JavaTpoint to open it in a browser
        url = 'https://kinopoisk.ru'
        # Open the URL using open() function of module
        webbrowser.open_new_tab(url)
        await message.answer(_("🎞 <b>Кинопоиск</b> открыт"))
    else:
        pass
