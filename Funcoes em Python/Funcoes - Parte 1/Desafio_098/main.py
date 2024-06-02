# Faça um programa que tenha uma função chamada contador(), que receba 3 parâmetros: início, fim e passo
# e realize a contagem.

# Seu programa tem que realizar 3 contagens através da função criada:

# A) De 1 até 10, de 1 em 1
# B) De 10 até 0, de 2 em 2
# C) Uma contagem personalizada

from time import sleep


def counter(start, end, step):
    if (step == 0):
        step = 1

    print(f'Contagem de {start} até {end} de {abs(step)} em {abs(step)}')

    if (start > end):
        if (step > 0):
            step *= -1
        for value in range(start, (end - 1), step):
            print(value, end=' ')
            sleep(1)
        print('FIM!')

    if (start < end):
        if (step < 0):
            step *= -1
        for value in range(start, (end + 1), step):
            print(value, end=' ')
            sleep(1)
        print('FIM!')


def write_line():
    print('=' * 50)


write_line()
counter(1, 10, 1)
write_line()
counter(10, 0, 2)
write_line()
print('Agora é sua vez de personalizar a contagem!')
start = int(input('Início: '))
end = int(input('Fim: '))
step = int(input('Passo: '))
write_line()
counter(start, end, step)
