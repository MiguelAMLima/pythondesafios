# Escreva um programa que leia a velocidade de um carro. Se ele ultrapassar
# 80Km/h, mostre uma mensagem dizendo que ele foi multado. A multa vai custar
# R$7,00 por cada Km acima do limite.
velocidade = float(input('Qual foi a velocidade do carro em Km/h? '))
if velocidade >= 81:
    multa = int((velocidade - 80)) * 7
    print('Você ultrapassou a velocidade permitida em {:.1f}Km, sua multa é de R${},00'
          .format((velocidade - 80), multa))
else:
    print('Você está dentro da velocidade permitida!')
