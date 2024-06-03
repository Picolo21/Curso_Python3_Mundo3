# Crie um programa que tenha uma função chamada voto() que vai receber como parâmetro o ano de
# nascimento de uma pessoa, retornando um valor literal indicando se uma pessoa tem voto
# NEGADO, OPCIONAL ou OBRIGATÓRIO nas eleições

def calculating_age(birth_date):
    from datetime import date

    now = date.today().year
    age = now - birth_date

    if (age < 16):
        return f'Com {age} anos: AINDA NÃO VOTA'
    if ((age < 18) or (age > 70)):
        return f'Com {age} anos: VOTO OPCIONAL'
    if (age >= 18):
        return f'Com {age} anos: VOTO OBRIGATÓRIO'


birth_date = int(input('Em que ano você nasceu? '))
print(calculating_age(birth_date))
