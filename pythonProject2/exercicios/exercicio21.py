sexo = str(input(' Imforme seu sexo: [M/F] ')). strip().upper()[0]
while sexo not in 'MmFf':
    sexo = str(input('Dados invalidos. por favor Digite deu sexo: ')).strip().upper()[0]
print('Sexo {} registrado com sucesso. '.format(sexo))
