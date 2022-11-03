#calcular o salário e os descontos
v = float(input('Digite o valor que você ganha por hora: R$ '))
h = float(input('Digite o número de horas trabalhadas no mês: '))
s = v * h
ir = s * 11 / 100
i = s * 8 / 100
si = s * 5 / 100
sl = s - ir - i - si
input('Dado o valor que você ganha por hora R${:.2f} e o tempo trabalhado no mês {:.2f} horas, o seu salário mensal bruto será {:.2f} reais'.format(v, h, s))
input('Com o desconto do imposto de renda de R${:.2f}, o desconto do INSS de R${:.2f} e o desconto do sindicato de R${:.2f}'.format(ir, i, si))
input('Teremos o valor do salário liquido de R${:.2f}'.format(sl))