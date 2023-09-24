# Crie um programa que tenha uma tupla totalmente preenchida
# com uma contagem por extenso, de zero até vinte. Seu programa
# deverá ler um número pelo teclado (entre 0 e 20) e mostrá-lo por
# extenso.
extenso = ('zero', 'um', 'dois', 'três', 'quatro', 'cinco', 'seis', 'sete',
           'oito', 'nove', 'dez', 'onze', 'doze', 'treze', 'quatorze', 'quinze',
           'dezesseis', 'dezessete', 'dezoito', 'dezenove', 'vinte')
repetir = 'S'
while repetir == 'S':
    while True:
        num = int(input('Digite um número entre 0 e 20 para visualizá-lo por extenso: '))
        if 0 <= num <= 20:
            break
        print('Tente novamente. ', end='')
    print(f'O número {num} por extenso é: {extenso[num]}')
    repetir = input('Deseja ver outro número? [S/N] ').upper()[0]
print('-=' * 16)
print('Programa encerrado.')
