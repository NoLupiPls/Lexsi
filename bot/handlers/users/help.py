from aiogram import types

from loader import dp
from bot.data.config import OWNER as own
from bot.middlewares.i18n import setup_middleware

i18n = setup_middleware(dp)
_ = i18n.gettext


@dp.message_handler(commands="help")
async def help_def(message: types.Message):
    if message.from_user.id == own:
        await message.answer(_("""/openc <i>vk</i> - открыть ссылку .com
/openr <i>kinopoisk</i> - ссылка .ru
/st - сверну и замьючу
/sleep - переведу в режим сна
/volume - изменю громкость
/music - открою Яндекс.Музыку
/kino - открою кинопоиск
/tg - открою Telegram
/ru - сверну окна
/pause - пауза видео или музыки
/close - закрою окно
/site <i>https://vk.com/nolupi</i> - вставьте справа ссылку
/imp - открою хуйювёрсе"""))
