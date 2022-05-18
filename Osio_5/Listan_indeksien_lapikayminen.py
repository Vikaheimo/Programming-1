"""
COMP.CS.100
Tekijä: Vili Ikäheimo
Opiskelijanumero: 150286761
Tehtävä
"""


def main():
    lista = []
    print("Give 5 numbers:")
    for i in range(1, 6):
        lista.append(int(input("Next number: ")))

    print("The numbers you entered, in reverse order:")
    lista.reverse()
    for a in lista:
        print(a)


if __name__ == "__main__":
    main()
