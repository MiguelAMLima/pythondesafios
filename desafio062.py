# Melhore o desafio061, perguntando para o usuário se ele quer mostrar mais
# alguns termos. O programa encerra quando ele disser que quer mostrar 0 termos.
print('-=' * 10, end='-\n')
print(f'{"Gerador de P.A.":^21}')
print('-=' * 10, end='-\n')
primeiro = int(input('\nInforme o primeiro termo: '))
razao = int(input('Informe a razão da P.A.: '))
termo = primeiro
cont = 1
mais = 10
total = 0
print('')
while mais != 0:
    total += mais
    while cont <= total:
        print(f'{termo}', end=' ➟ ')
        termo += razao
        cont += 1
    print('PAUSA')
    mais = int(input('Quantos termos a mais você quer mostrar? '))
print(f'\nProgressão finalizada com {total} termos mostrados.')
