from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

share_contact_keyboard = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text="📞 Telefon raqamni yuborish", request_contact=True)
        ]
    ],
    resize_keyboard=True,
    one_time_keyboard=True
)