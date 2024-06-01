# Crie um programa que leia nome, sexo e idade de várias pessoas, guardando os dados em um dicionário
# e todos os dicionários em uma lista. No final, mostre:

# A) Quantas pessoas foram cadastradas
# B) A média de idade do grupo
# C) Uma lista com todas as mulheres
# D) Uma lista com todas as pessoas com idade acima da média

people = list()
person = dict()
choice = ''

while (choice != 'N'):
    person['nome'] = input('Nome: ')
    person['sexo'] = input('Sexo [M / F]: ').upper()
    person['idade'] = int(input('Idade: '))
    people.append(person.copy())
    choice = input('Quer continuar [S / N]? ').upper()

sum = 0
for person in people:
    sum += person['idade']

average = sum / len(people)

women = list()
for person in people:
    if (person['sexo'] == 'F'):
        women.append(person.copy())

print()
print('=' * 50)
print()

print(f'-> O grupo tem {len(people)} pessoa(s)')
print(f'-> A média de idade é de {average:.2f} anos')
print(f'-> As mulheres cadastradas foram: ', end='')
for woman in women:
    print(woman['nome'], end=' ')
print()
print('-> Lista das pessoas que tem idade acima da média:')
print()
for person in people:
    if (person['idade'] > average):
        print(f'Nome = {person['nome']}; sexo = {person['sexo']}; idade = {person['idade']}')

print()
print('=' * 10, f'{'ENCERRADO':^15}', '=' * 10)
