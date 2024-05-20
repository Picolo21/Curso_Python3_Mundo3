# Crie um programa onde o usuário digite uma expressão qualquer que use parênteses. Seu aplicativo
# deverá analisar se a expressão passada está com os parênteses abertos e fechados na ordem correta.

expression = input('Digite a expressão: ')
characters = list()

for symbol in expression:
    if (symbol == '('):
        characters.append('(')
    if (symbol == ')'):
        if (len(characters) > 0):
            characters.pop()
        else:
            characters.append(')')

print()
if (len(characters) == 0):
    print('A expressão está válida!')
else:
    print('A expressão está errada!')
