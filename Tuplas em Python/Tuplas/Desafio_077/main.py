# Crie um programa que tenha uma tupla com várias palavras (não usar acentos). Depois disso,
# você deve mostrar, para cada palavra, quais são as suas vogais

words = ('aprender', 'programar', 'linguagem', 'python', 'curso', 'gratis', 'estudar', 'praticar',
         'trabalhar', 'mercado', 'programador', 'futuro')

for word in words:
    print(f'Na palavra {word.upper()} temos a(s) vogal(is):', end='')
    for letter in word.upper():
        if ((letter == 'A') or (letter == 'E') or (letter == 'I') or (letter == 'O') or (letter == 'U')):
            print(f' {letter}', end='')
    print()
