condition = True

soma=0
numero=[]

while condition:
    num=int(input('Digite o numero: '))
    if num < 0 or num > 1000:
        print ('Digite um número entre 0 e 1000: ')
    elif num != 0:
        soma += num
        numero.append(num)
    else:
        break

print('Soma: ', soma)
print('Menor Valor: ', min(numero))
print('Maior Valor: ', max(numero))