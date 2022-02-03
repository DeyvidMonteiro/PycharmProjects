print('{:=^40}.'.format('loja'))
preço = float(input('Preço das compras: R$ '))
print('''Formas de pagamento 
[1]à vista dinheiro/cheque
[2] à vista cartão
[3] 2x no cartão
[4] 3x ou mais no cartão''')
opção = int(input('Qual a sua opção ? '))
if opção == 1:
    total = preço - (preço * 0.10)
elif opção == 2:
    total = preço - (preço * 0.05)
elif opção == 3:
    total = preço
    parcela = total / 2
    print('sua compra será parcelada em 2x de R$ {:.2f} '.format(parcela))
elif opção == 4:
    total = preço + (preço * 0.20)
    totpar = int(input('quantas parcelas? '))
    parcela = total / totpar
    print('sua compra será parcelada em {}X de R$ {:.2f} com juros '.format(totpar, parcela))
else:
    total = preço
    print('opção invalida de pagamento. tente novamente ')
print('sua compra de R$ {:.2f} custará R$ {:.2f} no final. '.format(preço, total))

