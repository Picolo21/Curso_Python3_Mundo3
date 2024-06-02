# Faça um programa que tenha uma função chamada escreva(), que receba um texto qualquer como
# parâmetro e mostre uma mensagem com tamanho adaptável.

# Exemplo:

# escreva('Olá, Mundo!')

#Saída:

# ===============
#   Olá, Mundo!
# ===============

def write(message):
    length = len(message) + 10
    print('=' * length)
    print(f'{message:^{length}}')
    print('=' * length)


write('Gustavo Guanabara')
write('Curso de Python no YouTube')
write('CeV')
