# import asyncio
#
# from aiogram import types, Bot, Dispatcher
# from aiogram.filters import Command
# from random import *
#
#
# TOKEN = "7391043820:AAF7_1bKC-K_LekoBM4PGdJVEExraR588vc"
# channel_name = "@"
#
# bot = Bot(token=TOKEN)
# dp = Dispatcher()
#
# user_data = {}
#
# @dp.message()
# async def handle_text(message: types.Message):
#     user_id = message.from_user.id
#     if user_id not in user_data or message.text == '/start':
#         await start(message)
#     elif 'holat' not in user_data[user_id]:
#         await shaharlar(message)
#     elif 'shahar' not in user_data[user_id]:
#         await menu(message)
#     elif message.text == '🛍 Buyurtma berish':
#         await buyurtma(message)
#     elif message.text == '⬅️ Ortga':
#         await menu(message)
#     elif message.text == '📖 Buyurtmalar tarixi':
#         await tarix(message)
#     elif message.text == '🔥 Aksiya':
#         await aksiya(message)
#     elif message.text == "🙋🏻‍♂️ Jamoamizga qo'shiling":
#         await jamoa(message)
#
#
#
#
#
# @dp.message(Command("start"))
# async def start(message: types.Message):
#     user_id = message.from_user.id
#     user_data[user_id] = {}
#     button = [
#         [types.KeyboardButton(text="🇷🇺 Русский"), types.KeyboardButton(text="🇺🇿 O'zbekcha"), types.KeyboardButton(text="🇺🇸 English")]
#     ]
#     keyboard = types.ReplyKeyboardMarkup(keyboard=button, resize_keyboard=True)
#     await message.answer("Assalomu alaykum! \n Les Ailes yetkazib berish xizmatiga xush kelibsiz.\n\n"
#                          "Здравствуйте! Добро пожаловать в службу доставки Les Ailes.\n\n"
#                          "Hello! Welcome to Les Ailes delivery service.", reply_markup=keyboard)
#     print(user_data)
#
# async def shaharlar(message: types.Message):
#     user_id = message.from_user.id
#     language = message.text
#     user_data[user_id]['holat'] = language
#     button = [
#         [types.KeyboardButton(text='Toshkent'), types.KeyboardButton(text='Andijon')],
#         [types.KeyboardButton(text='Samarqand'), types.KeyboardButton(text="Farg'ona")],
#         [types.KeyboardButton(text='Buxoro'), types.KeyboardButton(text="Marg'ilon")],
#         [types.KeyboardButton(text='Nukus'), types.KeyboardButton(text='Xorazm')],
#         [types.KeyboardButton(text='Chirchiq'), types.KeyboardButton(text="Qo'qon")],
#     ]
#     keyboard = types.ReplyKeyboardMarkup(keyboard=button, resize_keyboard=True)
#     await message.answer('Qaysi shaharda yashaysiz? \nIltimos, shaharni tanlang:',reply_markup=keyboard)
#     print(user_data)
#
# async def menu(message: types.Message):
#     user_id = message.from_user.id
#     shahar = message.text
#     user_data[user_id]['shahar'] = shahar
#     button = [
#         [types.KeyboardButton(text='🛍 Buyurtma berish')],
#         [types.KeyboardButton(text='📖 Buyurtmalar tarixi')],
#         [types.KeyboardButton(text="⚙️Sozlash ℹ️ Ma'lumotlar"), types.KeyboardButton(text="🔥 Aksiya")],
#         [types.KeyboardButton(text="🙋🏻‍♂️ Jamoamizga qo'shiling"), types.KeyboardButton(text="☎️ Les Ailes bilan aloqa")],
#     ]
#     keyboard = types.ReplyKeyboardMarkup(keyboard=button, resize_keyboard=True)
#     await message.answer('Bosh menyu',reply_markup=keyboard)
#     print(user_data)
#
# async def buyurtma(message: types.Message):
#     user_id = message.from_user.id
#     user_data[user_id]['holat'] = 'buyurtma'
#     button = [
#         [types.KeyboardButton(text='🏃 Olib ketish'), types.KeyboardButton(text='🚙 Yetkazib berish')],
#         [types.KeyboardButton(text='⬅️ Ortga')]
#     ]
#     keyboard = types.ReplyKeyboardMarkup(keyboard=button, resize_keyboard=True)
#     await message.answer("Buyurtmani o'zingiz 🙋‍♂️ olib keting yoki Yetkazib berishni 🚙 tanlang", reply_markup=keyboard)
#     print(user_data)
#
#
# async def tarix(message: types.Message):
#     user_id = message.from_user.id
#     tarix = message.text
#     user_data[user_id]['tarix'] = tarix
#     button = [
#         [types.KeyboardButton(text="📞Raqamni jo'natish"), types.KeyboardButton(text='⬅️ Ortga')]
#     ]
#     keyboard = types.ReplyKeyboardMarkup(keyboard=button, resize_keyboard=True)
#     await message.answer("Avval ro'yxatdan o'ting",)
#     await message.answer("Ro'yxatdan o'tish uchun teelfon raqamingizni kiriting!\nMisol uchun, +998xx xxx xx xx", reply_markup=keyboard)
#     print(user_data)
#
# async def aksiya(message: types.Message):
#     user_id = message.from_user.id
#     aksiya = message.text
#     user_data[user_id]['aksiya'] = aksiya
#     await message.answer("Shahringizda hali aksiyalar mavjud emas")
#
#
# async def jamoa(message: types.Message):
#     user_id = message.from_user.id
#     jamoa = message.text
#     user_data[user_id]['jamoa'] = jamoa
#     button = [
#         [types.InlineKeyboardButton(text="O'tish",callback_data='text')]
#     ]
#     keyboard = types.InlineKeyboardMarkup(inline_keyboard=button, resize_keyboard=True)
#     await message.answer("Ahil jamoamizda ishlashga taklif qilamiz! Telegramdan chiqmay, shu yerning o'zida anketani to'ldirish uchun quyidagi tugmani bosing.",reply_markup=keyboard)
#
# async def main():
#     await dp.start_polling(bot)
#
#
# print('The bot is running...')
# asyncio.run(main())