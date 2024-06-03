# Faça um programa que tenha uma função chamada ficha(), que receba dois parâmetros opcionais: o nome
# de um jogador e quantos gols ele marcou. O programa deverá ser capaz de mostrar a ficha do jogador,
# mesmo que algum dado não tenha sido informado corretamente

def file(name='<desconhecido>', goals=''):
    if (name.strip() == ''):
        name = '<desconhecido>'

    if (goals.isnumeric()):
        goals = int(goals)
    else:
        goals = 0

    return f'O jogador {name} fez {goals} gol(s) no campeonato'


name = input('Nome do Jogador: ')
goals_number = input('Número de Gols: ')

print(file(name, goals_number))
