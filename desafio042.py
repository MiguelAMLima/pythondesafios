# Refaça o desafio035 dos triângulos, acrescentando o recurso de mostrar que
# tipo de triângulo será formado: -Equilátero: todos os lados iguais;
# -Isósceles: dois lados iguais; -Escaleno: todos os lados diferentes.
print('\n')
print('-=' * 12)
print('Analisador de Triângulos')
print('-=' * 12)
print('\n')
reta1 = float(input('Informe o comprimento da primeira reta em metros: '))
reta2 = float(input('Informe o comprimento da segunda reta em metros: '))
reta3 = float(input('Informe o comprimento da terceira reta em metros: '))
if (reta1 + reta2) > reta3 and (reta1 + reta3) > reta2 and (reta2 + reta3) > reta1:
    print('\nAs três retas podem formar um triângulo ', end='')
    if reta1 == reta2 == reta3:
        print('equilátero.')
    elif reta1 == reta2 or reta1 == reta3 or reta2 == reta3:
        print('isósceles.')
    else:
        print('escaleno.')
else:
    print('\nAs três retas NÃO podem formar um triângulo!')
