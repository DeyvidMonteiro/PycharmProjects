ficha = []
while True:
    nome = str(input('nome: '))
    nota1 = float(input('nota 1: '))
    nota2 = float(input('nota 2: '))
    media = (nota1 + nota2) / 2
    ficha.append([nome, [nota1, nota2], media])
    resp = str(input("que continuar? [S/N] "))
    if resp in 'Nn':
        break
print('-=' * 30)
print(f'{"N°.":<4}{"nome":<10}{"media":>8}')
print('-' * 26)
for i, a in enumerate(ficha):
    print(f'{i:<4}{a[0]:<10}{a[2]:8.1f}')
while True:
    print('=-' * 30)
    opc = int(input('mostrar notas de qual aluno? (999 interrompe) '))
    if opc == 999:
        print('finalizando')
        break
    if opc <= len(ficha) - 1:
        print(f'notas de {ficha[opc][0]} sao {ficha[opc][1]}')
print('<<<<< volte sempre >>>>>')

