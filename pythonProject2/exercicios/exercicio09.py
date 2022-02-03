from random import randint
from time import sleep
itens = ('pedra', 'papel', 'tesoura')
computador = randint(0, 2)
print('''Suas opções:
[0] Pedra
[1] Papel
[2] Tesoura''')
jogador = int(input('Qual é a sua jogada? '))
print('JO')
sleep(1)
print('KEN')
sleep(1)
print('PO =!!!')
print('-=' * 12)
print('O computador jogou {} '.format(itens[computador]))
print('O jogador jogou {} '.format(itens[jogador]))
print('-=' * 12)
if computador == 0: # computador jogou pedra
    if jogador == 0:
        print("EMPATE")
    elif jogador == 1:
        print('JOGADOR VENCOU! ')
    elif jogador == 2:
        print('COMPUTADOR VENCEU!')
    else:
        print('JOGADA INVALIDA !')
elif computador == 1: # computador jogou papel
    if jogador == 0:
        print('COMPUTADOR VENCEU!')
    elif jogador == 1:
        print('EMPATE!')
    elif jogador ==2:
        print('JOGADOR VENCEU!')
    else:
        print('JOGADA INVALIDA ! ')
elif computador == 2: # computador jogou tesoura
    if jogador == 0:
        print('JOGADOR VENCEU!')
    elif jogador == 1:
        print('COMPUTADOR VENCEU!')
    elif jogador == 2:
        print('EMPATE!')
    else:
        print('JOGADA INVALIDA ! ')
