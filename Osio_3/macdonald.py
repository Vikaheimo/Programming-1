"""
COMP.CS.100
Tekijä: Vili Ikäheimo
Opiskelijanumero: 150286761
Tehtävä 3.6.1
"""


def print_verse(elain, aani):
    """
    Tulostaa Old mac donald laulun sanoituksen
    :param elain: Eläin
    :param aani: Eläimen ääni
    :return: None
    """
    print("Old MACDONALD had a farm")
    print("E-I-E-I-O")
    print("And on his farm he had a " + elain)
    print("E-I-E-I-O")
    print("With a", aani, aani, "here")
    print("And a", aani, aani, "there")
    print("Here a", aani + ", there a", aani)
    print("Everywhere a", aani, aani)
    print("Old MacDonald had a farm")
    print("E-I-E-I-O")


def main():
    print_verse("cow", "moo")
    print()
    print_verse("pig", "oink")
    print()
    print_verse("duck", "quack")
    print()
    print_verse("horse", "neigh")
    print()
    print_verse("lamb", "baa")


if __name__ == "__main__":
    main()
