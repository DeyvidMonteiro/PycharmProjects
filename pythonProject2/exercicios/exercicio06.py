from datetime import date
atual = date.today().year
nasc = int(input('Ano de nascimeno: '))
idade = atual - nasc
print('O atleta tem {} anos. '.format(idade))
if idade <= 9:
    print('Classificação mirim. ')
elif idade <= 14 and idade > 9:
    print('Classificação infantil')
elif idade <= 19 and idade > 14:
    print('Classificação junior ')
elif idade > 19 and idade <= 25:
    print('classificação senior ')
elif idade > 25:
    print('Classificação master ')
