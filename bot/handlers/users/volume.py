from aiogram import types
import pyautogui as pag

from bot.keyboard.inline.inline_kd_menu import ikb_menu
from loader import dp
from bot.data.config import OWNER as own
from bot.middlewares.i18n import setup_middleware

i18n = setup_middleware(dp)
_ = i18n.gettext


@dp.message_handler(commands=["volume"])
async def volume(message: types.Message):
    if message.from_user.id == own:
        await message.answer(_("Кнопки выведены на экран! \n<b>Смотрите ниже:</b>"), reply_markup=ikb_menu)
    else:
        pass


@dp.callback_query_handler(text='vol_up')
async def volume_up(call: types.CallbackQuery):
    pag.hotkey("fn", "volumeup")
    await call.answer(_("↗ Громкость увеличена на 2"))


@dp.callback_query_handler(text='vol_down')
async def volume_up(call: types.CallbackQuery):
    pag.hotkey("fn", "volumedown")
    await call.answer(_("↘ Громкость уменьшена на 2"))


@dp.callback_query_handler(text='vol_mute')
async def volume_mute(call: types.CallbackQuery):
    pag.hotkey("fn", "volumemute")
    await call.answer(_("⛔ Звук выключен"))
