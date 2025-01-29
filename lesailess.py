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
#     elif 'phone' not in user_data[user_id]:
#         await send_code(message)
#     elif 'status' not in user_data[user_id]:
#         await check_code(message)
#     elif 'location' not in user_data[user_id]:
#         await info_location(message)
#     elif 'kategoriyalar' in user_data[user_id]['holat']:
#         await show_menu(message)
#     elif 'tovarlar' in user_data[user_id]['holat']:
#         await check_menu(message)
#     elif 'tovar' in user_data[user_id]['holat']:
#         await check_items(message)
#
#
# @dp.message(Command("start"))
# async def start(message: types.Message):
#     user_id = message.from_user.id
#     user_data[user_id] = {}
#     button = [
#         [types.KeyboardButton(text="Raqam jo'natish", request_contact=True)]
#     ]
#     keyboard = types.ReplyKeyboardMarkup(keyboard=button, resize_keyboard=True)
#     await message.answer("Assalomu alaykum! \n Les Ailes yetkazib berish xizmatiga xush kelibsiz:", reply_markup=keyboard)
#     print(user_data)


async def send_code(message: types.Message):
    user_id = message.from_user.id
    i = '+1234567890'
    ok = True
    if message.contact is not None:
        phone_c = message.contact.phone_number
        user_data[user_id]['phone'] = phone_c
        verification_code = randint(100000, 999999)
        user_data[user_id]['verification_code'] = verification_code
        await message.answer(f"Nomerizga tasdiqlash ko'di yuborildi\n"
                         f"Iltimos kodni kiriting: {verification_code}")
    elif len(message.text) == 13 and message.text[0:4]  == '+998':
         for symbol in message.text:
             if symbol not in i:
                await message.answer('Hato nomer kiritildi')
                var = ok == False
                break

         if ok == True:
            phone = message.text
            user_data[user_id]['phone'] = phone
            verification_code = randint(100000, 999999)
            user_data[user_id]['verification_code'] = verification_code
            await message.answer(f"Nomerizga tasdiqlash ko'di yuborildi\n"
                                 f"Iltimos kodni kiriting: {verification_code}")

    else:
        await message.answer('Hato nomer kiritildi')
    print(user_data)

async def check_code(message: types.Message):
    user_id = message.from_user.id
    code = message.text
    verification_code = user_data[user_id]['verification_code']
    if str(verification_code) == code:
        user_data[user_id]['status'] = 'verified'
        await message.answer("Nomeringiz tasdiqlandi")
        await ask_location(message)
    else:
        await message.answer('Kod hato terildi. Yana urunib koring')
    print(user_data)



async def ask_location(message:types.Message):
    user_id = message.from_user.id
    if 'location' in user_data[user_id]:
        del user_data[user_id]['location']
    if 'holat' in user_data[user_id]:
        del user_data[user_id]['holat']
    button = [
        [types.KeyboardButton(text="Loaktsiya jo'natish", request_location=True)]
    ]
    keyboard = types.ReplyKeyboardMarkup(keyboard=button, resize_keyboard=True)
    await message.answer("Loaktsiya jo'natish", reply_markup=keyboard)
    print(user_data)


async def info_location(message: types.Message):
    user_id = message.from_user.id
    if 'location' not in user_data[user_id]:
        if message.location is not None:
            latitude = message.location.latitude
            longitude = message.location.longitude
            location = {
                'latitude': latitude,
                'longitude': longitude
            }
        else:
            location = message.text
        user_data[user_id]['location'] = location
    button = [
        [types.KeyboardButton(text='Buyurtma berish')],
        [types.KeyboardButton(text='Orqaga')]
    ]
    keyboard = types.ReplyKeyboardMarkup(keyboard=button, resize_keyboard=True)
    user_data[user_id]['holat'] = 'kategoriyalar'
    await message.answer(f'Boshladikmi?', reply_markup=keyboard)
    print(user_data)


