"""
COMP.CS.100
Tekijä: Vili Ikäheimo
Opiskelijanumero: 150286761
Tehtävä
"""


def are_all_members_same(lista):
    """
    ottaa listan ja paluttaa onko kaikki sen arvot samanlaisia
    :param lista:
    :return:
    """
    if lista:
        edellinen_arvo = lista[0]
        for e in lista:
            if edellinen_arvo != e:
                return False
        return True
    return True


def main():
    print(are_all_members_same([1,1,1,1,1,1]))
    print(are_all_members_same([]))


if __name__ == "__main__":
    main()
