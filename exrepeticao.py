numero = float(input('Digite um número de 0 a 10: '))
while numero < 0 or numero > 10:
    numero = float(input('Digite um número de 0 a 10: '))
    print('O número digitado foi o número {}'.format(numero))
