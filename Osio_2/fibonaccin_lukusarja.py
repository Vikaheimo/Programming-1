"""
COMP.CS.100
Tekijä: Vili Ikäheimo
Opiskelijanumero: 150286761
"""


def main():
    lukumaara = int(input("How many Fibonacci numbers do you want? "))
    kierros = 1

    luku_a = 1
    luku_b = 1

    while kierros <= lukumaara:
        print(f"{kierros}. {luku_a}")
        kierros += 1
        luku_c = luku_a + luku_b
        luku_a = luku_b
        luku_b = luku_c


if __name__ == "__main__":
    main()
