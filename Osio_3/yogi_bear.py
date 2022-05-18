"""
COMP.CS.100
Tekijä: Vili Ikäheimo
Opiskelijanumero: 150286761
"""


def repeat_name(nimi, toistot):
    """
    Toistaa nimen halutulla tavalla halutun määrän
    :param nimi:
    :param toistot:
    :return:
    """
    for i in range(toistot):
        print(f"{nimi}, {nimi} Bear")


def verse(teksti, nimi):
    """
    toistaa säkeistön
    :param teksti:
    :param nimi:
    :return:
    """
    print(teksti)
    print(nimi + ", " + nimi)
    print(teksti)
    repeat_name(nimi, 3)
    print(teksti)
    repeat_name(nimi, 1)


def main():
    verse("I know someone you don't know", "Yogi")
    print()
    verse("Yogi has a best friend too", "Boo Boo")
    print()
    verse("Yogi has a sweet girlfriend", "Cindy")


if __name__ == "__main__":
    main()
