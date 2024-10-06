import telebot
import time

#Token do bot
token = '7576094527:AAHfjv4RLIZClltDwBgZhJPjJDI6OzruUhc'
bot = telebot.TeleBot(token)

#Id da conversa
chat_id = '1884768237'


# Função que envia a mensagem repetidamente
def send_auto_message():
    bot.send_message(chat_id,"Mensagem automática!")

while True:
    send_auto_message()
    time.sleep(10)

    
# Inicia o envio
bot.polling()
