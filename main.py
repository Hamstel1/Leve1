from datetime import time
import telebot

TOKEN = "7972048139:AAHZrA8TlHBJjE9IM9QRgy-zpB-_enYV-I0"

bot = telebot.TeleBot(TOKEN)

@bot.message_handler(commands=['start'])
def send_welcome(message):
    bot.send_message(message.chat.id, 'Привет ты написал мне /start')













while True:
    try:
        bot.polling(none_stop=True)
    except Exception as e:
        print(e)
        time.sleep()


