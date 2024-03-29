from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup

start_inline = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(text="Foto", callback_data="Foto"),
            InlineKeyboardButton(text="Music", callback_data="Music"),
            InlineKeyboardButton(text="Document", callback_data="Document"),

        ]
    ]
)
