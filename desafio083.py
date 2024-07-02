# Crie um programa onde o usuário digite uma expressão matemática qualquer
# que use parênteses. Seu aplicativo deverá analisar se a expressão passada
# está com os parênteses abertos e fechados na ordem correta.
expmat = str(input('Digite a expressão matemática: '))
pilha = []
for simb in expmat:
    if simb == '(':
        pilha.append('(')
    elif simb == ')':
        if len(pilha) > 0:
            pilha.pop()
        else:
            pilha.append(')')
            break
if len(pilha) == 0:
    print('Sua expressão está válida!')
else:
    print('Sua expressão está errada!')
