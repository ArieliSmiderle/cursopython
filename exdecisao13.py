v = float(input('Digite o valor que você ganha por hora trabalhada: R$ '))
h = float(input('Digite a quantidade de horas trabalhadas no mês: '))
s = v * h
ir1 = s * 5 / 100
ir2 = s * 10 / 100
ir3 = s * 20 / 100
inss = s * 10 / 100
fgts = s * 11 / 100
td = inss
td1 = ir1 + inss
td2 = ir2 + inss
td3 = ir3 + inss
sl = s - inss
sl1 = s - td1
sl2 = s - td2
sl3 = s - td3
if s <= 900:
    print('O salário bruto é R${:.2f}, o desconto do IR está isento, o desconto do inss é R${:.2f}, o fgts pago pela empresa é R${:.2f}, o total de descontos é R${:.2f} e seu salário liquido é R${:.2f}'.format(s, inss, fgts, td, sl))
elif s >= 900 and s <= 1500:
    print('O salário bruto é R${:.2f}, o desconto do IR é R${:.2f}, o desconto do inss é R${:.2f}, o fgts pago pela empresa é R${:.2f}, o total de descontos é R${:.2f} e seu salário liquido é R${:.2f}'.format(s, ir1, inss, fgts, td1, sl1))
elif s >= 1500 and s <= 2500:
    print('O salário bruto é R${:.2f}, o desconto do IR é R${:.2f}, o desconto do inss é R${:.2f}, o fgts pago pela empresa é R${:.2f}, o total de descontos é R${:.2f} e seu salário liquido é R${:.2f}'.format(s, ir2, inss, fgts, td2, sl2))
elif s > 2500:
    print('O salário bruto é R${:.2f}, o desconto do IR é R${:.2f}, o desconto do inss é R${:.2f}, o fgts pago pela empresa é R${:.2f}, o total de descontos é R${:.2f} e seu salário liquido é R${:.2f}'.format(s, ir3, inss, fgts, td3, sl3))
