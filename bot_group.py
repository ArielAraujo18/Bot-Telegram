import telebot
import time

# Seu token do bot
bot = telebot.TeleBot('7576094527:AAHfjv4RLIZClltDwBgZhJPjJDI6OzruUhc')

# Função que envia a mensagem repetidamente
@bot.send_message
def send_repeated_message():
    chat_id = '188476823'
    while True:
        bot.send_message(chat_id, "Sua mensagem aqui")
        time.sleep(10)  # Pausa de 20 segundos

# Inicia o envio
bot.polling(send_repeated_message)
