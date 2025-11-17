
import telebot
import os

TOKEN = os.getenv("BOT_TOKEN", "PUT-YOUR-TOKEN-HERE")
bot = telebot.TeleBot(TOKEN)

@bot.message_handler(commands=['start'])
def start(msg):
    bot.reply_to(msg, "مرحباً! البوت يعمل بنجاح ⚡")

@bot.message_handler(func=lambda m: True)
def echo(msg):
    bot.reply_to(msg, "تم الاستلام: " + msg.text)

bot.infinity_polling()
