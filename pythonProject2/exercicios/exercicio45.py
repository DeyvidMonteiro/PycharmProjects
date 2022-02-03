from random import randint
from time import sleep
lista = []
jogos = []
print('=-' * 30)
print(f'      JOGA DA MEGA SENA      ')
print('=-' * 30)
quant = int(input('quantos jogos quer sortear? '))
tot = 0
while tot <= quant:
    cont = 0
    while True:
        num = randint(1, 60)
        if num not in lista:
            lista.append(num)
            cont += 1
        if cont >= 6:
            break
    lista.sort()
    jogos.append(lista[:])
    lista.clear()
    tot += 1
print('-=' * 3, f'sorteando {quant} jogos', '-=' * 3)
for i, l in enumerate(jogos):
    print(f'Jogo {i}: {l} ')
    sleep(1)
