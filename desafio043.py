# Desenvolva uma lógica que leia o peso e a altura de uma pessoa, calcule
# seu IMC e mostre seu status, de acordo com a tabela abaixo: -Abaixo de
# 18.5: abaixo do peso; -Entre 18.5 e 25: peso ideal; -25 até 30: sobrepeso;
# -30 até 40: obesidade; -Acima de 40: obesidade mórbida.
peso = float(input('Informe o peso do avaliado (Kg): '))
altura = float(input('Informe a altura do avaliado (m): '))
IMC = peso / (altura ** 2)
print('IMC: {:.1f}\nStatus do avaliado: '.format(IMC), end='')
if IMC < 18.5:
    print('abaixo do peso.')
elif IMC < 25:
    print('peso ideal!')
elif IMC < 30:
    print('sobrepeso.')
elif IMC < 40:
    print('obesidade.')
else:
    print('obesidade mórbida.')
