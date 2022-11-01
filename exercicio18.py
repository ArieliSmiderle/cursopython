#calcular valor do aluguel de carros, levando em consideração o valor de R$60 ao dia e R$0.15 por km rodado
carro = (input('Digite o nome do carro utilizado: '))
dias = int(input('Quantos dias o carro permaneceu com você? '))
km = float(input('Quantos km foram rodados? '))
valor = (dias * 60) + (km * 0.15)
print('O valor a ser pago pelo carro {}, dado os {} dias e os {} km rodados será de R${}'.format(carro, dias, km, valor))