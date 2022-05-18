"""
COMP.CS.100
Tekijä: Vili Ikäheimo
Opiskelijanumero: 150286761
"""

EPSILON = 0.000000001


def compare_floats(num1, num2, virhetoleranssi):
    """
    kysyy kaksi numeroa palauttaa onko niiden välinen ero suurempi kuin virhetolernassi
    :param num1:
    :param num2:
    :param virhetoleranssi:
    :return:
    """
    return abs(num1 - num2) < virhetoleranssi


def main():
    print(compare_floats(0.0000000000000000000001, 0.00000000000000000001, EPSILON))


if __name__ == "__main__":
    main()
