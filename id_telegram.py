#como descobrir seu id no chat do telegram
import telebot
import time

chave_api = "7576094527:AAHfjv4RLIZClltDwBgZhJPjJDI6OzruUhc"

bot = telebot.TeleBot(chave_api)

@bot.message_handler(commands=['start']) #Após digitar /start ele irá lhe retornar o seu id
def send_welcome(message):
    chat_id = message.chat.id
    bot.reply_to(message, f"Seu chat ID é: {chat_id}")

bot.polling()