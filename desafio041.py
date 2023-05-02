# A Confederação Nacional de Natação precisa de um programa que leia o ano
# de nascimento de um atleta e mostre sua categoria, de acordo com a idade:
# -Até 9 anos: mirim; -Até 14 anos: infantil; -Até 19 anos: júnior;
# -Até 25 anos: sênior; -Acima: master.
from datetime import date
nascimento = int(input('Digite o ano de nascimento do atleta: '))
idade = date.today().year - nascimento
if 0 < idade <= 9:
    print('Idade do atleta: {}\nCategoria do atleta: mirim'.format(idade))
elif 9 < idade <= 14:
    print('Idade do atleta: {}\nCategoria do atleta: infantil'.format(idade))
elif 14 < idade <= 19:
    print('Idade do atleta: {}\nCategoria do atleta: júnior'.format(idade))
elif 19 < idade <= 25:
    print('Idade do atleta: {}\nCategoria do atleta: sênior'.format(idade))
elif idade > 25:
    print('Idade do atleta: {}\nCategoria do atleta: master'.format(idade))
else:
    print('Não foi possível verificar a idade do atleta, digite o ano de nascimento corretamente.')
