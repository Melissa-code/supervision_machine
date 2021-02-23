"""Module Dictionnaires

Présentation des dictionnaires

Copyright (c) 2021 Thierry P.G. DECKER
All Rights Reserved.
Released under the MIT license

"""


def main():
    """Les dictionnaires"""
    #
    # un dictionnaire est un tableau associatif (clé + valeur)
    #
    # dictionnaire = {
    #    "Nom": "DECKER",
    #    "Prenom": "Thierry",
    # }
    # print(dictionnaire["Nom"])
    # print(dictionnaire["Prenom"])
    #
    dictionnaire = {
        "DECKER": {
            "prenom": "Thierry",
            "age": 10,
        },
    }
    print(dictionnaire["DECKER"])


if __name__ == '__main__':
    main()