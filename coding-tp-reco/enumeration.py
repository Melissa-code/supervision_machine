"""Module Enumeration

Présentation de enumertion
(le fichier liste.py ne pouvait pas être créé : conflit de nom)

Copyright (c) 2021 Thierry P.G. DECKER
All Rights Reserved.
Released under the MIT license

"""


def main():
    """Les listes"""
    #
    # une liste est un tableau mutable
    #
    liste = ["ABC", 1, [10, 20, 30]]
    # print(liste[2][1])
    # for caractere in liste[2]:
    #    print(caractere)
    #
    # liste = [
    #    [0, 1, 2, 3, 4, 5],
    #    [10, 20, 30, 40, 50],
    # ]
    # for i in range(len(liste)):
    #    for j in range(len(liste[i])):
    #        print(liste[i][j])
    #
    # for ligne in liste:
    #    for valeur_colonne in ligne:
    #        print(valeur_colonne)
    #
    # liste = []
    # for i in range(10):
    #     liste.append(i)
    # print(liste)
    #
    # Liste en compréhension
    #
    liste = [i for i in range(10)]
    print(liste)


if __name__ == '__main__':
    main()