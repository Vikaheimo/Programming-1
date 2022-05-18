"""
COMP.CS.100
Tekijä: Vili Ikäheimo
Opiskelijanumero: 150286761
"""


def read_message():
    """
    kysyy viestin ja palauttaa viestit listassa
    :return:
    """
    teksti_lista = []
    rivi = input()
    while rivi != "":
        teksti_lista.append(rivi)
        rivi = input()
    return teksti_lista


def main():
    print("Enter text rows to the message. Quit by entering an empty row.")
    msg = read_message()

    print("The same, shouting:")
    for i in msg:
        print(i.upper())


if __name__ == "__main__":
    main()

