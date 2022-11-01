#calcular um reajuste salarial de 20%
salário = float(input('Digite o valor do salário do funcionario : R$ '))
aumento = salário * 20 / 100
reajuste = salário + aumento
input('O salário do funcionário é R${:.2f} e com o aumento de 20% que será de R${:.2f}, passará a ser R${:.2f}'.format(salário, aumento, reajuste))

