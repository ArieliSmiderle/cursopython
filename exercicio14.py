#calcular a área de um quadrado e mostrar o dobro
l = float(input('Digite a largura do quadrado: '))
a = float(input('Digite a altura do quadrado: '))
área = l * a
a2 = área * 2
input('Se a Largura do quadrado é {} e sua altura é {}, então sua área é {}m2'.format(l, a, área))
input('Se a área deste quadrado é {}m2, então o dobro da área é {}m2'.format(área, a2))
