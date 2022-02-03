frase = str(input('Digite uma frase: ')).strip().upper()
palavras = frase.split()
junto = ''.join(palavras)
inverso = ''
for letra in range(len(junto) - 1, -1, -1):
    inverso += junto[letra]
print('o inverso de {} é {} '.format(junto, inverso))
if inverso == junto:
    print('temos um palindromo! ')
else:
    print('a frase nao é um palindromo')
print('-=' * 15)
print('outro modo: ')
inverso = junto[::-1]
print('o inverso de {} é {} '.format(junto, inverso))
