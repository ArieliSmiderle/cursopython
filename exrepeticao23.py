print('Panificadora Pão de Ontem - Tabela de preços')
valor = float(input('Digite o valor do pão: R$ '))
n = 0
for n in range(1, 51):
    resultado = n * valor
    print(f'{n} - R$ {resultado:1.2f}')