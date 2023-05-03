# Crie um programa que faça o computador jogar Jokenpô com você.
from random import randint
print('\nVamos jogar Jokenpô!!\n')
print('Escolha:\n[ 1 ] para pedra\n[ 2 ] para papel\n[ 3 ] para tesoura\n')
jogador = int(input('Sua escolha: '))
pc = randint(1, 3)
if jogador == 1:
    if pc == 1:
        print('Você escolheu PEDRA e eu escolhi PEDRA...\nTemos um empate!')
    elif pc == 2:
        print('Você escolheu PEDRA e eu escolhi PAPEL...\nEu venci!! :D')
    elif pc == 3:
        print('Você escolheu PEDRA e eu escolhi TESOURA...\nParabéns, você me venceu!!')
elif jogador == 2:
    if pc == 1:
        print('Você escolheu PAPEL e eu escolhi PEDRA...\nParabéns, você me venceu!!')
    elif pc == 2:
        print('Você escolheu PAPEL e eu escolhi PAPEL...\nTemos um empate!')
    elif pc == 3:
        print('Você escolheu PAPEL e eu escolhi TESOURA...\nEu venci!! :D')
elif jogador == 3:
    if pc == 1:
        print('Você escolheu TESOURA e eu escolhi PEDRA...\nEu venci!! :D')
    elif pc == 2:
        print('Você escolheu TESOURA e eu escolhi PAPEL...\nParabéns, você me venceu!!')
    elif pc == 3:
        print('Você escolheu TESOURA e eu escolhi TESOURA...\nTemos um empate!')
else:
    print('Você não escolheu nenhuma opção válida, tente novamente!')
