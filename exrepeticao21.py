cds = int(input("Digite quantos cds você comprou: "))
a = 0
total = 0
for i in range(cds):
    valor = float(input('Digite qual o valor de cada cd: R$ '))
    total = total + valor
    media = total / cds
    a = a + 1
print(f"O valor médio gasto nos cds foi R$ {media}")