# Crie um programa que vai ler vários números e colocar em uma lista. Depois disso, mostre:

# A) Quantos números foram digitados.
# B) A lista de valores ordenada de forma decrescente.
# C) Se o valor 5 foi digitado e está ou não na lista.

numbers = list()
choice = ''

while (choice != 'N'):
    value = int(input('Digite um valor: '))
    numbers.append(value)
    choice = input('Quer continuar [S / N]? ').upper()
    print()

print('=' * 50, end='\n\n')
print(f'Você digitou {len(numbers)} elementos')
print(f'Os valores em ordem decrescente são {sorted(numbers, reverse=True)}')
if (5 in numbers):
    print('O valor 5 faz parte da lista!')
else:
    print('O valor 5 não foi encontrado na lista!')
