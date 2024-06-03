# Crie um programa que tenha uma função fatorial() que receba 2 parâmetros: o primeiro que indique
# o número a calcular e o outro chamado "show", que será um valor lógico (opcional) indicando se
# será mostrado ou não na tela o processo de cálculo do fatorial

def calculates_factorial(value, show=False):
    """
    -> Calcula o Fatorial de um número
    :param value: O número a ser calculado
    :param show: (opcional) Mostrar ou não a equação feita chegar no resultado
    :return: O valor do Fatorial de um número "value"
    """

    factorial = value
    for counter in range((value - 1), 0, -1):
        factorial *= counter

    if (show == True):
        equation = ''
        for counter in range(value, 0, -1):
            equation += f'{counter} '
            if (counter != 1):
                equation += 'x '
            else:
                equation += f'= {factorial:,}'
        return equation
    else:
        return f'{factorial:,}'


number = int(input('Escolha um número para calcular o fatorial: '))
print('-' * 50)
print(f'SHOW = FALSE: {calculates_factorial(number)}')
print(f'SHOW = TRUE: {calculates_factorial(number, True)}')
