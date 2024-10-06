import telebot
import time

#Token do bot
token = '7576094527:AAHfjv4RLIZClltDwBgZhJPjJDI6OzruUhc'
bot = telebot.TeleBot(token)

#Id da conversa
chat_id = '-4504812852'


sinais_teste = """🚥 SINALZINHO GRATUITO 🚥

• EURGBP (OTC) - PUT 🟥  - 19:35
• Expiração: 5 minutos [M5]
• Se perder, fazer até 1 Gale."""
#Exemplo de mensagens para serem programadas

sinais_teste_outro = """🚥 SINALZINHO GRATUITO 🚥

• EURUSD (OTC) - CALL 🟩  - 20:15
• Expiração: 5 minutos [M5]
• Se perder, fazer até 1 Gale.
""" #Exemplo de mensagens para serem programadas

# Função que envia a mensagem repetidamente
def send_auto_message():
    bot.send_message(chat_id, sinais_teste_outro)

def mennsagem():
    bot.send_message(chat_id, sinais_teste)


while True:
    send_auto_message()
    time.sleep(10)
    mennsagem()
    time.sleep(10)


# Inicia o envio
bot.polling()
