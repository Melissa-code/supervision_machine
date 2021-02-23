"""Module algorithme_caesar2

Copyright (c) 2021 Melissa BENARD
All Rights Reserved.
Released under the MIT license

"""
#
# Coder l'algorithme de Caesar
#
# - Demander la chaîne de caractère à chiffrer à l'utilisateur: input()
# - Demander à l'utilisateur le décalage à appliquer au chiffrement
# - Afficher la chaîne chiffrée
#
# Exemple:
#
# Texte en clair : "ABCDE...CYZ"
# Décalage : 2
# texte chiffré : "CDEFG...ZAB"


def main():
    """The main function
    """

    liste = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's',
                      't', 'u', 'v', 'w', 'x', 'y', 'z']

    #
    # je parcours et dédouble ma liste
    #
    for x in range(len(liste)):
        liste.append(liste[x])
    #
    # je crée une fonction qui retourne le résultat de l'index de la lettre + decalage
    #
    def chiffrage_lettre(lettre, liste, decalage):
        """Write string into a file

            Args:
            lettre (str)
            liste [] : alphabet
            decalage (str)

            Return: '?'
            """
        for i in range(len(liste)):
            if lettre == ' ':
                return ' '
            elif liste[i] == lettre:
                return str(liste[i+decalage])
        return '?'
    #
    # j'initialise ma variable en string
    #
    message_chiffre = str()
    #
    # J'ajoute à chaque lettre du message un décalage
    #
    while True:
        message = input('Veuillez entrer votre message: ')
        decalage = int(input('Veuillez entrer le decalage: '))
        for lettre in message:
            message_chiffre += chiffrage_lettre(lettre, liste, decalage)

        print('Voici le message chiffré :', message_chiffre)
        break


if __name__ == '__main__':
    main()
