from aiogram.contrib.middlewares.i18n import I18nMiddleware as BaseI18nMiddleware
from aiogram import types
from typing import Tuple, Any

from bot.data.config import I18N_DOMAIN, LOCALES_DIR, LANG


async def get_lang(user_id):
    return LANG


class ACLMiddleware(BaseI18nMiddleware):
    async def get_user_locale(self, action: str, args: Tuple[Any]):
        user = types.User.get_current()
        return await get_lang(user.id) or user.locale


def setup_middleware(dp):
    i18n = ACLMiddleware(I18N_DOMAIN, LOCALES_DIR)
    dp.middleware.setup(i18n)
    return i18n
