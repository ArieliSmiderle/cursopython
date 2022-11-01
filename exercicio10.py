#ver o valor de um produto e acrescentar 10% de desconto
preço = float(input('Digite o valor de um produto: R$ '))
d = preço - (preço * 10 / 100)
economia = preço - d
print('O valor do produto é R${:.2f}, e seu valor com desconto é R${:.2f} então você economizou R${:.2f}'.format(preço, d, economia))

