import telebot
import os
from dotenv import load_dotenv
from telebot import types

load_dotenv()

API_TOKEN = os.getenv("API_TOKEN")
bot = telebot.TeleBot(API_TOKEN)

@bot.message_handler(commands=['pin'])
def pin_message(message):
    bot.send_message(message.chat.id, "Give the message you want to pin.")
    bot.register_next_step_handler(message, message_pinner)

def message_pinner(message):
    bot.pin_chat_message(message.chat.id, message.message_id)

bot.infinity_polling()
