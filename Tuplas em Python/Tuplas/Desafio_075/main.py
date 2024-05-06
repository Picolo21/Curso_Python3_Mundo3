# Desenvolva um programa que leia quatro valores pelo teclado e guarde-os em um tupla
# No final, mostre:

# A) Quantas vezes apareceu o valor 9
# B) Em que posição foi digitado o primeiro valor 3
# C) Quais foram os números pares

one_value = int(input('Digite o 1º valor: '))
two_value = int(input('Digite o 2º valor: '))
three_value = int(input('Digite o 3º valor: '))
four_value = int(input('Digite o 4º valor: '))

values = (one_value, two_value, three_value, four_value)

print()
print('Você digitou os valores: ', end='')

for value in  values[:3]:
    print(f'{value} - ', end='')
print(values[3])

print(f'O valor 9 apareceu {values.count(9)} vez(es)')

if (values.count(3)):
    for position, value in enumerate(values):
        if (value == 3):
            print(f'O valor 3 apareceu primeiro na {position + 1}ª posição')
else:
    print('O valor 3 não apareceu nenhuma vez')




even = 0
for count in range(0, len(values)):
    if ((values[count] % 2) == 0):
        even += 1

if (even == 0):
    print('Nenhum valor par foi digitado')
else:
    print('O(s) valor(es) par(es) digitado(s) foi(ram): ', end='')
    count = 0
    while (count < len(values)):
        if (values[count] % 2 == 0):
            print(values[count], end=' ')
        count += 1
