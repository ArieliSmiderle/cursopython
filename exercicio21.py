#criar um algorítmo que calcula o peso ideal dado a fórmula (72.7 * altura) - 58
altura = float(input('Digite a sua altura: '))
peso = (72.7 * altura) - 58
input('O seu peso ideal considerando sua altura que é {:.2f}, seria {:.2f}kg'.format(altura, peso))
