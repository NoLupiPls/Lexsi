from aiogram import types
import webbrowser

from loader import dp
from bot.data.config import OWNER as own


@dp.message_handler(commands="kino")
async def open_kinopoisk(message: types.Message):
    if message.from_user.id == own:
        # Add a URL of JavaTpoint to open it in a browser
        url = 'https://kinopoisk.ru'
        # Open the URL using open() function of module
        webbrowser.open_new_tab(url)
        await message.answer("🎞 <b>Кинопоиск</b> открыт")
    else:
        pass
