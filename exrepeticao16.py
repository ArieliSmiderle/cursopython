num = int(input('Digite um número: '))
mult=0
for count in range(2, num):
    if(num % count == 0):
        mult += 1
if (mult == 0):
    print('O número {} é um número primo'.format(num))
else:
    print('O número {} não é um número primo'.format(num))
