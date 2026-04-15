import telebot

chave_api = "7576094527:AAHfjv4RLIZClltDwBgZhJPjJDI6OzruUhc" #Coloque o token aqui

bot = telebot.TeleBot(chave_api) #inicializando a biblioteca

#Abaixo está todas as funções disponíveis no script

@bot.message_handler(commands= ["pizza"])
def pizza(mensagem):
    bot.send_message(mensagem.chat.id, "Saindo a pizza para sua casa.")

@bot.message_handler(commands= ["hamburguer"])
def hamburguer(mensagem):
    bot.send_message(mensagem.chat.id, "Saindo o hamburgao!")

@bot.message_handler(commands=["hotdog"])
def hotdog(mensagem):
    bot.send_message(mensagem.chat.id, "A salsicha faz mal!")

@bot.message_handler(commands= ["opcao1"])
def opcao1(mensagem):
    texto = """
    Oque você deseja comer?
    /pizza PIZZA
    /hamburguer HAMBURGUER
    /hotdog HOT - DOG
    """
    bot.send_message(mensagem.chat.id, texto)

@bot.message_handler(commands= ["opcao2"])
def opcao2(mensagem):
    bot.send_message(mensagem.chat.id, "Para enviar uma reclamação, mande um email para a empresa")

@bot.message_handler(commands= ["opcao3"])
def opcao3(mensagem):
    bot.send_message(mensagem.chat.id, "Robô feito em python!")

def verificar(mensagem):
    return True


@bot.message_handler(func= verificar)
def responder(mensagem):
    texto = """
    Escolha uma opção para continuar (Clique no item):
    /opcao1 Fazer um pedido
    /opcao2 Reclamar de um pedido
    /opcao3 Qual linguagem foi usada?
    Responder qualquer outra coisa não vai funcionar, clique em uma das opções
    """
    bot.reply_to(mensagem,texto)

bot.polling() #Deixar o script em loop