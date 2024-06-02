# Faça um programa que tenha uma função chamada maior(), que receba vários parâmetros com valores
# inteiros. Seu programa tem que analisar todos os valores e dizer qual deles é o maior

from time import sleep


def bigger(*values):
    write_line()
    print('Analisando os valores passados...')
    print('Os valores informados foram: ', end='')
    for value in values:
        print(value, end=' ')
        sleep(0.5)
    print(f'\nForam informados {len(values)} valores ao todo')

    bigger = 0
    for value in range(0, len(values)):
        if (value == 0):
            bigger = value

        if (values[value] > bigger):
            bigger = values[value]

    print(f'O maior valor informado foi o {bigger}')
    write_line()


def write_line():
    print('=' * 50)


bigger(2, 9, 4, 5, 7, 1)
bigger(4, 7, 0)
bigger(1, 2)
bigger(6)
bigger()
