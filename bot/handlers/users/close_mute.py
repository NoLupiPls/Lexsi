from aiogram import types
import pyautogui as pag

from loader import dp
from bot.data.config import OWNER as own


@dp.message_handler(commands="st")
async def stoooop(message: types.Message):
    if message.from_user.id == own:
        pag.hotkey("win", "d")
        pag.hotkey("fn", "volumemute")
        await message.answer("✅ Готово!", disable_notification=True)
    else:
        pass
