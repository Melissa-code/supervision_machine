"""Module name

Copyright (c) 2021 Thierry P.G. DECKER
All Rights Reserved.
Released under the MIT license

"""

import math

def calculer_volume_sphere(rayon):
    """calcul du volume d'une sphere

    Volume = 4/3 * pi * (R ** 3)

    Parametres entree :
        - rayon

    Retourne : Volume
    """
    volume = 4/3 * math.pi * (rayon ** 3)
    return volume


def calculer_volume_boite(longueur=1, largeur=1, hauteur=1):
    """calcul du volume d'une boite

    Parametres entrée:
        - Longueur
        - Largeur
        - Hauteur

    Volume = longueur * largeur * hauteur
    """
    return longueur * largeur * hauteur


def main():
    pass


if __name__ == '__main__':
    main()