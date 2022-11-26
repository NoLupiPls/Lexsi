from aiogram import types
import pyautogui as pag

from loader import dp
from bot.data.config import OWNER as own
import os


@dp.message_handler(commands="tg")
async def open_tg(message: types.Message):
    if message.from_user.id == own:
        import webbrowser
        # Add a URL of JavaTpoint to open it in a browser
        # url = 'https://web.telegram.org/z/'
        # Open the URL using open() function of module
        # webbrowser.open_new_tab(url)
        os.startfile("C:/Users/asus/AppData/Roaming/Telegram Desktop/Telegram.exe")
        await message.answer("📊 <b>Telegram</b> открыт!")
    else:
        pass
