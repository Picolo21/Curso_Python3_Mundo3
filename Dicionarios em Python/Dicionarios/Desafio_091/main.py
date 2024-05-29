# Crie um programa onde 4 jogadores joguem um dado e tenham resultados aleatórios. Guarde esses
# resultados em um dicionário. No final, coloque esse dicionário em ordem, sabendo que o vencedor
# tirou o maior número no dado

from random import randint
from time import sleep
from operator import itemgetter

game = {
    'jogador_1': randint(1, 6),
    'jogador_2': randint(1, 6),
    'jogador_3': randint(1, 6),
    'jogador_4': randint(1, 6)
}

ranking = list()

for key, values in game.items():
    print(f'{key} tirou {values} no dado.')
    sleep(1)

ranking = sorted(game.items(), key=itemgetter(1), reverse=True)

print()
print('=' * 50)
print(' ' * 20, 'RANKING:')
print('=' * 50)
print()

for index, value in enumerate(ranking):
    print(f'{index + 1}º lugar: {value[0]} com {value[1]}')
