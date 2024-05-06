# Crie um programa que tenha uma tupla única com nomes de produtos e seus respectivos preços,
# na sequência. No final, mostre uma listagem de preços, organizando os dados em forma tabular

print('=' * 40)
print(' ' * 10, 'LISTAGEM DE PREÇOS')
print('=' * 40)

objects_list = ('Lápis', 1.75, 'Borracha', 2, 'Caderno', 15.90, 'Estojo', 25, 'Transferidor', 4.2,
                'Compasso', 9.99, 'Mochila', 120.32, 'Canetas', 22.3, 'Livro', 34.9)

for count in range(0, len(objects_list)):
    if (count % 2 == 0):
        print(f'{objects_list[count]:<}{'.'*(25-len(objects_list[count]))}', end='')
    else:
        print(f' R$ {objects_list[count]:>10,.2f}', end='\n')

print('=' * 40)
