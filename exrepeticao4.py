paisA = 80000
paisB = 200000
ano = 0
while paisA < paisB:
    paisA += paisA * 3 /100
    paisB += paisB * 1.5 / 100
    ano += 1
print ('O pais A ultrapassa ou iguala B em {} anos'.format(ano))