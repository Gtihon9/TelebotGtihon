import telebot

bot = telebot.TeleBot('1195584879:AAFOmIELuwzaOJqBHSmwVqvxI3sf25eMhgs')

@bot.message_handler(commands=['start'])
def start(message):
    send_mess = f"Hi {message.from_user.first_name} !"
    bot.send_message(message.from_user.id, send_mess)

@bot.message_handler(func=lambda message: True)
def upper(message):
    bot.reply_to(message, message.text.upper())

bot.polling(none_stop=True)