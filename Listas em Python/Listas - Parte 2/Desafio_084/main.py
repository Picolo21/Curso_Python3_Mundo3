# Faça um programa que leia nome e peso de várias pessoas, guardando tudo em uma lista. No
# final, mostre:

# A) Quantas pessoas foram cadastradas
# B) Uma listagem com as pessoas mais pesadas
# C) Uma listagem com as pessoas mais leves

people = list()
choice = ''
max_weight = 0
min_weight = 0
heavy_people = list()
lighter_people = list()

while (choice != 'N'):
    person = list()
    name = input('Nome: ')
    person.append(name)
    weight = float(input('Peso: '))
    person.append(weight)
    people.append(person[:])
    person.clear()
    choice = input('Quer continuar [S / N]? ').upper()

for person in people:
    if (min_weight == 0):
        min_weight = person[1]
    if (person[1] < min_weight):
        min_weight = person[1]
    if (person[1] > max_weight):
        max_weight = person[1]

for person in people:
    if (person[1] == max_weight):
        heavy_people.append(person[0])
        continue
    if (person[1] == min_weight):
        lighter_people.append(person[0])

print()
print('=' * 50, end='\n\n')
print(f'Ao todo, você cadastrou {len(people)} pessoa(s).')
print(f'O maior peso foi de {max_weight:.2f} Kg. Peso de {heavy_people}')
print(f'O menor peso foi de {min_weight:.2f} Kg. Peso de {lighter_people}')
