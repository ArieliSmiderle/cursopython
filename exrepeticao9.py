n1 = int(input('Digite o primeiro número: '))
n2 = int(input('Digite o segundo número: '))
while n1 > n2:
    n1 = int(input('Digite o primeiro número e ele tem que ser menor que o segundo: '))
    n2 = int(input('Digite o segundo número e ele tem que ser maior que o primeiro: '))
for i in range (n1, n2, 1):
    print (i)