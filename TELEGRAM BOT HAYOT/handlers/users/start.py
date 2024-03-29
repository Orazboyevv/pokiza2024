from aiogram import types
from aiogram.dispatcher.filters.builtin import CommandStart
from keyboards.default.keyboard import start_button, music_button
from keyboards.inline.inline_button import start_inline
from loader import dp
from filters.admin_filter import AdminFilter
from filters.group_filter import IsGroup
from filters.private_filter import IsPrivate

@dp.message_handler(CommandStart())
async def bot_start(message: types.Message):
    await message.answer(f"Salom, {message.from_user.full_name}!", reply_markup=start_button)


@dp.message_handler(text="Cs_1.6 download🔥")
async def kino(msg:types.Message):
    kino = open("static/apk/SteamSetup.exe","rb")
    text = "Cs_1.6 Orginal"
    await msg.answer_document(document=kino , reply_markup=start_button)


# @dp.callback_query_handler(text="Foto")
# async def foto(msg: types.Message):
#     foto = open("static/image/start.jpg", "rb")
#     text = "Rasmmi dodasi"
#     await msg.ansver(text, replay_markup=start_inline)
#     await msg.answer_photo(photo=foto)

@dp.message_handler(text="Foto")
async def rasm(msg:types.Message):
    text = "Rasimmi dodasi"
    rasm = open(text,"static/image/start.jpg", "rb")
    await msg.answer_photo(photo=rasm,reply_markup=start_inline)





@dp.message_handler(text="Chit kod🧑🏻‍💻")
async def Music(msg: types.Message):
    text = "Kekarakli tugmani tanlang"
    await msg.answer(text, reply_markup=music_button)


@dp.message_handler(text="отдача Chit✍🏻")
async def musicc(msg: types.Message):
    text = """sv_cheats 1
              impulse 101
              sv_aim 15
              cl_cmdrate 101
              cl_updaterate 101
              rate 25000
              sv_maxrate25000
              sv_minrate25000
              sv_minupdaterate 101
              gl_zmax 8192
              gl_spriteblend 0"""
    await msg.answer(text,reply_markup=start_button)

@dp.message_handler(text="прицел Chit ╾━╤デ╦︻(•⤙•) ")
async def muusic(msg:types.Message):
    text = """cl_lw 1
              cl_lc 1
              cl_dynamiccrosshair
              +duck
              cl_lw 0
              cl_lc 0
              -duck
              cl_dynamiccrosshair 0
              net_garph 1"""
    await msg.answer(text,reply_markup=start_button)

@dp.message_handler(text="Skin, Pack🧢")
async def musiic(msg:types.Message):
    musiic = open("static/document/aiogram-bot-template-master.zip","rb")
    await msg.answer_document(document=musiic)

@dp.message_handler(text="GO BACK")
async def go_back(msg: types.Message):
    await msg.answer("Oraqaga qaytildi", reply_markup=start_button)



