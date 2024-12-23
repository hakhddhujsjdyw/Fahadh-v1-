
# pyrogram imports
from pyrogram.types import Message, InlineKeyboardButton, InlineKeyboardMarkup, CallbackQuery
from pyrogram import filters, Client, enums, errors
from pyrogram.errors import UserNotParticipant, PeerIdInvalid, UserIsBlocked


# bots imports
from RknDeveloper.database import rkn_botz
from configs import rkn1
import random, asyncio, os

@Client.on_chat_join_request()
async def accept_request(bot, r):

    rm = InlineKeyboardMarkup([[
        InlineKeyboardButton("✛ Aᴅᴅ Mᴇ Tᴏ Yᴏᴜʀ Cʜᴀɴɴᴇʟ ࿇", url=f"https://t.me/{bot.username}?startchannel=Bots4Sale&admin=invite_users+manage_chat")
        ],[
        InlineKeyboardButton("✛ Aᴅᴅ Mᴇ Tᴏ Yᴏᴜʀ Gʀᴏᴜᴘ ࿇", url=f"https://t.me/{bot.username}?startgroup=Bots4Sale&admin=invite_users+manage_chat")     
    ]])
    
    try:
        await bot.send_message(
            r.from_user.id,
            f"**𝖧𝖾𝗅𝗅𝗈 {r.from_user.mention} 👻\n\n 𝖶𝖾𝗅𝖼𝗈𝗆𝖾 𝖳𝗈 {r.chat.title} 𝖸𝗈𝗎𝗋 𝖱𝖾𝗊𝗎𝖾𝗌𝗍 𝖧𝖺𝗌 𝖡𝖾𝖾𝗇 𝖠𝗉𝗉𝗋𝗈𝗏𝖾𝖽.\n\nSend /start to know more**",
            reply_markup=rm)
                        
    except UserIsBlocked:
        print("User blocked the bot")
    except PeerIdInvalid:
        print("Err")
    except Exception as e:
        print(f"#Error\n{str(e)}")

    await r.approve()
         
@Client.on_message(filters.command("start"))
async def start_commond(bot, m :Message):
    if m.chat.type in [enums.ChatType.GROUP, enums.ChatType.SUPERGROUP]:
        await rkn_botz.add_chat(bot, m)
        return await m.reply_text("**❣️ Hᴇʟʟᴏ {}!\n\nWʀɪᴛᴇ Mᴇ Pʀɪᴠᴀᴛᴇ Fᴏʀ Mᴏʀᴇ Dᴇᴛᴀɪʟs.**".format(m.from_user.first_name), reply_markup=InlineKeyboardMarkup(
                [
                    [
                        InlineKeyboardButton("Pʀɪᴠᴀᴛᴇ", url=f"https://t.me/{bot.username}?start=start")
                    ]
                ]
            ))
            
    await rkn_botz.add_user(bot, m)   
    await m.reply_text("**Hᴇy, {}!\n\nI'ᴍ Aɴ Aᴜᴛᴏ Aᴘᴘʀᴏᴠᴇ Bᴏᴛ.\nI Cᴀɴ Aᴘᴘʀᴏᴠᴇ Usᴇʀs Iɴ Cʜᴀɴɴᴇʟs & Gʀᴏᴜᴘs.Aᴅᴅ Mᴇ Tᴏ Yᴏᴜʀ Cʜᴀɴɴᴇʟ Aɴᴅ Gʀᴏᴜᴘ ᴀɴᴅ Pʀᴏᴍᴏᴛᴇ Mᴇ Tᴏ Aᴅᴍɪɴ Wɪᴛʜ Aᴅᴅ Mᴇᴍʙᴇʀs Pᴇʀᴍɪssɪᴏɴ.\n\n__Pᴏᴡᴇʀᴅ Bʏ : @MCUupdatesLINKS__**".format(m.from_user.mention), reply_markup=InlineKeyboardMarkup([[                
                InlineKeyboardButton("✛ Aᴅᴅ Mᴇ Tᴏ Yᴏᴜʀ Cʜᴀɴɴᴇʟ ࿇", url=f"https://t.me/{bot.username}?startchannel=Bots4Sale&admin=invite_users+manage_chat")
                    ],[
                InlineKeyboardButton("✛ Aᴅᴅ Mᴇ Tᴏ Yᴏᴜʀ Gʀᴏᴜᴘ ࿇", url=f"https://t.me/{bot.username}?startgroup=Bots4Sale&admin=invite_users+manage_chat")
                ],[
                InlineKeyboardButton("💥 Uᴘᴅᴀᴛᴇ 💥", url="http://t.me/+pBkpSCdh8IQzNjJl"),
                InlineKeyboardButton("🔎 Sᴜᴘᴘᴏʀᴛ 🔍", url="https://t.me/+uUxCcQ6eanxjZDE1")
            ]]))
            
 
@Client.on_callback_query(filters.regex("start"))
async def start_query(bot, cb : CallbackQuery):
    await cb.message.edit("**Hᴇy, {}!\n\nI'ᴍ Aɴ Aᴜᴛᴏ Aᴘᴘʀᴏᴠᴇ [Aᴅᴍɪɴ Jᴏɪɴ Rᴇǫᴜᴇsᴛs]({}) Bᴏᴛ.\nI Cᴀɴ Aᴘᴘʀᴏᴠᴇ Usᴇʀs Iɴ Cʜᴀɴɴᴇʟs & Gʀᴏᴜᴘs.Aᴅᴅ Mᴇ Tᴏ Yᴏᴜʀ Cʜᴀɴɴᴇʟ Aɴᴅ Gʀᴏᴜᴘ ᴀɴᴅ Pʀᴏᴍᴏᴛᴇ Mᴇ Tᴏ Aᴅᴍɪɴ Wɪᴛʜ Aᴅᴅ Mᴇᴍʙᴇʀs Pᴇʀᴍɪssɪᴏɴ.\n\n__Powerd By : @MCUupdatesLINKS__**".format(cb.from_user.mention), reply_markup=InlineKeyboardMarkup([[                
                InlineKeyboardButton("✛ Aᴅᴅ Mᴇ Tᴏ Yᴏᴜʀ Cʜᴀɴɴᴇʟ ࿇", url=f"https://t.me/{bot.username}?startchannel=Bots4Sale&admin=invite_users+manage_chat")
                    ],[
                InlineKeyboardButton("✛ Aᴅᴅ Mᴇ Tᴏ Yᴏᴜʀ Gʀᴏᴜᴘ ࿇", url=f"https://t.me/{bot.username}?startgroup=Bots4Sale&admin=invite_users+manage_chat")
                ],[
                InlineKeyboardButton("💥 Uᴘᴅᴀᴛᴇ 💥", url="http://t.me/+pBkpSCdh8IQzNjJl"),    
                InlineKeyboardButton("🔎 Sᴜᴘᴘᴏʀᴛ 🔍", url="https://t.me/+uUxCcQ6eanxjZDE1")
            ]]))
    
