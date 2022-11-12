n = int(input('Digite o termo que deseja encontrar: '))
u = 1
p = 1
if (n == 1) or (n == 2):
    print ('1')
else:
    count = 3
    while count <= n:
        termo = u + p
        p = u
        u = termo
        count += 1
        print (termo)

