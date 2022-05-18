"""
COMP.CS.100
Tekijä: Vili Ikäheimo
Opiskelijanumero: 150286761
Tehtävä
"""
from math import sqrt


def area(a, b, c):
    """
    laskee ja palauttaa kolmion piinta-alan arvon annetuilla sivun pituuksilla
    :param a:
    :param b:
    :param c:
    :return:
    """
    a = float(a)
    b = float(b)
    c = float(c)
    s = (a+b+c)/2
    ala = sqrt(s*(s-a)*(s-b)*(s-c))
    return ala


def main():
    line1 = input("Enter the length of the first side: ")
    line2 = input("Enter the length of the second side: ")
    line3 = input("Enter the length of the third side: ")

    pinta_ala = area(line1, line2, line3)
    print(f"The triangle's area is {pinta_ala:.1f}")


if __name__ == "__main__":
    main()
