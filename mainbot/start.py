from pyrogram import filters as vrn
from bot import mainbot
from config import HANDLER, MY_ID
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton

import logging

@mainbot.on_message(vrn.command('start', HANDLER) & vrn.private)
async def start(mainbot, message):
  await message.reply_photo(
    photo = {},
    caption = f"Hola {message.from_user}, I am the horrifying Annabelle userbot made for [this person](t.me/user?id={MY_ID}). The messages you send here will be forwarded to my master",
    reply_markup = InlineKeyboardMarkup([
      [InlineKeyboardMarkup("Contact bot Owner 😉", url="http://t.me/Keerthy_Admin_Bot")],
      [InlineKeyboardButton("Support Channel", url="t.me/+1qdEeHOTLdQ1M2Vl"), InlineKeyboardButton("Group", url="https://t.me/+CG7AQS6IfUNhYTNl")]
      ])
  )
    
@mainbot.on_message(vrn.incoming & vrn.private)
async def frwd(mainbot, message):
  try:
    USER_ID = message.from_user.mention
    await mainbot.forward_message(message.from_user.id, MY_ID)
  except:
    mainbot.send_message(MY_ID, f"{USER_ID} is spamming me! I am not able to forward his messages")
    
