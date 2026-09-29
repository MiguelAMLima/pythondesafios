# Faça um programa que tenha uma função chamada escreva(),
# que receba um texto qualquer como parâmetro e mostre
# uma mensagem com bordas de tamanho adaptável.
def escreva(msg):
    tam = len(msg) + 4
    print('~' * tam)
    print(f'  {msg}')
    print('~' * tam)


mensagem = str(input('Escreva sua mensagem para personalizar: '))
escreva(mensagem)
