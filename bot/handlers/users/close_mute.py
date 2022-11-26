from aiogram import types
import pyautogui as pag

from loader import dp
from bot.data.config import OWNER as own
from bot.middlewares.i18n import setup_middleware

i18n = setup_middleware(dp)
_ = i18n.gettext


@dp.message_handler(commands="st")
async def stoooop(message: types.Message):
    if message.from_user.id == own:
        pag.hotkey("win", "d")
        pag.hotkey("fn", "volumemute")
        await message.answer(_("✅ Готово!"), disable_notification=True)
    else:
        pass
