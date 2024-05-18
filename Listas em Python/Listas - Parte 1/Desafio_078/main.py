# Faça um programa que leia 5 valores inteiros e guarde-os em uma lista. No final, mostre qual
# foi o maior e o menor valor digitado e as respectivas posições na lista

values = list()
bigger = 0
smaller = 0

for cont in range(0, 5):
    number = int(input(f'Digite o {cont + 1}° valor para a Posição {cont}: '))
    values.append(number)

print('=' * 50)
print(f'Você digitou os valores {values}')

for index in range(0, len(values)):
    if (index == 0):
        bigger = smaller = values[index]
    if (bigger < values[index]):
        bigger = values[index]
    if (smaller > values[index]):
        smaller = values[index]

print(f'O maior valor digitado foi {bigger} e ele aparece na(s) posição(ões) ', end='')
for index, value in enumerate(values):
    if (value == bigger):
        print(f'{index}...', end=' ')

print()
print(f'O menor valor digitado foi {smaller} e ele aparece na(s) posição(ões) ', end='')
for index, value in enumerate(values):
    if (value == smaller):
        print(f'{index}...', end=' ')
