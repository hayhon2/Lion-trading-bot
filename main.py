import telebot
import os

# ضع التوكن هنا
TOKEN = "8143605867:AAHN3qthuwKoG_K5bm9h56KzzP-ePodedeA"
bot = telebot.TeleBot(TOKEN)

# ضع ال ID هنا
ADMIN_ID = 6568396855

@bot.message_handler(commands=['start'])
def start(msg):
    bot.reply_to(msg, "⚡ مرحباً! البوت يعمل بنجاح.\nأهلاً بك يا LION.")

@bot.message_handler(func=lambda m: True)
def echo(msg):
    bot.reply_to(msg, "🦁 تم الاستلام: " + msg.text)

bot.infinity_polling()
