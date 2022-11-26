from aiogram import types
import pyautogui as pag

from loader import dp
from bot.data.config import OWNER as own


@dp.message_handler(commands=["close"])
async def close_widget(message: types.Message):
    if message.from_user.id == own:
        pag.hotkey("alt", "f4")
        await message.answer("🚫 Окно закрыто")
    else:
        pass
