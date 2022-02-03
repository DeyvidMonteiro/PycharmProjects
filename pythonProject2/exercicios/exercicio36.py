cont = ('zero', 'um', 'dois', 'tres', 'quatro', 'cinco', 'seis', 'sete',
        'oito', 'nove','dez')
while True:
    num = int(input('Digite um numero: '))
    if 0 <= num <= 10:
        break
    print('tente novamente ', end='')
print('você digitou o numero {} '.format(cont[num]))
