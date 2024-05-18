# Crie um programa onde o usuário possa digitar vários valores numéricos e cadastre-os em uma
# lista. Caso o número já exista lá dentro, ele não será adicionado. No final, serão exibidos
# todos os valores únicos digitados, em ordem crescente.

choice = ''
values = list()

while (choice != 'N'):
    number = int(input('Digite um valor: '))
    if (number in values):
        print('Valor duplicado. Não vou adicionar esse número!')
    else:
        values.append(number)
        print('Valor adicionado com sucesso!')

    choice = input('Quer continuar [S / N]? ').upper()

print('=' * 50)
print(f'Você digitou os valores {sorted(values)}')
