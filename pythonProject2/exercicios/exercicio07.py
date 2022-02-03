peso = float(input('Qual é o seu peso (KG) ? '))
altura = float(input('Qual e sua altura (M) ? '))
imc = peso / (altura ** 2)
print('O IMC dessa pessoa é de {:.2f} '.format(imc))
if imc < 18.5:
    print('você está abaixo do peso normal')
elif imc > 18.5 and imc <= 25:
    print('Você está no peso odeal ')
elif imc > 25 and imc <= 30:
    print('Você está com sobrepeso ')
elif imc > 30 and imc <= 40:
    print('Você está em em quadro de obesidade ')
else:
    print('Você está em um quadro de obesidade morbida ')
