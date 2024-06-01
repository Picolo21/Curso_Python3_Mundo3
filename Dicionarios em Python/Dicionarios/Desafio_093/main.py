# Crie um programa que gerencie o aproveitamento de um jogador de futebol. O programa vai ler
# o nome do jogador e quantas partidas ele jogou. Depois vai ler a quantidade de gols feitos
# em cada partida. No final, tudo isso será guardado em um dicionário, incluindo o total de gols
# feitos durante o campeonato.

player = dict()

player['nome'] = input('Nome do jogador: ')
player['gols'] = list()

games = int(input(f'Quantas partidas {player['nome']} jogou? '))

for game in range(0, games):
    goals = int(input(f'Quantos gols na partida {game + 1}? '))
    player['gols'].append(goals)

sum = 0

for goal in player['gols']:
    sum += goal

player['total'] = sum

print()
print('=' * 50)
print()

print(player)

print()
print('=' * 50)
print()

for key, values in player.items():
    print(f'O campo {key} tem o valor {values}')

print()
print('=' * 50)
print()

print(f'O jogador {player['nome']} jogou {games} partida(s)', end='\n\n')
for game in range(0, len(player['gols'])):
    print(f'Na {game + 1}ª partida, fez {player['gols'][game]} gol(s)')
print()
print(f'Foi um total de {sum} gol(s)')
