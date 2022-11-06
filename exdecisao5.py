n1 = float(input('Digite a primeira nota do aluno: '))
n2 = float(input('Digite a segunda nota do aluno: '))
m = (n1 + n2) / 2
if m == 10:
    print('Aprovado com distinção')
elif m >= 7:
    print('Aprovado')
else:
    print('Reprovado')
