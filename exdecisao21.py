#a 1,90 / 20 3 %, acima 20 5% / g 2,50/ 20 4%, acima 20 6%
c = input('Digite o combustível escolhido (a)alcool ou (g)gasolina: ')
litros = float(input('Digite a quantidade a ser abastecida em litros: '))
if c == 'g':
    gasolina = litros * 2.50
if litros < 20:
    desconto = gasolina * 3 / 100
    total = gasolina - desconto
    print('O valor do desconto será R${:.2f} e o valor a ser pago será R${:.2f}'.format(desconto, total))
else:
    gasolina = litros * 2.50
    desconto = gasolina * 5 / 100
    total = (litros * 2.50) - desconto
    print('O valor do desconto é R${:.2f} e o valor a ser pago será R${:.2f}'.format(desconto, total))
if c == 'a':
    al = litros * 1.90
if litros < 20:
    desconto = al * 4 / 100
    total = al - desconto
    print('O valor do desconto é R${:.2f} e o valor a ser pago é R$ {:.2f}'.format(desconto, total))
else:
    al = litros * 1.90
    desconto = al * 6 / 100
    total = al - desconto
    print('O valor do desconto é R${:.2f} e o valor a ser pago é R${:.2f}'.format(desconto, total))
