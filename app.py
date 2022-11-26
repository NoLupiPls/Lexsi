async def on_startup(dp):
    import bot.filters as filters
    filters.setup(dp)

    from bot.utils.notify_admins import on_startup_notify
    await on_startup_notify(dp)

    from bot.utils.set_bot_commands import set_default_commands
    await set_default_commands(dp)
    print('Бот запущен')


if __name__ == '__main__':
    from aiogram import executor
    from bot.handlers import dp

    executor.start_polling(dp, on_startup=on_startup)
