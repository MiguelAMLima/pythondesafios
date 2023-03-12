# Crie um programa que leia o nome de uma cidade e diga se ela
# começa ou não com a palavra "santo".
"""cidade = str(input('Em que cidade você nasceu? ')).strip().lower().split()
print('A sua cidade começa com a palavra "Santo"?', 'santo' in cidade[0])"""

cidade = str(input('Em que cidade você nasceu? ')).strip()
print('A sua cidade começa com a palavra "Santo"?', cidade[:5].lower() == 'santo')
