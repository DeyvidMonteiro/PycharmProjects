num = []
while True:
    n = int(input('Digite um valor: '))
    if n not in num:
        num.append(n)
        print('Vaor adicionado com sucesso... ')
    else:
        print('valor duplicado! Não vou adicionar... ')
    r = str(input('Quer continuar? [S/N] '))
    if r in 'Nn':
        break
print('=-' * 30)
num.sort()
print(f'Voce digitou os valores {num} ')
