#converter um valor em real para um valor em dólar
real = float(input('Digite o valor que você quer converter: R$'))
dolar = real / 5.11
print('Com R${:.2f} você terá US${:.2f}'.format(real, dolar))
