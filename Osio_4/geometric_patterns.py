"""
COMP.CS.100
Tekijä: Vili Ikäheimo
Opiskelijanumero: 150286761
Tehtävä
"""
from math import pi


def tarkistus(luku):
    """
    tarkastaa onko luku oikein
    :param luku:
    :return:
    """
    if luku > 0:
        return False
    return True


def print_circumference(c):
    """
    tulostaa ympärysmitan
    :param c:
    :return:
    """
    print(f"The circumference is {c:.2f}")


def print_area(a):
    """
    tulostaa pinta - alan
    :param a:  pinta - ala
    :param c: ympärysmitta
    :return:
    """
    print(f"The surface area is {a:.2f}")


def square():
    """
    kysyy käyttäjältä neliön sivun pituuden
    :return:
    """
    luku = 0

    while tarkistus(luku):
        luku = float(input("Enter the length of the square's side: "))

    area = luku ** 2
    circumference = 4 * luku
    print_circumference(circumference)
    print_area(area)


def rectangle():
    """
    kysyy suorakaiteen sivujen pituudet
    :return:
    """
    sivu1 = 0
    sivu2 = 0

    while tarkistus(sivu1):
        sivu1 = float(input("Enter the length of the rectangle's side 1: "))
    while tarkistus(sivu2):
        sivu2 = float(input("Enter the length of the rectangle's side 2: "))

    area = sivu1 * sivu2
    circumference = 2 * (sivu1 + sivu2)
    print_circumference(circumference)
    print_area(area)


def circle():
    """
    kysyy ympyrän sivujen pituudet
    :return:
    """
    radius = 0

    while tarkistus(radius):
        radius = float(input("Enter the circle's radius: "))

    area = pi*radius**2
    circumference = 2 * pi * radius
    print_circumference(circumference)
    print_area(area)


def menu():
    """
    Print a menu for user to select which geometric pattern to use in calculations.
    """
    while True:
        answer = input("Enter the pattern's first letter or (q)uit: ")

        if answer == "s":
            square()

        elif answer == "c":
            circle()

        elif answer == "r":
            rectangle()

        elif answer == "q":
            return

        else:
            print("Incorrect entry, try again!")

        # Empty row for the sake of readability.
        print()


def main():
    menu()
    print("Goodbye!")


if __name__ == "__main__":
    main()
