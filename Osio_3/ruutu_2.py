"""
COMP.CS.100
Tekijä: Vili Ikäheimo
Opiskelijanumero: 150286761
"""


def read_input(teksti):
    """
    kysyy tekstiä jota esittää input kohdassa
    ja sitteen kyselee lukua kunnes käyttäjä antaa sallitun luvun
    :param teksti:
    :return:
    """
    num = -0.1
    while num <= 0:
         num = int(input(teksti))

    return num


def print_box(leveys, korkeus, merkki):
    """
    tulostaa laatikon hlaudulla korkeudella ja leveydelä
    :param leveys:
    :param korkeus:
    :param merkki:
    :return:
    """
    for i in range(int(korkeus)):
        print(int(leveys)*merkki)


def main():
    width = read_input("Enter the width of a frame: ")
    height = read_input("Enter the height of a frame: ")
    mark = input("Enter a print mark: ")
    print()
    print_box(width, height, mark)


if __name__ == "__main__":
    main()
