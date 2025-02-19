import telebot
import os
from dotenv import load_dotenv
from telebot import types

load_dotenv()
API_TOKEN = os.getenv("API_TOKEN")
bot = telebot.TeleBot(API_TOKEN)

GROUP_RULES = "📌 قوانین گروه:\n1️⃣ رعایت ادب و احترام الزامی است.\n2️⃣ ارسال هرزنامه (اسپم) ممنوع است.\n3️⃣ تبلیغات بدون اجازه مجاز نیست."

@bot.message_handler(commands=['start'])
def send_welcome(message):
    bot.send_message(message.chat.id, "✅ ربات مدیریت گروه فعال شد.")

@bot.message_handler(commands=['pin'])
def pin_message(message):
    bot.send_message(message.chat.id, "Give the message you want to pin.")
    bot.register_next_step_handler(message, message_pinner)

def message_pinner(message):
    bot.pin_chat_message(message.chat.id, message.message_id)
    
@bot.message_handler(commands=['kick'])
def kick_user(message):
    if message.reply_to_message:
        user_id = message.reply_to_message.from_user.id
        bot.kick_chat_member(message.chat.id, user_id)
        bot.send_message(message.chat.id, f"🚫 کاربر [{user_id}] از گروه اخراج شد!")
    else:
        bot.send_message(message.chat.id, "🔺 لطفاً به پیام کاربر ریپلای کنید تا اخراج شود.")

@bot.message_handler(commands=['ban'])
def ban_user(message):
    if message.reply_to_message:
        user_id = message.reply_to_message.from_user.id
        bot.ban_chat_member(message.chat.id, user_id)
        bot.send_message(message.chat.id, f"🚫 کاربر [{user_id}] مسدود شد!")
    else:
        bot.send_message(message.chat.id, "🔺 لطفاً به پیام کاربر ریپلای کنید تا بن شود.")

@bot.message_handler(commands=['unban'])
def unban_user(message):
    if message.reply_to_message:
        user_id = message.reply_to_message.from_user.id
        bot.unban_chat_member(message.chat.id, user_id)
        bot.send_message(message.chat.id, f"✅ کاربر [{user_id}] رفع مسدودیت شد!")
    else:
        bot.send_message(message.chat.id, "🔺 لطفاً به پیام کاربر ریپلای کنید تا از بن خارج شود.")

@bot.message_handler(commands=['promote'])
def promote_user(message):
    if message.reply_to_message:
        user_id = message.reply_to_message.from_user.id
        bot.promote_chat_member(
            message.chat.id,
            user_id,
            can_change_info=True,
            can_delete_messages=True,
            can_invite_users=True,
            can_restrict_members=True,
            can_pin_messages=True,
            can_promote_members=False
        )
        bot.send_message(message.chat.id, f"🎩 کاربر [{user_id}] به ادمین ارتقا یافت!")
    else:
        bot.send_message(message.chat.id, "🔺 لطفاً به پیام کاربر ریپلای کنید تا به ادمین ارتقا یابد.")

@bot.message_handler(commands=['demote'])
def demote_user(message):
    if message.reply_to_message:
        user_id = message.reply_to_message.from_user.id
        bot.promote_chat_member(
            message.chat.id,
            user_id,
            can_change_info=False,
            can_delete_messages=False,
            can_invite_users=False,
            can_restrict_members=False,
            can_pin_messages=False,
            can_promote_members=False
        )
        bot.send_message(message.chat.id, f"🔽 کاربر [{user_id}] به کاربر عادی تنزل یافت.")
    else:
        bot.send_message(message.chat.id, "🔺 لطفاً به پیام کاربر ریپلای کنید تا به کاربر عادی تنزل یابد.")

@bot.message_handler(content_types=['new_chat_members'])
def welcome_new_member(message):
    for new_user in message.new_chat_members:
        welcome_text = f"👋 خوش آمدید {new_user.first_name}!\n{GROUP_RULES}"
        bot.send_message(message.chat.id, welcome_text)

bot.infinity_polling()
