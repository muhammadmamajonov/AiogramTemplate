from aiogram import Router, types
from aiogram.filters import CommandStart
from keyboards.defaoult import share_contact_keyboard


router = Router()


@router.message(CommandStart())
async def start_handler(message: types.Message):
    await message.answer("Assaolmu alaykum! Xush kelibsiz!", reply_markup=share_contact_keyboard)


@router.message(lambda message: message.contact is not None)
async def contact_handler(message: types.Message):
    contact = message.contact
    user_id = contact.user_id
    phone_number = contact.phone_number
    first_name = contact.first_name or ""
    last_name = contact.last_name or ""

    await message.answer()
