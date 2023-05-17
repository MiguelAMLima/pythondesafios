# Melhore o jogo do desafio028 onde o computador vai "pensar" em um número
# entre 0 e 10. Só que agora o jogador vai tentar adivinhar até acertar,
# mostrando no final quantos palpites foram necessários para vencer.
from random import randint
from time import sleep
computador = randint(0, 10)
print('-=-' * 20)
print('Vou pensar em um número entre 0 e 10. Tente adivinhar...')
print('-=-' * 20)
jogador = 11
c = 0
while jogador != computador:
    jogador = int(input('Em qual número pensei? '))
    c += 1
    print('PROCESSANDO...')
    sleep(1)
    if jogador > computador:
        print(f'O número que pensei foi menor que {jogador}, tente novamente!')
    elif jogador < computador:
        print(f'O número que pensei foi maior que {jogador}, tente novamente!')
print(f'Parabéns! você acertou! o número que pensei foi {computador}.\nVocê precisou de {c} tentativas.')
