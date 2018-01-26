# Arda - Inteligencia Artificial
# By Pedro Corin - 2018

print('Olá! Qual seu nome?')
nome = input('>: ')

if 'Pedro' in nome:
    print('Hello Sir!')
else:
    print('Muito prazer {}!'.format(nome))

while True:
    resp = input('>: ')
    if resp == 'tchau!':
        break
    else:
        print('Vamos continuar conversando')
print('Bye, bye {}'.format(nome))
