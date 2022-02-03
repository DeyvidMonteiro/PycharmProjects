from math import factorial
n = int(input('Digite um numero para calcular seu fatorial: '))
f = factorial(n)
print('O fatorial de {} é  {} '.format(n, f))
print('=-=' * 15)
nn = int(input('Digite um numero para saber o seu fatorial: '))
print('calculando {}! = '.format(nn), end='')
c = nn
ff = 1
while c > 0:
    print('{} '.format(c), end='')
    print('x ' if c > 1 else '= ', end='')
    ff *= c
    c -= 1
print('{} '.format(ff))

