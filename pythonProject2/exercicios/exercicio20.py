somaid = 0
mediaid = 0
maiorho = 0
nomevelho = ''
totm20 = 0
for p in range(1, 5):
    print('----------- {}° Pessoa -----------'.format(p))
    nome = str(input('Nome ')).strip()
    idade = int(input('Idade: '))
    sexo = str(input('Sexo [M/F]: ')).strip()
    somaid += idade
    if p == 1 and sexo in 'Mm':
        maiorho = idade
        nomevelho = nome
    if sexo in 'Mm' and idade > maiorho:
        maiorho = idade
        nomevelho = nome
    if sexo in 'Ff' and idade > 20:
        totm20 += 1
mediaid = somaid / 4
print('A media de idade do grupo é de {} anos '.format(mediaid))
print('O homen mais velho tem {} anos e se chama {}'.format(maiorho, nomevelho))
print('Ao todo sao {} mulheres com menos de 20 anos '.format(totm20))
