# Faça um programa que leia nome e média de um aluno, guardando também a situação em um dicionário.
# No final, mostre o conteúdo da estrutura na tela

student = dict()

student['nome'] = input('Nome: ')
student['média'] = float(input(f'Média de {student["nome"]}: '))

if (student['média'] >= 7):
    student['situação'] = 'Aprovado'
else:
    student['situação'] = 'Reprovado'

print()
print(f'Nome é igual a {student['nome']}')
print(f'Média é igual a {student['média']:.2f}')
print(f'Situação é igual a {student['situação']}')
