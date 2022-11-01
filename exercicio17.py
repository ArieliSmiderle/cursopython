#solicitar a temperatura em graus Fahrenheit e transformar em graus Celsius
f = float(input('Informe a temperatura em °F: '))
c = (f - 32) * 5/9
input('A temperatura de {:.2f}°F equivale a {:.2f}°C'.format(f, c))