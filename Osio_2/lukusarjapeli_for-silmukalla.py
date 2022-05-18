"""
COMP.CS.100
Tekijä: Vili Ikäheimo
Opiskelijanumero: 150286761
"""


def main():
    numero = int(input("How many numbers would you like to have? "))

    for i in range(1,numero+1):
        if i % 3 == 0 and i % 7 == 0:
            print("zip boing")

        elif i % 7 ==0:
            print("boing")

        elif i % 3 == 0:
            print("zip")

        else:
            print(i)


if __name__ == "__main__":
    main()
