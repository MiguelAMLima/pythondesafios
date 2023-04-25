# Faça um programa que leia o ano de nascimento de um jovem e informe,
# de acordo com sua idade: -Se ele ainda vai se alistar ao serviço militar; -Se é a hora
# de se alistar; -Se já passou do tempo de alistamento. Seu programa também
# deverá mostrar o tempo que falta ou que passou do prazo.
from datetime import date
nascimento = int(input('Digite o ano de nascimento do avaliado: '))
idade = date.today().year - nascimento
if idade == 18:
    print('Você precisa se alistar imediatamente!')
elif idade < 18:
    print('Você precisará se alistar daqui a {} ano(s).'.format(18 - idade))
    print('Seu alistamento será em {}'.format(nascimento + 18))
else:
    print('Você já deveria ter se alistado há {} ano(s).'.format(idade - 18))
    print('Seu alistamento deveria ter sido em {}'.format(nascimento + 18))
