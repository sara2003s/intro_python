'''
Crie um script que simule um jogo de advinhação, onde o computador 
gera um num eor aleatorio entre 1 e 19, e o úsuario tem que advinhar 
qual o número sorteado pelo computador. O usúario terá 3 tentativas
para acertar o número
'''

import random, os

os.system('cls')

print('''Tenta advinhar o número sorteado entre 1 e 10.
 Voce tem 3 tentativas...''')

numero_sorteado = random.randrange(1, 11)
tentativas = 3

palpite = int(input('Qual o seu palpite para o número sorteado? '))

while tentativas > 0:
    tentativas -= 1    
    if palpite == numero_sorteado:
        print('Bingo!!! Voce acertou o número sorteado')
        break # Encerra imediantamente a execução do laço
    elif palpite < numero_sorteado:
        print('Seu palpite foi menor que o número sorteado')
    else:
        print('Seu palpite foi menor do que o número sorteado')

palpite = int(input(f'Voce ainda tem {tentativas} tentativa. Tente novamente:'))

print('########## FIM DO SCRIPT #########')