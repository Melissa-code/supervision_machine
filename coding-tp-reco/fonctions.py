"""Module Structures de fonctions

Présentation des fonctions

Copyright (c) 2021 Thierry P.G. DECKER
All Rights Reserved.
Released under the MIT license

"""

import formules_volume as fv


def main():
    """Utilisation des fonctions"""
    # rayon = 10
    # volume = calculer_volume_sphere(rayon)
    # print('volume sphere:', volume)
    # print(calculer_volume_boite(10, 10, 2))
    # print(calculer_volume_boite(hauteur=2, longueur=10, largeur=10))
    # print(calculer_volume_boite(largeur=10))
    print(fv.calculer_volume_boite(20, hauteur=30, largeur=10))


if __name__ == '__main__':
    main()