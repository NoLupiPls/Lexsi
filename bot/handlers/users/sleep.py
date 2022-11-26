from time import sleep
from aiogram import types
import pyautogui as pag

from loader import dp
from bot.data.config import OWNER as own
from bot.middlewares.i18n import setup_middleware

i18n = setup_middleware(dp)
_ = i18n.gettext


@dp.message_handler(commands="sleep")
async def sleep_def(message: types.Message):
    if message.from_user.id == own:
        await message.answer(_("✅ Буквально через пару секунд я Ваш ноутбук переведу в <b>режим сна</b>"),
                             disable_notification=True)
        pag.press("win")
        sleep(1)
        pag.press("tab")
        sleep(1)
        pag.press("down")
        sleep(0.2)
        pag.press("down")
        sleep(0.2)
        pag.press("down")
        sleep(0.2)
        pag.press("down")
        sleep(0.2)
        pag.press("down")
        sleep(0.2)
        pag.press("enter")
        sleep(1)
        pag.press("enter")
    else:
        pass
