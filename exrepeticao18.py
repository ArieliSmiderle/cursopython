#calcular a média ente as idades
i1 = int(input('Digite a primeira idade: '))
i2 = int(input('Digite a segunda idade: '))
i3 = int(input('Digite a terceira idade: '))
i4 = int(input('Digite a quarta idade: '))
i5 = int(input('Digite a quinta idade: '))
me = (i1 + i2 + i3 + i4 + i5) / 5
if me <= 25:
    print('Com a média {} o grupo de pessoas é jovem'.format(me))
elif me > 25 and me < 61:
    print('Com a média {} o grupo de pessoas é adulto'.format(me))
else:
    print('Com a média {} o grupo de pessoas é idoso'.format(me))