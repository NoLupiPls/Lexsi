from aiogram import types
import os
import time

from loader import dp
from bot.data.config import OWNER as own


@dp.message_handler(content_types=["photo"])
async def downl_photo(message: types.Message):
    if message.from_user.id == own:
        await message.photo[-1].download(destination_file=f"bot/img/{message.message_id}.jpg")
        os.startfile(f"D:/.Develop/.Codes/.Python/Other/Lexsi/bot/img/{message.message_id}.jpg")
        # os.startfile(f"C:/Users/1/Desktop/папка/img{message.message_id}.jpg")
        time.sleep(3)
        await message.reply("🖥 Вывел фото на <b>дисплей</b>")
    else:
        pass
