#com o valor ganho por hora e as horas trabalhdas ao mês, calcular o salário mensal
v = float(input('Digite o valor que você ganha por hora: R$ '))
h = float(input('Digite o número de horas trabalhadas no mês: '))
s = v * h
input('Dado o valor que você ganha por hora R${} e o tempo trabalhado no mês {} horas, o seu salário mensal será {} reais'.format(v, h, s))