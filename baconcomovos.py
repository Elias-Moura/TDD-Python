""" Aprendendo TDD

Bacom com ovos:

1 - Receber um número inteiro.
2 - Saber se o número é multiplo de 3 e 5:
    retornar bacon com ovos
3 - Saber se o número é multiplo apenas de 3:
    retornar bacon
4 - saber se o número é multiplo apenas de 5:
    retornar ovos
5 - saber se o número Não é multiplo de 3 e 5:
    Passar fome
"""


def bacon_com_ovos(x):
    assert isinstance(x, (int, float)), 'x deve ser int ou float'
    if x % 3 == 0 and x % 5 == 0:
        return 'Bacon com ovos'
    elif x % 3 == 0:
        return 'Bacon'
    elif x % 5 == 0:
        return 'Ovos'
    return 'Passar fome'
