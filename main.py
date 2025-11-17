import telebot
import os

# قراءة التوكن والـ ID من المتغيرات
TOKEN = os.getenv("BOT_TOKEN")
ADMIN_ID = int(os.getenv("USER_ID"))

bot = telebot.TeleBot(TOKEN)

@bot.message_handler(commands=['start'])
def start(msg):
    bot.reply_to(msg, "⚡ qمرحباً! البوت يعمل بنجاح.\nأهلاً بك يا LION.")

@bot.message_handler(func=lambda m: True)
def echo(msg):
    bot.reply_to(msg, f"🦁 تم الاستلام: {msg.text}")

bot.infinity_polling()
