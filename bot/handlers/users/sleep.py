from time import sleep
from aiogram import types
import pyautogui as pag

from loader import dp
from bot.data.config import OWNER as own


@dp.message_handler(commands="sleep")
async def sleep_def(message: types.Message):
    if message.from_user.id == own:
        await message.answer("✅ Буквально через пару секунд я Ваш ноутбук переведу в <b>режим сна</b>",
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
