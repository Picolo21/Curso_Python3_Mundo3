# Faça um programa que tenha uma função chamada área(), que receba as dimensões de um terreno
# retangular (largura e comprimento) e mostre a área do terreno.

def calculates_area(width, length):
    area = length * width
    print(f'A área de um terreno {width:.2f} m x {length:.2f} m é de {area:.2f} m²')


print('=' * 50)
print(f'{'CONTROLE DE TERRENOS':^50}')
print('=' * 50, end='\n\n')

width = float(input('LARGURA (m): '))
length = float(input('COMPRIMENTO (m): '))
calculates_area(width, length)
