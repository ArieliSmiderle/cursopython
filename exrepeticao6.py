n1 = float(input('Digite o primeiro número: '))
n2 = float(input('Digete o segundo número: '))
n3 = float(input('Digite o terceiro número: '))
n4 = float(input('Digite o quarto número: '))
n5 = float(input('Digite o quinto número: '))
if n1 > n2 and n1 > n3 and n1 > n4 and n1 > n5:
    print('O maior número é o número {}'.format(n1))
elif n2 > n1 and n2 > n3 and n2 > n4 and n2 > n5:
    print('O maior número é o número {}'.format(n2))
elif n3 > 1 and n3 > n2 and n3 > n4 and n3 > n5:
    print('O maior número é o número {}'.format(n3))
elif n4 > n1 and n4 > n2 and n4 > n3 and n4 > n5:
    print('O maior número é o número {}'.format(n4))
elif n5 > n1 and n5 > n2 and n5 > n3 and n5 > n4:
    print('O maior número é o número {}'.format(n5))