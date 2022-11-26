from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

ikb_menu = InlineKeyboardMarkup(row_width=2,
                                inline_keyboard=[
                                    [
                                        InlineKeyboardButton(text="↗", callback_data="vol_up"),
                                        InlineKeyboardButton(text="↘", callback_data="vol_down")
                                    ],
                                    [
                                        InlineKeyboardButton(text="Мьют", callback_data="vol_mute")
                                    ]
                                ])
