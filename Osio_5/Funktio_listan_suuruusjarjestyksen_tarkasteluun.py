"""
COMP.CS.100
Tekijä: Vili Ikäheimo
Opiskelijanumero: 150286761
Tehtävä
"""


def is_the_list_in_order(lista):
    """
    tarkastaa onko annetun listan arvot suurusjärjestyksessä
    :param lista:
    :return:
    """
    if lista:
        edellinen = lista[0]
        for i in lista:
            if edellinen > i:
                return False
            edellinen = i
    return True


def main():
    print(is_the_list_in_order([1, 2, 5, 6, 5, 9]))


if __name__ == "__main__":
    main()
