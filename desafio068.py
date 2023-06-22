# Faça um programa que jogue par ou ímpar com o jogador. O jogo só será
# interrompido quando o jogador PERDER, mostrando o total de vitórias
# consecutivas que ele conquistou no final do jogo.
from random import randint
cont = 0
print('-' * 30)
print('Vamos jogar PAR ou ÍMPAR!')
print('-' * 30)
while True:
    tipo = int(input('[0 = PAR / 1 = ÍMPAR] Digite a sua escolha: '))
    jogador = int(input('Escolha um número de 0 a 10: '))
    computador = randint(0, 10)
    soma = jogador + computador
    print(f'Meu número foi: {computador}')
    print('-' * 30)
    if soma % 2 == 0:
        if tipo == 0:
            print(f'Você escolheu PAR e o valor foi {soma}. Parabéns, você ganhou! vamos de novo!')
            cont += 1
        else:
            print(f'Você escolheu ÍMPAR e o valor foi {soma}. EU GANHEI!')
            break
    else:
        if tipo == 0:
            print(f'Você escolheu PAR e o valor foi {soma}. EU GANHEI!')
            break
        else:
            print(f'Você escolheu ÍMPAR e o valor foi {soma}. Parabéns, você ganhou! vamos de novo!')
            cont += 1
print(f'\nVocê venceu {cont} vezes seguidas!')
