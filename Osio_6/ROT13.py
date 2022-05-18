"""
COMP.CS.100
Tekijä: Vili Ikäheimo
Opiskelijanumero: 150286761
"""


def encrypt(letter):
    """
    salaa annetun merkin rot-13 salauksella ja palauttaa salatun merkin
    :param letter:
    :return:
    """
    selkokielinen = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"]
    rotated = selkokielinen[13:] + selkokielinen[:13]
    if letter.lower() in selkokielinen:
        paikka = selkokielinen.index(letter.lower())
        if letter in selkokielinen:
            return rotated[paikka]
        else:
            return rotated[paikka].upper()
    else:
        return letter


def row_encryption(merkkijono):
    """
    otta annetun merkkijonon ja palauttaa rot-13 salatun version siitä encrypt
    funktiota apua käyttäen
    :param merkkijono:
    :return:
    """
    return_value = ""
    selkokielinen = ["a","b","c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"]
    for m in merkkijono:
        return_value += encrypt(m)
    return return_value


def main():
    print(encrypt("a"))

if __name__ == "__main__":
    main()
