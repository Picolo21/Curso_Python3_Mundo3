# Crie uma tupla preenchida com os 20 primeiros colocados da Tabela do Campeonato Brasileiro
# de Futebol, na ordem de colocação. Depois mostre:

# A) Apenas os 5 primeiros colocados
# B) Os últimos 4 colocados na tabela
# C) Uma lista com os times em ordem alfabética
# D) Em que posição na tabela está o time da Juventude

teams = ('Athletico-PR', 'Bahia', 'Botafogo', 'Atlético-MG', 'Bragantino', 'Palmeiras', 'Flamengo',
         'São Paulo', 'Internacional', 'Cruzeiro', 'Grêmio', 'Fortaleza', 'Criciúma', 'Corinthians',
         'Juventude', 'Fluminense', 'Vasco da Gama', 'EC Vitória', 'Atlético-GO', 'Cuiabá')

print('=' * 60)
print(' ' * 12, 'LISTA DE TIMES DO BRASILEIRÃO 2024')
print('=' * 60, end='\n\n')

print('-' * 60)

print('Classificação completa do Campeonato Brasileiro 2024', end='\n\n')

for position, team in enumerate(teams):
    print(f'{position + 1}º {team}')

print('-' * 60)

print('-' * 60)

print('5 primeiros colocados do Campeonato Brasileiro 2024', end='\n\n')

for position, team in enumerate(teams[:5]):
    print(f'{position + 1}º {team}')

print('-' * 60)

print('-' * 60)

print('4 últimos colocados do Campeonato Brasileiro 2024', end='\n\n')

for position, team in enumerate(teams[(len(teams) - 4):]):
    print(f'{position + (len(teams) - 4) + 1}º {team}')

print('-' * 60)

print('Lista Ordenada do Campeonato Brasileiro 2024', end='\n\n')

for team in sorted(teams):
    print(f'{team}')

print('-' * 60)

print('-' * 60)

print('Posição do Juventude no Campeonato Brasileiro 2024', end='\n\n')

for position, team in enumerate(teams):
    if (team == 'Juventude'):
        print(f'{team} está na {position + 1}ª posição do Campeonato Brasileiro 2024')

print('-' * 60)
