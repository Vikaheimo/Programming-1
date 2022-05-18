"""
COMP.CS.100
Tekijä: Vili Ikäheimo
Opiskelijanumero: 150286761
"""


def count_abbas(merkkijono):
    """
    ottaa merkkijonon arvoksi ja palauttaa kuinka nonta kertaa abba sisältyy merkkijonoon
    :param merkkijono:
    :return:
    """
    counter = 0
    if len(merkkijono) < 4:
        return 0
    edelliset = "aaa"
    for m in merkkijono:
        edelliset += m
        if edelliset == "abba":
            counter += 1
        edelliset = edelliset[1:]
    return counter


def main():
    print(count_abbas("abbabbabba"))


if __name__ == "__main__":
    main()
