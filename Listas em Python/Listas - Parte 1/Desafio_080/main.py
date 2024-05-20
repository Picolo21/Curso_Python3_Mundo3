# Crie um programa onde o usuário possa digitar cinco valores numéricos e cadastre-os em
# uma lista, já na posição correta de inserção (sem usar o sort()). No final, mostre a lista
# ordenada na tela.

numbers = list()

for count in range(0, 5):
    value = int(input('Digite um valor: '))

    if (count == 0):
        numbers.append(value)
        print(f'{value} foi adicionado ao final da lista...', end='\n\n')
        continue
    else:
        for list_count in range(0, len(numbers)):
            if (value < numbers[list_count]):
                numbers.insert(list_count, value)
                print(f'{value} foi adicionado na posição {list_count} da lista...', end='\n\n')
                break
            if (value == numbers[list_count]):
                numbers.insert(list_count, value)
                print(f'{value} foi adicionado na posição {list_count} da lista...', end='\n\n')
                break
            if ((list_count == (len(numbers) - 1)) and (value > numbers[len(numbers) - 1])):
                numbers.insert((list_count + 1), value)
                print(f'{value} foi adicionado na posição {list_count + 1} da lista...', end='\n\n')
                break

print('=' * 50, end='\n\n')
print(f'Os valores digitados em ordem crescente foram {numbers}')
