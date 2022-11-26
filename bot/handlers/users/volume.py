from aiogram import types
from aiogram.types import CallbackQuery
import pyautogui as pag

from keyboard.inline import ikb_menu
from loader import dp
from bot.data.config import OWNER as own


@dp.message_handler(commands=["volume"])
async def volume(message: types.Message):
    if message.from_user.id == own:
        await message.answer("Кнопки выведены на экран!\n"
                             "<b>Смотрите ниже:</b>", reply_markup=ikb_menu)
    else:
        pass


@dp.callback_query_handler(text='vol_up')
async def volume_up(call: types.CallbackQuery):
    pag.hotkey("fn", "volumeup")
    await call.answer("↗ Громкость увеличена на 2")


@dp.callback_query_handler(text='vol_down')
async def volume_up(call: types.CallbackQuery):
    pag.hotkey("fn", "volumedown")
    await call.answer("↘ Громкость уменьшена на 2")


@dp.callback_query_handler(text='vol_mute')
async def volume_mute(call: types.CallbackQuery):
    pag.hotkey("fn", "volumemute")
    await call.answer("⛔ Звук выключен")