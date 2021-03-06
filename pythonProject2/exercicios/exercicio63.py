def leiaint(msg):
    while True:
        try:
            n = int(input(msg))
        except (ValueError, TypeError):
            print('\033[31mERRO: Por favor, digite um numero inteiro valido.\033[m ')
            continue
        except (KeyboardInterrupt):
            print('\033[31mUsuario preferiu nao digitar esse numero.\033[m ')
            return 0
        else:
            return n

def leiafloat(msg):
    while True:
        try:
            n = float(input(msg))
        except (ValueError, TypeError):
            print('\033[31mERRO: Por favor, digite um numero inteiro valido.\033[m ')
            continue
        except (KeyboardInterrupt):
            print('\033[31mUsuario preferiu nao digitar um valor valido.\033[m ')
            return 0
        else:
            return n


n1 = leiaint('digite um numero inteiro: ')
n2 = leiafloat('Digite um numero real ')
print(f'O valor inteiro digitado foi {n1} e o real foi {n2}')

