primeiro = int(input('primeiro termo: '))
razão = int(input('Razão: '))
decimo = primeiro + (10 - 1) * razão
for c in range(primeiro, decimo + razão, razão):
    print('{} '.format(c), end='-> ')
print('Acabou')
