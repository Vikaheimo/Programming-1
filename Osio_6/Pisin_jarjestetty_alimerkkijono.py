"""
COMP.CS.100
Tekijä: Vili Ikäheimo
Opiskelijanumero: 150286761
"""


def longest_substring_in_order(merkkijono):
    """
    ottaa parametriksi merkkijonon ja palauttaa pisimmän merkkijonon
    annetusta merkkijonosta joka on aakkosjärjestyksessä
    :param merkkijono:
    :return:
    """
    edellinnen_merkki = ""
    pisin_merkkijono = ""
    edelliset_merkit = ""

    for m in merkkijono:
        if edellinnen_merkki >= m:
            edelliset_merkit = ""

        edelliset_merkit += m

        if len(edelliset_merkit) > len(pisin_merkkijono):
            pisin_merkkijono = edelliset_merkit
        edellinnen_merkki = m

    return pisin_merkkijono



def main():
    print(longest_substring_in_order("efghijklmnopopqefgabcdeabcdefghijklm"))


if __name__ == "__main__":
    main()
