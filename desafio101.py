# Crie um programa que tenha uma função chamada
# voto() que vai receber como parâmetro o ano de
# nascimento de uma pessoa, retornando um valor
# literal indicando se a pessoa tem voto negado,
# opcional ou obrigatório nas eleições.
def voto(ano):
    from datetime import date
    atual = date.today().year
    idade = atual - ano
    if idade < 16:
        return f'Idade: {idade} anos\nSituação: NÃO VOTA.'
    elif 16 <= idade < 18 or idade > 65:
        return f'Idade: {idade} anos\nSituação: VOTO OPCIONAL.'
    else:
        return f'Idade: {idade} anos\nSituação: VOTO OBRIGATÓRIO.'


nasc = int(input('Em que ano você nasceu? '))
print('-' * 30)
print(voto(nasc))
