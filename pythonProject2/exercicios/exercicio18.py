from datetime import date
atual = date.today().year
totalma = 0
totalme = 0
for pess in range(1, 8):
    nasc = int(input('Em que ano a {}° pessoa nasceu? '.format(pess)))
    idade = atual - nasc
    if idade >= 21:
       totalma += 1
    else:
        totalme =+ 1
print('Ao todo tivemos {} pessoas maiores de idade '.format(totalma))
print('E também tivemos {} pessoas menosres de idade '.format(totalme))
