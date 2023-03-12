# Escreva um programa que converta uma temperatura digitada em ºC
# para ºF e K.
celsius = float(input('Informe a temperatura em ºC: '))
fahrenheit = celsius * 1.8 + 32
kelvin = celsius + 273
print('A temperatura de {:.2f}ºC equivale a {:.2f}ºF e {:.2f}K !'.format(celsius, fahrenheit, kelvin))
