p1 = str(input('Digite o nome do primeiro produto: '))
v1 = float(input('Digite o valor do primeiro produto:R$ '))
p2 = str(input('Digite o nome do segundo produto: '))
v2 = float(input('Digite o valor do segundo produto:R$ '))
p3 = str(input('Digite o nome do terceiro produto: '))
v3 = float(input('Digite o valor do terceiro produto:R$ '))
if v1 < v2 and v1 < v3:
    print('O produto que deve ser comprado é {} que custa R${}'.format(p1, v1))
elif v2 < v1 and v2 < v3:
    print('O produto que deve ser comprado é {} que custa R${}'.format(p2, v2))
elif v3 < v1 and v3 < v2:
    print('O produto que deve ser comprado é {} que custa R${}'.format(p3, v3))