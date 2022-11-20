from math import inf

maior = -inf
menor = inf
soma = 0
contador = 0
while True:
    temperatura = float(input("Digite a temperatura em graus: "))
    if temperatura <= 0:
        break

    contador += 1
    soma += temperatura
    if temperatura < menor:
        menor = temperatura
    if temperatura > maior:
        maior = temperatura
        media = soma / contador

print(f"A menor temperatura foi {menor}C")
print(f"A maior temperatura foi {maior}C")
print(f"A média das temperaturas foi {media}C")