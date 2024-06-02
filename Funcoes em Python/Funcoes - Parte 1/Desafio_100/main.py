# Faça um programa que tenha uma lista chamada números e duas funções chamadas sorteia() e
# somaPar(). A primeira função vai sortear 5 números e vai colocá-los dentro da lista
# e a segunda função vai mostrar a soma entre todos os valores PARES sorteados pela
# função anterior.

from random import randint
from time import sleep


def draw_number(list):
    for counter in range(0, 5):
        value = randint(1, 10)
        print(value, end=' ')
        sleep(0.5)
        list.append(value)
    print()
    print('PRONTO. Todos os 5 números foram sorteados!')


def sum_even(list):
    sum = 0
    for value in list:
        if ((value % 2) == 0):
            sum += value
    print(f'Somando todos os valores pares de {list}, temos um total de {sum}')


numbers = list()
print('Sorteando 5 valores aleatóriamente...')
print('Os valores sorteados foram: ', end='')
draw_number(numbers)
sum_even(numbers)
