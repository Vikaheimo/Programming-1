"""
COMP.CS.100
Tekijä: Vili Ikäheimo
Opiskelijanumero: 150286761
"""


def main():
    numero = int(input("Choose a number: "))
    for i in range(1,11):
        print(str(i)+" * " + str(numero) + " = " + str(numero*i))

if __name__ == "__main__":
    main()
