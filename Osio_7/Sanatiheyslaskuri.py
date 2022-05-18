"""
COMP.CS.100
Tekijä: Vili Ikäheimo
Opiskelijanumero: 150286761
"""


def arvojen_muokkaus(sanakirja, sanat):
    """
    laskee kuinka monta sanaa on teksissä ja muokkaa ne sanakirjaan
    :param sanakirja:
    :param sanat:
    :return:
    """
    for sana in sanat.split():
        if sana in sanakirja:
            sanakirja[sana] += 1
        else:
            sanakirja[sana] = 1


def print_arvot(sanakirja):
    """
    printaa sanakirjan arvot
    :param sanakirja:
    :return:
    """
    for i in sorted(sanakirja):
        print(i, ":", sanakirja[i], "times" )

def main():
    values = {}
    print("Enter rows of text for word counting. Empty row to quit.")
    teksti = input()
    while teksti != "":
        arvojen_muokkaus(values, teksti.lower())
        teksti = input()
    print_arvot(values)


if __name__ == "__main__":
    main()
