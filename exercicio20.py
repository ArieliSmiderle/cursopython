#produto, soma e elevado ao cubo
n1 = int(input('Digite o primeiro número inteiro: '))
n2 = int(input('Digite o segundo número inteiro: '))
n3 = float(input('Digite um número real: '))
p = (n1 * 2) * (n2 / 2)
s = (n1 * 3) + n3
c = n3 ** 3
print(input('O resultado do produto do dobro do primeiro com metade do segundo é {:.2f}'.format(p)))
print(input('O resultado da soma do triplo do primeiro com o terceiro é {:.2f}'.format(s)))
print(input('O resultado do terceiro número elevado ao cubo é {:.2f}'.format(c)))