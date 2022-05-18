"""
COMP.CS.100
Tekijä: Vili Ikäheimo
Opiskelijanumero: 150286761
Tehtävä
"""


def main():
    lista = []
    for i in range(1,6):
            lista.append(float(input(f"Enter the time for performance {i}: ")))
    summa = 0
    lista.remove(min(lista))
    lista.remove(max(lista))
    for n in lista:
        summa += n
    print(f"The official competition score is {summa/3:.2f} seconds.")


if __name__ == "__main__":
    main()
