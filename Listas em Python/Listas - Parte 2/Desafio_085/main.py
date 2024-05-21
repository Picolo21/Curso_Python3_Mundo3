# Crie um programa onde o usuário possa digitar sete valores numéricos e cadastre-os em uma
# lista única que mantenha separados os valores pares e ímpares. No final, mostre os valores
# pares e ímpares em ordem crescente.

# OBS: irei adotar posição 0 da lista para os números pares e posição 1 para o números ímpares

numbers = [[], []]

for position in range(0, 7):
    value = int(input(f'Digite o {position + 1}º valor: '))
    if ((value % 2) == 0):
        numbers[0].append(value)
    else:
        numbers[1].append(value)

print()
print('=' * 50, end='\n\n')
print(f'Os valores pares digitados foram: {sorted(numbers[0])}')
print(f'Os valores ímpares digitados foram: {sorted(numbers[1])}')
