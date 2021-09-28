#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# (c) @AlbertEinsteinTG

from pyrogram import filters, Client
from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup, CallbackQuery
from bot import Translation, LOGGER # pylint: disable=import-error
from bot.database import Database # pylint: disable=import-error

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
                caption = f"<b>{file_name}</b>\n \n<b>┈••✿ @MOVIESWORLD52 ✿••┈</b>\n \n<b>➠𝐂ʜᴀɴɴᴇʟ : @MOVIESWORLD54</b>",
                parse_mode="html",
                reply_markup=InlineKeyboardMarkup(
                    [
                        [
                            InlineKeyboardButton
                                (
                                    '⚠️ 𝙅𝙊𝙄𝙉', url="https://t.me/MOVIESWORLD52"
                                )
                        ],
                        [
                            InlineKeyboardButton
                                (
                                    '⚠️ 𝙅𝙊𝙄𝙉', url="https://t.me/MOVIESWORLD54"
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
        InlineKeyboardButton('💡 𝙃𝙀𝙇𝙋', callback_data="help"),
        InlineKeyboardButton('🔐 𝘾𝙇𝙊𝙎𝙀', callback_data="close")
    ]]
    
    reply_markup = InlineKeyboardMarkup(buttons)
    
    await bot.send_vedio(
        chat_id=update.chat.id,
        vedio="https://telegra.ph/file/c69f27daf9873fd3e6dc9.mp4",
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
