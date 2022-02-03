from random import randint
v = 0
while True:
    jogador = int(input('Digite um valor: '))
    comp = randint(0, 10)
    total = jogador + comp
    tipo = ' '
    while tipo not in 'PI':
        tipo = str(input('Par ou Impar? [P/I] ')).strip().upper()[0]
    print(f'Você jogou {jogador} e o computador jogou {comp}. Total de {total}', end='')
    print('deu Par ' if total % 2 == 0 else 'deu Impar')
    if tipo == 'P':
        if total % 2 == 0:
            print('você venceu! ')
            v += 1
        else:
            print('você perdeu! ')
            break
    elif tipo == 'I':
        if total % 2 == 1:
            print('Voce venceu!')
            v += 1
        else:
            print('você perdeu! ')
            break
    print('vamos jogar novamente...')
print(f'Game over! você venceu {v} vezes. ')
print('-' * 30)
