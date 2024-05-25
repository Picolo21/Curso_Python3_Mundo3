# Faça um programa que ajude um jogador da MEGA-SENA a criar palpites. O programa vai
# perguntar quantos jogos serão gerados e vai sortear 6 números entre 1 e 60 para
# cada jogo, cadastrando tudo em uma lista composta

import random
import time

numbers = list()

print('=' * 60)
print(' ' * 19, 'NÚMEROS DA MEGA-SENA')
print('=' * 60)

game_numbers = int(input('Quantos jogos você quer que eu sorteie? '))

for counter in range(0, game_numbers):
    numbers.append([])

for counter in range(0, len(numbers)):
    if (len(numbers[counter]) < 1):
        value = random.randint(1, 60)
        numbers[counter].append(value)
    while (len(numbers[counter]) < 6):
        value = random.randint(1, 60)
        if (value in numbers[counter]):
            continue
        else:
            numbers[counter].append(value)

print()
print('=' * 10, f'{'SORTEANDO OS JOGOS':^22}', '=' * 10, end='\n\n')

for games in range(0, len(numbers)):
    print(f'Jogo {games + 1}: { sorted(numbers[games])}')
    time.sleep(1)

print()
print('=' * 15, f'{'BOA SORTE!':^12}', '=' * 15)
