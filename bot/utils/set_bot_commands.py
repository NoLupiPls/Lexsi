from aiogram import types


async def set_default_commands(dp):
    await dp.bot.set_my_commands([
        types.BotCommand('help', 'Help'),
        types.BotCommand('close', 'Close widget'),
        types.BotCommand('st', 'Close and mute'),
        types.BotCommand('tg', 'Open Telegram')
    ])
