"""Module Structures de controle

Présentation des structures de controle

Copyright (c) 2021 Thierry P.G. DECKER
All Rights Reserved.
Released under the MIT license

"""


def main():
    """The main function
    """
    #
    # if: conditionnal test
    #
    nombre = 10
    if not (nombre > 10 or nombre  == 10) and nombre < 100:
        print('vrai')


if __name__ == '__main__':
    main()