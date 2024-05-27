# Crie um programa que leia nome e duas notas de vários alunos e guarde tudo em uma lista composta.
# No final, mostre um boletim contendo a média de cada um e permita que o usuário possa mostrar as
# notas de cada aluno individualmente


people = []
choice = ''

while (choice != 'N'):
    grades = []
    person = []

    name = input('Nome: ')
    person.append(name)

    for grade in range(0, 2):
        grade = float(input(f'Nota {grade + 1}: '))
        grades.append(grade)
    average = (grades[0] + grades[1]) / 2.0
    grades.append(average)
    person.append(grades)

    people.append(person)

    choice = input('Quer continuar [S / N]? ').upper()

print()
print('=' * 50, end='\n\n')

print(f'{'RA':<5} {'NOME':<30} {'MÉDIA':<5}')
print('-' * 50)

for student in range(0, len(people)):
    print(f'{(student + 1):<5} {(people[student][0]):<30} {(people[student][1][2]):<5.2f}')

print('-' * 50)

option = 0

while (option != 999):
    option = int(input('Mostrar notas de qual aluno (999 interrompe)? '))

    if ((option < 1) or (option > len(people))):
        print('Opção inválida. Por favor, escolha novamente...')
        print('-' * 50)
        continue

    print(f'Notas de {people[option - 1][0]} são {people[option - 1][1][0]:.2f} e {people[option - 1][1][1]:.2f}')
    print('-' * 50)

print()
print('FINALIZANDO...')
print('VOLTE SEMPRE!')
