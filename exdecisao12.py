#reajuste de salário
s = float(input('Digite o valor do seu salário: R$ '))
s1 = s + (s * 20 / 100)
v1 = s1 - s
s2 = s + (s * 15 / 100)
v2 = s2 - s
s3 = s + (s * 10 / 100)
v3 = s3 - s
s4 = s + (s * 5 / 100)
v4 = s4 - s
if s <= 280:
    print('O salário era R${:.2f}, com um aumento de 20% que totaliza R${:.2f}, o salário passou a ser R${:.2f}'.format(s, v1, s1))
elif s >= 280 and s <= 700:
    print('O salário era R${:.2f}, com um aumento de 15% que totaliza R${:.2f}, o salário passou a ser R${:.2f}'.format(s, v2, s2))
elif s >= 700 and s <= 1500:
    print('O salário era R${:.2f}, com um aumento de 10% que totaliza R${:.2f}, o salário passou a ser R${:.2f}'.format(s, v3, s3))
elif s >= 1500:
    print('O salário era R${:.2f}, com um aumento de 5% que totaliza R${:.2f}, o salário passou a ser R${:.2f}'.format(s, v4, s4))
    