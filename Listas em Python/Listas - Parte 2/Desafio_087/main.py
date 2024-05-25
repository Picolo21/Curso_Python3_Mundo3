# Aprimore o DESAFIO 086, mostrando no final:

# A) A soma de toos os valores pares
# B) A soma dos valores da terceira coluna
# C) O maior valor da segunda linha

numbers = [[], [], []]

for counter_one in range(0, 3):
    for counter_two in range(0, 3):
        value = int(input(f'Digite um valor para [{counter_one}, {counter_two}]: '))
        numbers[counter_one].append(value)

print()
print('=' * 50, end='\n\n')

for counter_one in range(0, 3):
    for counter_two in range(0, 3):
        print(f'[ {numbers[counter_one][counter_two]} ]', end='')
    print()

print()
print('=' * 50)

sum = 0

for counter_one in range(0, 3):
    for counter_two in range(0, 3):
        if ((numbers[counter_one][counter_two] % 2) == 0):
            sum += numbers[counter_one][counter_two]

print(f'A soma dos valores pares é igual a {sum}')

sum = 0

for counter in range(0, 3):
    sum += numbers[counter][2]

print(f'A soma dos valores da terceira coluna é igual a {sum}')

bigger = 0

for counter in range(0, 3):
    if (bigger == 0):
        bigger = numbers[1][counter]
        continue
    if (bigger < numbers[1][counter]):
        bigger = numbers[1][counter]

print(f'O maior valor da segunda linha é o {bigger}')
