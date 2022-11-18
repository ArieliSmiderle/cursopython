n = int(input('Digite um número para calcular seu fatorial: '))
c = n
f = 1
print('O fatorial de {}! é igual: '.format(n), end='')
while c > 0:
    print('{}'.format(c), end='')
    print(' * ' if c > 1 else ' = ', end='')
    f *= c
    c -= 1
print('{}'.format(f))