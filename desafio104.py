# Crie um programa que tenha uma função leia_int(),
# que vai funcionar de forma semelhante à função
# input() do Python, só que fazendo a validação
# para aceitar apenas um valor numérico inteiro.
def leia_int(msg):
    ok = False
    valor = 0
    while True:
        num = str(input(msg))
        if num.isnumeric():
            valor = int(num)
            ok = True
        else:
            print('\033[0;31mERRO! Digite um número inteiro válido.\033[m')
        if ok:
            break
    return valor


n = leia_int('Digite um número: ')
print(f'Você acabou de digitar o número {n}')
