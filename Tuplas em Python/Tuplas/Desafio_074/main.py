# Crie um programa que vai gerar cinco números aleatórios e colocar em uma tupla. Depois disso, mostre
# a listagem de números gerados e também indique o menor e o maior valor que estão na tupla

from random import randint

values = (randint(0, 100), randint(0, 100), randint(0, 100), randint(0, 100), randint(0, 100))

print('Os valores sorteados foram:', end='\n\n')

for position, value in  enumerate(values):
    print(f'{position + 1}º - {value}')

print()
print(f'O maior valor sorteado foi {sorted(values)[0]}')
print(f'O maior valor sorteado foi {sorted(values)[4]}')
