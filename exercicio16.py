#calcular o valor de um carro com 20% de desconto a vista e 10% de juros a prazo
carro = (input('Digite o modelo do carro que você deseja comprar: '))
valor = float(input('Digite o valor do carro {}: R$ '.format(carro)))
desconto = valor - (valor * 5 / 100)
juros = valor + (valor * 10 / 100)
parcelas = (input('Digite em até quantas vezes deseja parcelar: '))
input('O carro {} irá custar {:.2f}, se pago a vista sairá por {:.2f} e caso seja parcelado em até {} vezes, sairá por {:.2f}'.format(carro, valor, desconto, parcelas, juros))