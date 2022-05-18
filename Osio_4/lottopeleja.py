"""
COMP.CS.100
Tekijä: Vili Ikäheimo
Opiskelijanumero: 150286761
Tehtävä
"""
from math import factorial


def todennakoisyys(kaikki_pallot, nostetut_pallot):
    """
    Ottaa pallojen määrän ja nostettujen pallojen määrän ja
    tulostaa kuinka modennla tavalla ne voidaan järjestellä
    :param kaikki_pallot: kaikkien palljoen määrä
    :param nostetut_pallot: nostettujen pallojen määrä
    :return:
    """
    x = factorial(kaikki_pallot - nostetut_pallot)
    toden = factorial(kaikki_pallot) / (x * factorial(nostetut_pallot))

    return toden


def virheet(kaikki_pallot, nosteut_pallot):
    """
    testaa virheet todennäköisyysfunktiolle, eli siis onko pallojen määrä oikea
    ja onko kaikkien pallojen määrä suurempi tai yhtäsuurin kuin nostettujen pallojen
    :param kaikki_pallot:
    :param nosteut_pallot:
    :return:
    """
    if kaikki_pallot <= 0 or nosteut_pallot <= 0:
        print("The number of balls must be a positive number.")
        return True
    elif kaikki_pallot < nosteut_pallot:
        print("At most the total number of balls can be drawn.")
        return True


def main():

    all = int(input("Enter the total number of lottery balls: "))
    picked = int(input("Enter the number of the drawn balls: "))

    if not virheet(all, picked):
        print(f"The probability of guessing all {picked} balls correctly is 1/{todennakoisyys(all, picked):.0f}")


if __name__ == "__main__":
    main()
