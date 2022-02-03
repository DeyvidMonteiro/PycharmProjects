from time import sleep
n1 = int(input('primeiro valor: '))
n2 = int(input('segundo valor: '))
opcao = 0
while opcao != 5:
    print('''    [ 1 ] somar
    [ 2 ] multiplicar
    [ 3 ] maior
    [ 4 ] novos numeros
    [ 5 ] sair do programa ''')
    opcao = int(input(' >>> qual a sua opção? '))
    if opcao == 1:
        soma = n1 + n2
        print(' a soma entre {} + {} é {}' .format(n1, n2, soma))
    elif opcao == 2:
        produto = n1 * n2
        print('o resultado de {} X {} é {} '.format(n1, n2, produto))
    elif opcao == 3:
        if n1 > n2:
            maior = n1
        else:
            maior = n2
        print('entre {} e {} o maior valor é {} '.format(n1, n2, maior))
    elif opcao == 4:
        print('informe os numeros novamente: ')
        n1 = int(input('primeiro valor: '))
        n2 = int(input('segundo valor: '))
    elif opcao == 5:
        print('finalizando..!')
    else:
        print('opção invalda. tente novamente! ')
print(('=-=' *15))
sleep(2)
print('fim do programa! ')