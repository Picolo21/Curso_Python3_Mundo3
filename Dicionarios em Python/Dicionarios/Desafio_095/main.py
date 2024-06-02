# Aprimore o DESAFIO 093 para que ele funcione com vários jogadores, incluindo um sistema de
# visualização de detalhes do aproveitamento de cada jogador

players = list()
player = dict()
choice = ''

while (choice != 'N'):
    goals = list()
    player['nome'] = input('Nome do jogador: ')
    games = int(input(f'Quantas partidas {player['nome']} jogou? '))
    for game in range(0, games):
        goal = int(input(f'Quantos gols na {game + 1}ª partida? '))
        goals.append(goal)
    player['gols'] = goals

    sum = 0
    for goal in goals:
        sum += goal
    player['total_de_gols'] = sum
    players.append(player.copy())

    choice = input('Quer continuar [S / N]? ').upper()
    if ((choice != 'S') or (choice != 'N')):
        while not((choice == 'S') or (choice == 'N')):
            print('ERRO! Escolha S ou N para continuar usando o programa')
            choice = input('Quer continuar [S / N]? ').upper()

    if (choice == 'S'):
        print('-' * 50)

print()
print('=' * 100)
print()

print(f'{'Código':>6} {'Nome':<20} {'Gols':<50} {'Total':<10}')
print('-' * 100)
for person in range(0, len(players)):
    print(f'{(person + 1):>6} {players[person]['nome']:<20} {str(players[person]['gols']):<50} {players[person]['total_de_gols']:<10}')
print('-' * 100)

option = int(input('Mostrar os dados de qual jogador (999 encerra o programa)? '))
while (option != 999):
    if ((option < 1) or (option > len(players))):
        print(f'ERRO! Não existe jogador com código {option}. Tente novamente')
        print('-' * 50)
        option = int(input('Mostrar os dados de qual jogador (999 encerra o programa)? '))
        continue

    print(f'-- LEVANTAMENTO DO JOGADOR {players[option - 1]['nome']}')
    for game in range(0, len(players[option - 1]['gols'])):
        print(f'No {game + 1}º jogo, fez {players[option - 1]['gols'][game]} gol(s)')

    print('-' * 50)
    option = int(input('Mostrar os dados de qual jogador (999 encerra o programa)? '))

print('=' * 25, f'{'VOLTE SEMPRE':^16}', '=' * 25)
