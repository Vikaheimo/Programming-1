"""
COMP.CS.100
Tekijä: Vili Ikäheimo
Opiskelijanumero: 150286761
"""


def main():
    numero = int(input("Choose a number: "))
    luku = 0
    kierros = 1
    while luku <= 100:
        luku = kierros * numero
        print(str(kierros), "*", str(numero), "=", luku )
        kierros += 1

if __name__ == "__main__":
    main()
