"""
COMP.CS.100
Tekijä: Vili Ikäheimo
Opiskelijanumero: 150286761
Tehtävä
"""


def input_to_list(x):
    """
    kysyy kuinka monta lukua kysytään ja palauttaa
    listan numeroista
    :param x:
    :return:
    """
    lista = []
    print(f"Enter {x} numbers:")

    for i in range(x):
        lista.append(input())
    return lista


def main():
    kpl = int(input("How many numbers do you want to process: "))
    lista = input_to_list(kpl)

    luku_jota_etsia = input("Enter the number to be searched: ")
    laskuri = 0

    for a in lista:
        if a == luku_jota_etsia:
            laskuri += 1

    if laskuri > 0:
        print(f"{luku_jota_etsia} shows up {laskuri} times among the numbers you have entered.")

    else:
        print(f"{luku_jota_etsia} is not among the numbers you have entered.")


if __name__ == "__main__":
    main()
