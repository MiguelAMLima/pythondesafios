# Faça um programa que tenha uma função chamada
# notas() que pode receber várias notas de alunos
# e vai retornar um dicionário com as seguintes
# informações: -Quantidade de notas, -A maior nota,
# -A menor nota, -A média da turma, -A situação
# (opcional). Adicione também as docstrings da função.
def notas(lista, sit):
    """
    -> Função para analisar notas e situações de vários alunos.
    :param lista: uma ou mais notas dos alunos.
    :param sit: indica se deve ou não adicionar a situação.
    :return: dicionário com várias informações sobre a situação da turma.
    """
    r = dict()
    r['Quantidade de notas'] = len(lista)
    r['Maior nota'] = max(lista)
    r['Menor nota'] = min(lista)
    r['Média da turma'] = round(sum(lista) / len(lista), 2)
    if sit:
        if r['Média da turma'] >= 7:
            r['Situação da turma'] = 'BOA'
        elif r['Média da turma'] >= 5:
            r['Situação da turma'] = 'RAZOÁVEL'
        else:
            r['Situação da turma'] = 'RUIM'
    return r


resp = list()
i = 1
while True:
    nota = float(input(f'Digite a {i}ª nota: [-1 encerra] '))
    if nota == -1.0:
        break
    resp.append(nota)
    i += 1
situacao = str(input('Deseja visualizar a situação da turma? [S/N]: ')).strip()[0]
if situacao in 'Ss':
    print(notas(resp, sit=True))
else:
    print(notas(resp, sit=False))
