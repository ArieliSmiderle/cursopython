#ler número e dizer dia da semana específico
dia = int(input('Digite um dia da semana: '))
if dia == 1:
    print('O dia digitado {} corresponde ao domingo'.format(dia))
elif dia == 2:
    print('O dia digitado {} corresponde a segunda-feira'.format(dia))
elif dia == 3:
    print('O dia digitado {} corresponde a terça-feira'.format(dia))
elif dia == 4:
    print('O dia digitado {} corresponde a quarta-feira'.format(dia))
elif dia == 5:
    print('O dia digitado {} corresponde a quinta-feira'.format(dia))
elif dia == 6:
    print('O dia digitado {} corresponde a sexta-feira'.format(dia))
elif dia == 7:
    print('O dia digitado {} corresponde a sábado'.format(dia))
else:
    print('O dia digitado não corresponde a um dia da semana')
