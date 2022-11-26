from aiogram import types
import os
import time

from loader import dp
from bot.data.config import OWNER as own
from bot.middlewares.i18n import setup_middleware

i18n = setup_middleware(dp)
_ = i18n.gettext


@dp.message_handler(content_types=["photo"])
async def downl_photo(message: types.Message):
    if message.from_user.id == own:
        await message.photo[-1].download(destination_file=f"bot/img/{message.message_id}.jpg")
        os.startfile(f"D:/.Develop/.Codes/.Python/Other/Lexsi/bot/img/{message.message_id}.jpg")
        # os.startfile(f"C:/Users/1/Desktop/папка/img{message.message_id}.jpg")
        time.sleep(3)
        await message.reply(_("🖥 Вывел фото на <b>дисплей</b>"))
    else:
        pass
