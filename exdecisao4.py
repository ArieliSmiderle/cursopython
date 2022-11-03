letra = input('Digite uma letra: ')
if letra in ('a', 'e' , 'i', 'o', 'u'):
    print('A letra digitada é uma vogal')
elif letra in ('b', 'c', 'd', 'f', 'g', 'h', 'j', 'k', 'l', 'm', 'n', 'p', 'q', 'r', 's', 't', 'v', 'w', 'x', 'y', 'z'):
    print('A letra digitada é uma consoante')
else:
    print('O símbolo digitado não é uma letra')