from math import inf

maior = -inf
menor = inf
gordo = -inf
magro = inf
soma = 0
contador = 0
while True:
    cliente = float(input("Digite seu código: "))
    if cliente <= 0:
        break
    altura = float(input('Digite sua altura: '))
    peso = float(input('Digite seu peso: '))

    contador += 1
    soma += altura
    if altura < menor:
        menor = altura
    if altura > maior:
        maior = altura
        soma += peso
        if peso < gordo:
            gordo = peso
        if peso > magro:
            magro = peso

print(f"A menor altura foi {menor}C")
print(f"A maior altura foi {maior}C")
print(f"O maior peso é {gordo}C")
print(f"O menor peso é {magro}C")