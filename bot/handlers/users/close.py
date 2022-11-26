from aiogram import types
import pyautogui as pag

from loader import dp
from bot.data.config import OWNER as own
from bot.middlewares.i18n import setup_middleware

i18n = setup_middleware(dp)
_ = i18n.gettext


@dp.message_handler(commands=["close"])
async def close_widget(message: types.Message):
    if message.from_user.id == own:
        pag.hotkey("alt", "f4")
        await message.answer(_("🚫 Окно закрыто"))
    else:
        pass
