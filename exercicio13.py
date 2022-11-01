#calcular area de uma parede e calcular a quantidade de tinta para pintar
largura = float(input('Digite a largura da parede: '))
altura = float(input('Digite a altura da parede: '))
cor = (input('Digite a cor desejada para pintar a parede: '))
área = largura * altura
print('Vemos que com a largura da parede {} e sua altura {}, temos uma área de {}m2'.format(largura, altura, área))
tinta = área / 2
print('Para pintar uma parede de {}m2, iremos precisar de {}l de tinta da cor {}'.format(área, tinta, cor))
