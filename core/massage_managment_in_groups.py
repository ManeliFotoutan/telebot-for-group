import telebot
import os
from dotenv import load_dotenv

load_dotenv()

API_TOKEN = os.getenv("API_TOKEN")

bot = telebot.TeleBot(API_TOKEN)

BAD_WORDS = ["ق ه ر م", "کیوحرم","بیشعور", "کثافت", "قهرم"]

@bot.message_handler(func=lambda message: message.chat.type in ["group", "supergroup"])
def handle_messages(message):
    print(f"Message from {message.from_user.first_name}: {message.text}")  

    if message.text:  
        if any(word in message.text.lower() for word in BAD_WORDS):
            try:
                bot.delete_message(message.chat.id, message.message_id) 
                bot.send_message(message.chat.id, f"🚨 {message.from_user.first_name} لطفاً از کلمات مناسب‌تری استفاده کن!")  
            except telebot.apihelper.ApiException as e:
                print(f"Error deleting message: {e}")

bot.infinity_polling()
