from datetime import date
atual = date.today().year
print('você nao precisa realizar o alistamento obrigatorio')
nasc = int(input('ano de nascimento: '))
idade = atual - nasc
print('quem nasceu em {} tem {} anos em {} '.format(nasc, idade, atual))
if idade == 18:
    print('você tem que se alistar imediatamente')
elif idade < 18:
    saldo1 = 18 - idade
    print('voce deverá se alistra em {} anos'.format(saldo1))
    print('seu alistameto será em {} '.format(atual + saldo1))
elif idade > 18:
    saldo2 = idade - 18
    print('seu alistamento foi a {} anos '.format(saldo2))
    print('seu alistamento ocorreu em {} '.format(atual - saldo2))
