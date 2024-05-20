# Crie um programa que vai ler vários números e colocar em uma lista. Depois disso, crie
# duas listas extras que vão conter apenas os valores pares e os valores ímpares digitados,
# respectivamente. Ao final, mostre o conteúdo das três listas geradas

list_one = list()
list_two = list()
list_three = list()
choice = ''

while (choice != 'N'):
    value = int(input('Digite um valor: '))
    list_one.append(value)
    choice = input('Quer continuar [S / N]? ').upper()
    print()

for number in list_one:
    if ((number % 2) == 0):
        list_two.append(number)
    else:
        list_three.append(number)

print('=' * 50, end='\n\n')
print(f'A lista completa é {list_one}')

if (len(list_two) == 0):
    print('Nenhum número par foi digitado')
else:
    print(f'A lista com todos os números pares digitados é {list_two}')

if (len(list_three) == 0):
    print('Nenhum número ímpar foi digitado')
else:
    print(f'A lista com todos os números ímpares digitados é {list_three}')
