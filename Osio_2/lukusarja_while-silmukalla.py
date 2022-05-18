"""
COMP.CS.100
Tekijä: Vili Ikäheimo
Opiskelijanumero: 150286761
"""


def main():
    numero = int(input("How many numbers would you like to have? "))
    kierrokset = 1
    
    while numero >= kierrokset:
        if kierrokset % 3 == 0 and kierrokset % 7 == 0:
            print("zip boing")

        elif kierrokset % 7 ==0:
            print("boing")

        elif kierrokset % 3 == 0:
            print("zip")

        else:
            print(kierrokset)

        kierrokset += 1


if __name__ == "__main__":
    main()
