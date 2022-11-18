#calcular o fatorial de um número e repetir
n = int(input('Digite um número: '))
resultado = 1
count = 1
if (n < 0) or (n >= 16):
    print('Digite um número inteiro, positivo e menor que 16: ')
while count <= n:
    resultado *= count
    count += 1
print('o fatorial de {} é = {}'.format(n, resultado))