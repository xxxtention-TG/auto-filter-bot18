#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# (c) @AlbertEinsteinTG

from pyrogram import filters, Client
from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup, CallbackQuery
from bot import Translation, LOGGER # pylint: disable=import-error
from bot.database import Database # pylint: disable=import-error
import random

PHOTOS = [
    "https://telegra.ph/file/01374b486b931f0bc2f6d.jpg",
    "https://telegra.ph/file/3e899bf95ed39674ca94e.jpg",
    "https://telegra.ph/file/89425c5d6bdeb8d0efdc0.jpg",
    "https://telegra.ph/file/3ed9d0a096ee889b5ae82.jpg",
    "https://telegra.ph/file/c4337f2e3f0c139c2ca69.jpg",
    "https://telegra.ph/file/2213647057cf80f6bff6c.jpg",
    "https://telegra.ph/file/05f3036179db455bceed0.jpg",
    "https://telegra.ph/file/d82ba27c01756aad907d6.jpg",
    "https://telegra.ph/file/a636580c4b1c4ddbd8240.jpg",
    "https://telegra.ph/file/62fdee7cdd574952a89e3.jpg",
    "https://telegra.ph/file/27f7c867903c5416e9e94.jpg",
    "https://telegra.ph/file/d7e9529e35670ffbf215d.jpg",
    "https://telegra.ph/file/c69f27daf9873fd3e6dc9.mp4",
]

db = Database()

@Client.on_message(filters.command(["start"]) & filters.private, group=1)
async def start(bot, update):
    
    try:
        file_uid = update.command[1]
    except IndexError:
        file_uid = False
    
    if file_uid:
        file_id, file_name, file_caption, file_type = await db.get_file(file_uid)
        
        if (file_id or file_type) == None:
            return
        
        caption = file_caption if file_caption != ("" or None) else ("<code>" + file_name + "</code>")
        try:
            await update.reply_cached_media(
                file_id,
                quote=True,
                caption = f"<b>{file_name}</b>\n \n<b>┈••✿ @MOVIESWORLD52 ✿••┈</b>\n \n<b>➠𝐂ʜᴀɴɴᴇʟ : https://t.me/joinchat/Xr-vil0sYk85NWM1</b>\n \n<b>➠𝐂ʜᴀɴɴᴇʟ : https://t.me/joinchat/WjcMRPNkHJAxZDk1</b>",
                parse_mode="html",
                reply_markup=InlineKeyboardMarkup(
                    [
                        [
                            InlineKeyboardButton
                                (
                                    '⚠️ 𝖩𝖮𝖨𝖭', url="https://t.me/MOVIESWORLD52"
                                )
                        ],
                        [
                            InlineKeyboardButton
                                (
                                    '⚠️ 𝖩𝖮𝖨𝖭', url="https://t.me/MOVIESWORLD54"
                                ),
                            InlineKeyboardButton
                                (
                                    '⚠️ 𝖩𝖮𝖨𝖭', url="https://t.me/MOVIESWORLD59"
                                )
                        ] 
                    ]
                )
            )
        except Exception as e:
            await update.reply_text(f"<b>Error:</b>\n<code>{e}</code>", True, parse_mode="html")
            LOGGER(__name__).error(e)
        return

    buttons = [[
        InlineKeyboardButton('🕵️‍♂️ 𝘾𝙍𝙀𝘼𝙏𝙊𝙍', url='https://t.me/darkz_angel'),
        InlineKeyboardButton('⚠️ 𝙂𝙍𝙊𝙐𝙋', url ='https://t.me/MOVIESWORLD52')
    ],[
        InlineKeyboardButton('♻️ 𝙅𝙊𝙄𝙉 𝙊𝙐𝙍 𝘾𝙃𝘼𝙉𝙉𝙀𝙇 ♻️', url='https://t.me/MOVIESWORLD52')
    ],[
        InlineKeyboardButton('💡 𝙃𝙀𝙇𝙋', callback_data="help"),
        InlineKeyboardButton('🔐 𝘾𝙇𝙊𝙎𝙀', callback_data="close")
    ]]
    
    reply_markup = InlineKeyboardMarkup(buttons)
    
    await bot.send_photo(
        chat_id=update.chat.id,
        photo=random.choice(PHOTOS),
        caption=Translation.START_TEXT.format(
                update.from_user.first_name),
        reply_markup=reply_markup,
        parse_mode="html",
        reply_to_message_id=update.message_id
    )


@Client.on_message(filters.command(["help"]) & filters.private, group=1)
async def help(bot, update):
    buttons = [[
        InlineKeyboardButton('𝙃𝙊𝙈𝙀 ⚡', callback_data='start'),
        InlineKeyboardButton('𝘼𝘽𝙊𝙐𝙏 🚩', callback_data='about')
    ],[
        InlineKeyboardButton('𝘾𝙇𝙊𝙎𝙀 🔐', callback_data='close')
    ]]
    
    reply_markup = InlineKeyboardMarkup(buttons)
    
    await bot.send_message(
        chat_id=update.chat.id,
        text=Translation.HELP_TEXT,
        reply_markup=reply_markup,
        parse_mode="html",
        reply_to_message_id=update.message_id
    )


@Client.on_message(filters.command(["about"]) & filters.private, group=1)
async def about(bot, update):
    
    buttons = [[
        InlineKeyboardButton('𝙃𝙊𝙈𝙀 ⚡', callback_data='start'),
        InlineKeyboardButton('𝘾𝙇𝙊𝙎𝙀 🔐', callback_data='close')
    ]]
    reply_markup = InlineKeyboardMarkup(buttons)
    
    await bot.send_message(
        chat_id=update.chat.id,
        text=Translation.ABOUT_TEXT,
        reply_markup=reply_markup,
        disable_web_page_preview=True,
        parse_mode="html",
        reply_to_message_id=update.message_id
    )
