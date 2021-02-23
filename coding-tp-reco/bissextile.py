"""Module Structures de bissextile

Présentation de bissextile

Copyright (c) 2021 Thierry P.G. DECKER
All Rights Reserved.
Released under the MIT license

"""


def main():
    """Année bissextile

    1- si l'année est divisible par 4 non divisible par 100
    ou
    2- si l'année est divisible par 400
    """
    annee = 2015
    #
    # test et affichage si annee est bissextile
    #
    if (annee % 4 == 0 and annee % 100 != 0) or annee % 400 == 0:
        print(annee, ' : année bissextile')
    else:
        print(annee, ': année non bissextile')


if __name__ == '__main__':
    main()