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
    for m in merkkijono:
        return_value += encrypt(m)
    return return_value


def read_message():
    """
    kysyy viestin ja palauttaa viestit listassa
    :return:
    """
    teksti_lista = []
    rivi = input()
    while rivi != "":
        teksti_lista.append(rivi)
        rivi = input()
    return teksti_lista


def main():
    print("Enter text rows to the message. Quit by entering an empty row.")
    msg = read_message()

    print("ROT13:")
    for i in msg:
        print(row_encryption(i))


if __name__ == '__main__':
    main()