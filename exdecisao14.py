#somar duas notas, calcular sua média e retornar com conceito e decisão
n1 = float(input('Digite a primeira nota: '))
n2 = float(input('Digite a segunda nota: '))
m = (n1 + n2) / 2
if m >= 9:
    print('As notas do aluno foram {} e {}, totalizando a média {}, então seu conceito foi A e o aluno está aprovado'.format(n1, n2, m))
elif m <= 8.9 and m >= 7.5:
    print('As notas do aluno foram {} e {}, totalizando a média {}, então seu conceito foi B e o aluno está aprovado'.format(n1, n2, m))
elif m <= 7.4 and m >= 6:
    print('As notas do aluno foram {} e {}, totalizando a média {}, então seu conceito foi C e o aluno está aprovado'.format(n1, n2, m))
elif m <= 5.9 and m >= 4:
    print('As notas do aluno foram {} e {}, totalizando a média {}, então seu conceito foi D e o aluno está reprovado'.format(n1, n2, m))
elif m <= 3.9:
    print('As notas do aluno foram {} e {}, totalizando a média {}, então seu conceito foi E e o aluno está reprovado'.format(n1, n2, m))
    