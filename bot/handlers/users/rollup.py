from aiogram import types
import pyautogui as pag

from bot.data.config import OWNER as own
from loader import dp
from bot.middlewares.i18n import setup_middleware

i18n = setup_middleware(dp)
_ = i18n.gettext


@dp.message_handler(commands=["rollup", "ru"])
async def start(message: types.Message):
    if message.from_user.id == own:
        pag.hotkey("win", "d")
        await message.answer(_("↪ Окна свёрнуты"))
    else:
        pass
