"""Module encodage

Copyright (c) 2021 Melissa BENARD
All Rights Reserved.
Released under the MIT license

"""

# chaine = "ABCDE"


# def tranformer_chaine_liste(chaine):
#    chaine = chaine1
#    result = (list(chaine.strip()))
#    print(result)
#    return result

#
# Initialistation de ma variable text
#
text = "ABCDE"


def encoder_chaine(chaine):
    """encoding Base 64

        Args:
            chaine (str): The string chaine to encode

        Returns:
            The encoding in Base 64
    """
    #
    # 1. Transformer la chaine "ABCDE" en liste
    #
    # list() crée un objet liste
    # strip retire les "" caractères de debut et fin de la chaîne de caractères
    #
    liste = (list(chaine.strip()))
    print(liste)
    #
    # 2. Remplacer dans la liste les caractères par leur code Unicode
    #
    # enumerate() pour avoir un compteur dans la boucle for
    # ord() renvoie un caractère Unicode
    #
    for index, car in enumerate(liste):
        liste[index] = ord(liste[index])
    print(liste)
    #
    # 3. Transformer chaque valeur par sa représentation binaire
    #
    # bin() renvoie une chaîne binaire
    #
    for index, nb in enumerate(liste):
        liste[index] = bin(liste[index])
    print(liste)
    #
    # 4. Supprimer les '0b' en début de chaque élément
    #
    # nb[2:] permet de retirer les 2 premiers éléments de la liste
    #
    for index, nb in enumerate(liste):
        liste[index] = nb[2:]
    print(liste)
    #
    # 5. Transformer chaque élément et ajoutant autant de zéros à gauche qu'il en faut pour avoir 8 caracteres
    #
    # zfill() remplit une chaîne de caractères avec autant de zeros que mis en parametre
    #
    for index, nb in enumerate(liste):
        liste[index] = nb.zfill(8)
    print(liste)
    #
    # 6. Transformer cette liste en chaîne de caractères
    #
    # join() crée et renvoie une chaîne de caractères
    #
    liste = "".join(liste)
    print(liste)
    #
    # 7. Créer à partir de cette chaîne une liste dont les éléments font 6 caractères
    #
    # [index:index+6] ajout de la valeur 6 à l'index
    #
    liste2 = []
    for index in range(0, len(liste), 6):
        liste2.append(liste[index: index + 6])
    print(liste2)
    #
    # 8. Ajouter 2 zeros au dernier élément de la liste
    #
    # ljust(6,"0")
    #
    for index, nb in enumerate(liste2):
        liste2[index] = nb.ljust(6, "0")
    print(liste2)
    #
    # 9. Transformer la chaîne de caractères écrites en binaire en nombres décimaux
    #
    # int() transforme en nombre décimal
    #
    for index, nb in enumerate(liste2):
        liste2[index] = int(nb, base=2)
    print(liste2)
    #
    # 10. Transformer le code : leurs caracteres dans la table Base 64 :
    #
    table_64 = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789+/"
    liste3 = []
    for element in liste2:
        new_char = table_64[element]
        liste3.append(new_char)
    print(liste3)
    #
    # 11. Transformer la liste en chaine de caractères
    #
    liste3 = "".join(liste3)
    print(liste3)
    #
    # 12. La chaine de caractere finale doit avoir une longueur multiple de 4:
    #
    # modulo % 4 : divisible par 4
    #
    while len(liste3) % 4 != 0:
        liste3 = liste3 + '='
    print(liste3)


def main():
    """
    Encodage d'une chaine ASCII quelconque en Base 64
    """
    # tranformer_chaine_liste(chaine1)
    encoder_chaine(text)


if __name__ == '__main__':
    main()