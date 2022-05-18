"""
COMP.CS.100
Tekijä: Vili Ikäheimo
Opiskelijanumero: 150286761
Tehtävä
"""


def main():
    lista = []
    print("Give 5 numbers:")
    for i in range(5):
        lista.append(int(input("Next number: ")))

    print("The numbers you entered that were greater than zero were:")
    for element in lista:
        if element > 0:
            print(element)


if __name__ == "__main__":
    main()
