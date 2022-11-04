n1 = float(input('Digite o primeiro número: '))
n2 = float(input('Digite o segundo número: '))
op = input('Digite a operação que você deseja realizar (+, -, *, /): ')
if op == '+':
    resultado = n1 + n2
elif op == '-':
    resultado = n1 - n2
elif op == '*':
    resultado = n1 * n2
elif op == '/':
    resultado = n1 / n2
print('O resultado é {}'.format(resultado))
if (resultado % 2) == 0:
    print('O número {} é par'.format(resultado))
else:
    print('O número {} é impar'.format(resultado))
if (resultado % 1) == 0:
    print('é inteiro')
else:
    print('é decimal')
if resultado >= 0:
    print('E é positivo')
else:
    print('E é negativo')