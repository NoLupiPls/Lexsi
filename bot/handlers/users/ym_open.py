from aiogram import types

from loader import dp
from bot.data.config import OWNER as own
import os


@dp.message_handler(commands="music")
async def open_music(message: types.Message):
    if message.from_user.id == own:
        os.startfile("C:/Users/asus/Desktop/Яндекс.Музыка.lnk")
        # import webbrowser
        # Add a URL of JavaTpoint to open it in a browser
        # url = 'https://vk.com/audios252841255'
        # Open the URL using open() function of module
        # webbrowser.open_new_tab(url)
        await message.answer("🎧 <b>Яндекс.Музыка</b> открыта!")
    else:
        pass
