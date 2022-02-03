print('Gerador de PA')
print('=-=' * 15)
primeiro = int(input('Primeiro termo: '))
razao = int(input('Razão da PA: '))
termo = primeiro
cont = 1
tot = 0
mais = 10
while mais != 0:
    tot += mais
    while cont <= tot:
        print('{} -> '.format(termo), end='')
        termo = termo + razao #+=
        cont += 1
    print('Pausa')
    mais = int(input('Quantos termos você quer mostrar a mais? '))
print('Progressão finalizado com {} termos. '.format(tot))

