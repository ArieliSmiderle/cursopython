turno = str(input('Digite o turno que você estuda (m)matutino, (v)vespertino, (n)noturno: '))
nome = str(input('Digite seu nome: '))
if turno == 'm':
    print('Bom dia, {}, tenha uma ótima aula!'.format(nome))
elif turno == 'v':
    print('Boa tarde, {}, tenha uma ótima aula!'.format(nome))
elif turno == 'n':
    print('Boa noite, {}, tenha uma ótima aula!'.format(nome))