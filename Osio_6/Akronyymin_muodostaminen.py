"""
COMP.CS.100
Tekijä: Vili Ikäheimo
Opiskelijanumero: 150286761
"""


def create_an_acronym(teksti):
    """
    muodostaa sanalle akronyymin
    :param teksti:
    :return:
    """
    teksti = teksti.upper()
    akronyyymi = teksti[0]
    seuraava_akronyymiin = False
    for c in teksti:
        if c == " ":
            seuraava_akronyymiin = True
        elif seuraava_akronyymiin:
            seuraava_akronyymiin = False
            akronyyymi += c
    return akronyyymi


def main():
    print(create_an_acronym("kissa paa k jgfjh  fgg"))


if __name__ == "__main__":
    main()