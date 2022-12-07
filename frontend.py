import telebot
from config import token

bot = telebot.TeleBot(token)

@bot.message_handler(commands=['help', 'start'])
def send_welcome(message):
	bot.reply_to(message, """\Hi there, I am RosterBot. I am here to make rosters easy!\""")

# @bot.message_handler(func=lambda message: True)
# def echo_message(message):
#    bot.reply_to(message, message.text)

bot.infinity_polling()
	
