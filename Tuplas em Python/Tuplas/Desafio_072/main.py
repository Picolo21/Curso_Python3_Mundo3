# Crie um programa que tenha uma tupla totalmente preenchida com uma contagem por extenso, de
# zero até vinte. Seu programa deverá ler um número pelo teclado (entre 0 e 20) e mostrá-lo
# por extenso.

numbers = ('zero', 'um', 'dois', 'três', 'quatro', 'cinco', 'seis', 'sete',
           'oito', 'nove', 'dez', 'onze', 'doze', 'treze', 'quatorze', 'quinze',
           'dezesseis', 'dezessete', 'dezoito', 'dezenove', 'vinte')

value = int(input('Digite um número entre 0 e 20: '))

while ((value < 0) or (value > 20)):
    value = int(input('Tente novamente. Digite um número entre 0 e 20: '))

print(f'Você digitou o número {numbers[value]}')
