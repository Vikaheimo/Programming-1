"""
COMP.CS.100
Tekijä: Vili Ikäheimo
Opiskelijanumero: 150286761
"""


def main():
    for kuukausi in range(1, 13):
        for paivamaara in range(1, 32):
            if kuukausi < 8:
                if kuukausi == 2 and paivamaara < 29:
                    print(f"{paivamaara}.{kuukausi}.")

                elif kuukausi % 2 == 1:
                    print(f"{paivamaara}.{kuukausi}.")

                elif paivamaara < 31 and kuukausi != 2:
                    print(f"{paivamaara}.{kuukausi}.")
            else:
                if kuukausi % 2 == 0:
                    print(f"{paivamaara}.{kuukausi}.")

                elif paivamaara < 31:
                    print(f"{paivamaara}.{kuukausi}.")


if __name__ == "__main__":
    main()
