# Arda - Inteligencia Artificial
# By Pedro Corin - 2018
from chatterbot.trainers import ListTrainer
from chatterbot import ChatBot

bot = ChatBot('Arda')

conversa = ['Olá','Olá', 'Tudo bem?', 'Tudo ótimo! E com você?','Qual seu nome?','Arda e o seu?']
musica = ['Gosta de música?','Claro que gosto! Quem não iria gosta?','Qual sua banda preferida?','Pink Floyd. E a sua?','Guns','Guns n Roses é demais!']


bot.set_trainer(ListTrainer)
bot.train(conversa)
bot.train(musica)

while True:
    quest = input('Você: ')
    resposta = bot.get_response(quest)
    if float(response.confidence) > 0.5:
        print('Arda: ', resposta)
    else:
        print('Arda: Eu não sei.')

