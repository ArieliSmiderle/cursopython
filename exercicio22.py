#calcular a quantidade excedente de peso e cobrar multa de 4 reais ao kg
q = float(input('Digite a quantidade pescada de peixes: '))
e = q - 50
m = e * 4
input('A quantidade excedente foi {}, e o valor da multa a ser paga será R${}'.format(e, m))
