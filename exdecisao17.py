valor = int(input('Digite um valor para retirar: '))
cem = int(valor / 100)
valor = valor - (cem * 100)
cinquenta = int(valor / 50)
valor = valor - (cinquenta * 50)
dez = int(valor / 10)
valor = valor - (dez * 10)
cinco = int(valor / 5)
valor = valor - (cinco * 5)
um = valor
print('Notas R$ 100,00 = {}'.format(cem))
print('Notas R$ 50,00 = {}'.format(cinquenta))
print('Notas R$ 10,00 = {}'.format(dez))
print('Notas R$ 5,00 = {}'.format(cinco))
print('Notas R$ 1,00 = {}'.format(um))