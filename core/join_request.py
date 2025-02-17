import telebot
import os
from dotenv import load_dotenv
from telebot import types

load_dotenv()

API_TOKEN = os.getenv("API_TOKEN")

bot = telebot.TeleBot(API_TOKEN)

@bot.chat_member_handler()
def handle_new_chat_members(message: types.ChatMemberUpdated):
    if message.new_chat_member.status == 'member':
        bot.send_message(message.chat.id, f"Welcome {message.new_chat_member.user.first_name}!")

@bot.message_handler(content_types=['new_chat_members'])
def on_new_member(message):
    for new_member in message.new_chat_members:
        bot.send_message(message.chat.id, f"Welcome {new_member.first_name}!")
        bot.approve_chat_join_request(message.chat.id, new_member.id)

bot.infinity_polling()
