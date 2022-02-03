num = int(input('digite um numero inteiro: '))
print('''escolha umas das bases para conversão:
 [ 1 ] converter para BINARIO
 [ 2 ] converter para OCTAL
 [ 3 ] converter para EXADECIMAL ''')
opcao = int(input('sua opção: '))
if opcao == 1:
    print('{} convertido para binario é igual a {} '.format(num, bin(num)[2:]))
elif opcao == 2:
    print('{} convertido para OCTAL e igaul a {} '.format(num, oct(num[2:])))
elif opcao == 3:
    print('{} convertido para EXADECIMAL é igaul a {} '.format(num, hex(num)[2:]))
else:
    print('opção invalida. tente novamente!')