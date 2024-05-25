# Crie um programa que crie uma matriz de dimensão 3 x 3 e preencha com valores lidos pelo
# teclado. No final, mostre a matriz na tela com a formatação correta

numbers = list()

for counter_one in range(0, 3):
    for counter_two in range(0, 3):
        value = int(input(f'Digite um valor para [{counter_one}, {counter_two}]: '))
        numbers.append(value)

print()
print('=' * 50, end='\n\n')

counter = 0

for counter_one in range(0, 3):
    for counter_two in range(0, 3):
        print(f'[ {numbers[counter]} ]', end='')
        counter += 1
        if (counter_two == 2):
            print()
