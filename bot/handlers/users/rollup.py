from aiogram import types
import pyautogui as pag

from bot.data.config import OWNER as own
from loader import dp


@dp.message_handler(commands=["rollup", "ru"])
async def start(message: types.Message):
    if message.from_user.id == own:
        pag.hotkey("win", "d")
        await message.answer("↪ Окна свёрнуты")
    else:
        pass
