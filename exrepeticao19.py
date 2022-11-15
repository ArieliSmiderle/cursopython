candidato1 = 0
candidato2 = 0
candidato3 = 0
numero_eleitores = int(input("Digite o número de eleitores: "))
for i in range(0,numero_eleitores):
    voto = input("Escolha entre o candidato1, candidato2, candidato3")
if voto == "candidato1":
    candidato1 = candidato1 + 1
elif voto == "candidato2":
    candidato2 = candidato2 + 1
elif voto == "candidato3":
    candidato3 = candidato3 + 1
else:
    print("voto nulo.")
print("numero de votos do candidato 1:", candidato1)
print("numero de votos do candidato 2:", candidato2)
print("numero de votos do candidato 3:", candidato3)
