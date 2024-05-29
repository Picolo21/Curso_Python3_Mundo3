# Crie um programa que leia nome, ano de nascimento e carteira de trabalho e cadastre-os (com idade)
# em um dicionário. Se por acaso a CTPS for diferente de ZERO, o dicionário receberá também o ano
# de contratação e o salário. Calcule e acrescente, além da idade, com quantos anos a pessoa vai
# se aposentar, levando em conta 35 anos de contribuição para ambos os sexos.

from datetime import date

person = dict()

person['nome'] = input('Nome: ')
birth_year = int(input('Ano de Nascimento: '))
person['CTPS'] = int(input('Carteira de Trabalho (0 não tem): '))

if (person['CTPS'] != 0):
    person['ano_de_contracação'] = int(input('Ano de contratação: '))
    person['salário'] = float(input('Salário: R$ '))

age = (date.today().year - birth_year)
person['idade'] = age

print()
print('=' * 50)
print()

print(f'Nome tem o valor {person['nome']}')
print(f'Idade tem o valor {person['idade']}')
print(f'CTPS tem o valor {person['CTPS']}')

if (person['CTPS'] != 0):
    print(f'Ano de contratação tem o valor {person['ano_de_contracação']}')
    print(f'Salário tem o valor {person['salário']:.2f}')
    print(f'Aposentadoria tem o valor {(person['ano_de_contracação'] + 35) - birth_year}')