menu = {
    'Burgerlar': {'Cheeseburger':27000, 'Chiliburger':26000, 'Humberger':25000},
    'Tovuqlar': {'Qanotlar':30000, 'Oyoqchalar':35000, 'Strips':40000},
    'Ichimliklar': {'Ice-Tea':17000, 'Choy':4000, 'Moxito':17000}
}



async def show_menu(message: types.Message):
    user_id = message.from_user.id
    user_data[user_id]['holat'] = 'tovarlar'
    if message.text == 'Buyurtma berish':
        buttons = []
        for category in menu:
            button = [types.KeyboardButton(text = category)]
            buttons.append(button)
        button_back = [types.KeyboardButton(text='Orqaga')]
        buttons.append(button_back)
        keyboard = types.ReplyKeyboardMarkup(keyboard=buttons, resize_keyboard=True)
        await message.answer(f'Nimadan boshlaymiz?', reply_markup=keyboard)
    elif message.text == 'Orqaga':
        await ask_location(message)



async def check_menu(message: types.Message):
    user_id = message.from_user.id
    category = message.text
    user_data[user_id]['category'] = category
    if category in menu:
        await show_items(message)
    elif category == 'Orqaga':
        await info_location(message)



async def show_items(message: types.Message):
    user_id = message.from_user.id
    buttons = []
    category = user_data[user_id]['category']
    for item in menu[category]:
        button = [types.KeyboardButton(text=item)]
        buttons.append(button)
    keyboard = types.ReplyKeyboardMarkup(keyboard=buttons, resize_keyboard=True)
    user_data[user_id]['holat'] = 'tovar'
    await message.answer(f'Nimadan boshlaymiz?', reply_markup=keyboard)



async def check_items(message: types.Message):
    user_id = message.from_user.id
    item = message.text
    category = user_data[user_id]['category']
    if item in menu[category]:
        user_data[user_id]['item'] = item
        price = menu[category][item]
        buttons = [
            [types.InlineKeyboardButton(text=f'-', callback_data=f'minus_{item}'),
             types.InlineKeyboardButton(text=f'1', callback_data=f'count_{item}'),
             types.InlineKeyboardButton(text=f'+', callback_data=f'plus_{item}')],
            [types.InlineKeyboardButton(text=f"Savatga qo'shish", callback_data=f'add_{item}')]
        ]
        keyboard = types.InlineKeyboardMarkup(inline_keyboard=buttons)
        await message.answer(f'Tovar: {item}\n'
                             f'Narxi: {price}', reply_markup=keyboard)

count = 1
@dp.callback_query(lambda c: c.data.startswith(('plus', 'minus', 'add')))
async def check_callback_data(callback: types.CallbackQuery):
     user_id = callback.from_user.id
     command, item = callback.data.split('_')
     global count
     if command == 'plus':
         count += 1
     elif command == 'minus':
         if count > 1:
             count -= 1
     elif command == 'add':
         if 'basket' not in user_data[user_id]:
             user_data[user_id]['basket'] = {item:count}
         else:
             user_data[user_id]['basket'][item] = count
         count = 1
         print(user_data)

         buttons = [
             [types.InlineKeyboardButton(text=f'-', callback_data=f'minus_{item}'),
              types.InlineKeyboardButton(text=f'{count}', callback_data=f'count_{item}'),
              types.InlineKeyboardButton(text=f'+', callback_data=f'plus_{item}')],
             [types.InlineKeyboardButton(text=f"Savatga qo'shish", callback_data=f'add_{item}')]
         ]
         keyboard = types.InlineKeyboardMarkup(inline_keyboard=buttons)
         category = user_data[user_id]['category']
         price = menu[category][item]
         price = price * count
         await callback.message.edit_text(f'Tovar: {item}\n'
                                          f'Narxi: {price}', reply_markup=keyboard)
         print('Count:', count)


async def main():
    await dp.start_polling(bot)


print('The bot is running...')
asyncio.run(main())
