# Crie uma tupla preenchida com os 20 primeiros colocados da
# tabela do Campeonato Brasileiro de Futebol, na ordem de
# colocação. Depois mostre: A) Apenas os 5 primeiros colocados;
# B) Os últimos 4 colocados da tabela; C) Uma lista com os times
# em ordem alfabética; D) Em que posição na tabela está o time do
# São Paulo.
CBF = ('Botafogo', 'Palmeiras', 'Grêmio', 'Bragantino', 'Fluminense',
       'Athletico-PR', 'Flamengo', 'Fortaleza', 'Atlético-MG', 'Corinthians',
       'Cuiabá', 'Cruzeiro', 'Internacional', 'São Paulo', 'Vasco da Gama',
       'Goiás', 'Bahia', 'Santos', 'América-MG', 'Coritiba')
print('\n', end='')
print('-=' * 6, 'Campeonato Brasileiro de Futebol', '=-' * 6)
print(f"\n{'Primeiros 5 colocados:':^58}")
for cont in range(0, 5):
    print(f'{cont + 1}º -> {CBF[cont]}')
print(f"\n{'Últimos 4 colocados:':^58}")
for cont in range(16, 20):
    print(f'{cont + 1}º -> {CBF[cont]}')
print(f"\n{'Times em ordem alfabética:':^58}")
alfa = sorted(CBF)
for time in alfa:
    print(time)
print(f"\nO time do São Paulo está na {CBF.index('São Paulo') + 1}ª posição.")
