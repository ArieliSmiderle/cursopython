paisA = float(input('Digite o número da primeira população: '))
paisB = float(input('Digite o número da segunda população: '))
ano = 0
while paisA < paisB:
    paisA += paisA * 3 / 100
    paisB += paisB * 1.5 / 100
    ano += 1
print('O pais A ultrapassa ou iguala B em {} anos'.format(ano))